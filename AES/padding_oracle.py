import concurrent.futures
import os

def xor(a: bytes, b: bytes) -> bytes:
    lenb = len(b)
    return bytes([a[i] ^ b[i % lenb] for i in range(len(a))])


def pad(text: bytes, size: int):
    padding = size - (len(text) % size)
    return text + bytes([padding])*padding


def brute(
    byte: bytes,
    plaintext: bytes,
    curBlock: bytes,
    prevBlock: bytes,
    oracle,
):
    index = len(plaintext)
    size = len(curBlock)
    tmpPlaintext = os.urandom(size - 1 - index) + bytes([byte]) + plaintext
    xorWith = os.urandom(size - 1 - index) + bytes([index+1])*(index+1)
    iv = xor(xor(tmpPlaintext, xorWith), prevBlock)
    test = oracle(iv, curBlock)
    return byte, test


def decryptBlock(
    curBlock: bytes,
    prevBlock: bytes,
    oracle,
    lastBlock: bool = False,
    threads: int = 8
) -> bytes:
    plaintext = b""
    i = 0
    while (i < 16):
        with concurrent.futures.ThreadPoolExecutor(threads) as executor:
            listResult = []
            result = 0
            for b in range(256):
                listResult.append(executor.submit(brute, byte = b, plaintext = plaintext, curBlock = curBlock, prevBlock = prevBlock, oracle = oracle))
            for tup in concurrent.futures.as_completed(listResult):
                byte, test = tup.result()
                if test:
                    result = byte
                    break
            if not lastBlock:
                plaintext = bytes([result]) + plaintext
                i += 1
            else:
                plaintext = bytes([result]) * result
                i = result
                lastBlock = False
    return plaintext


def decrypt(
    iv: bytes,
    ciphertext: bytes,
    blockSize: int,
    oracle,
    threads: int = 8
) -> bytes:
    ciphertextBlocks = [ciphertext[i:i+blockSize] for i in range(0, len(ciphertext), blockSize)]
    lenBlocks = len(ciphertextBlocks)
    plaintextBlocks = []
    for indexBlock in range(lenBlocks):
        curBlock = ciphertextBlocks[indexBlock]
        lastBlock = False
        if indexBlock == lenBlocks - 1:
            lastBlock = True
        if indexBlock == 0:
            prevBlock = iv
        else:
            prevBlock = ciphertextBlocks[indexBlock - 1]
        plaintextBlock = decryptBlock(curBlock, prevBlock, oracle, lastBlock, threads)
        plaintextBlocks.append(plaintextBlock)
    return b"".join(plaintextBlocks)


def encrypt(
    plaintext: bytes,
    blockSize: int,
    oracle,
    threads: int = 8
) -> bytes:
    plaintext = pad(plaintext, blockSize)
    plaintextBlocks = [plaintext[i:i+blockSize] for i in range(0, len(plaintext), blockSize)]
    ciphertextBlocks = [b""] * len(plaintextBlocks) + [os.urandom(blockSize)]
    for indexBlock in range(len(plaintextBlocks) - 1, -1, -1):
        cipher = ciphertextBlocks[indexBlock + 1]
        fakeIv = os.urandom(blockSize)
        fakePlaintext = decryptBlock(cipher, fakeIv, oracle, False, threads)
        plaintextBlock = plaintextBlocks[indexBlock]
        realIv = xor(xor(fakePlaintext, plaintextBlock), fakeIv)
        ciphertextBlocks[indexBlock] = realIv
    ciphertext = b"".join(ciphertextBlocks)
    iv, ciphertext = ciphertext[:16], ciphertext[16:]
    return iv, ciphertext