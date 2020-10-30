import multiprocessing as mp
from math import isqrt

n = 0x665166804cd78e8197073f65f58bca14e019982245fcc7cad74535e948a4e0258b2e919bf3720968a00e5240c5e1d6b8831d8fec300d969fccec6cce11dde826d3fbe0837194f2dc64194c78379440671563c6c75267f0286d779e6d91d3e9037c642a860a894d8c45b7ed564d341501cedf260d3019234f2964ccc6c56b6de8a4f66667e9672a03f6c29d95100cdf5cb363d66f2131823a953621680300ab3a2eb51c12999b6d4249dde499055584925399f3a8c7a4a5a21f095878e80bbc772f785d2cbf70a87c6b854eb566e1e1beb7d4ac6eb46023b3dc7fdf34529a40f5fc5797f9c15c54ed4cb018c072168e9c30ca3602e00ea4047d2e5686c6eb37b9
e = 0x2c998e57bc651fe4807443dbb3e794711ca22b473d7792a64b7a326538dc528a17c79c72e425bf29937e47b2d6f6330ee5c13bfd8564b50e49132d47befd0ee2e85f4bfe2c9452d62ef838d487c099b3d7c80f14e362b3d97ca4774f1e4e851d38a4a834b077ded3d40cd20ddc45d57581beaa7b4d299da9dec8a1f361c808637238fa368e07c7d08f5654c7b2f8a90d47857e9b9c0a81a46769f6307d5a4442707afb017959d9a681fa1dc8d97565e55f02df34b04a3d0a0bf98b7798d7084db4b3f6696fa139f83ada3dc70d0b4c57bf49f530dec938096071f9c4498fdef9641dfbfe516c985b27d1748cc6ce1a4beb1381fb165a3d14f61032e0f76f095d
# cipher_text = 0x503d5dd3bf3d76918b868c0789c81b4a384184ddadef81142eabdcb78656632e54c9cb22ac2c41178607aa41adebdf89cd24ec1876365994f54f2b8fc492636b59382eb5094c46b5818cf8d9b42aed7e8051d7ca1537202d20ef945876e94f502e048ad71c7ad89200341f8071dc73c2cc1c7688494cad0110fca4854ee6a1ba999005a650062a5d55063693e8b018b08c4591946a3fc961dae2ba0c046f0848fbe5206d56767aae8812d55ee9decc1587cf5905887846cd3ecc6fc069e40d36b29ee48229c0c79eceab9a95b11d15421b8585a2576a63b9f09c56a4ca1729680410da237ac5b05850604e2af1f4ede9cf3928cbb3193a159e64482928b585ac

def ContinuedFraction(e, n):
	result = []
	while True:
		q, r = n // e, n % e
		result.append(q)
		if r == 0:
			return result
		n, e = e, r

def Convergents(cf):
	result = []
	for i in range(len(cf)):
		k, d = 1, cf[i]
		for j in range(i - 1, -1, -1):
			tmp_k, tmp_d = k, d
			k, d = tmp_d, tmp_k + tmp_d * cf[j]
		result.append((k, d))
	return result

def run(num):
	q0 = 1
	for i in conv:
		k, q1 = i
		if q1 > isqrt(isqrt(n)):
			print(None)
			return
		if pow(c, q1, n) == 8101:
			print(q1)
			return
		else:
			for r in range(num, num + 10):
				for s in range(num, num + 10):
					d = r * q1 + s * q0
					if pow(c, d, n) == 8101:
						print(d)
						return
			q0 = q1

cf = ContinuedFraction(e, n)
conv = Convergents(cf)
c = pow(8101, e, n)

if __name__ == "__main__":
	processes = []
	for i in range(4):
		process = mp.Process(target = run, args = (i * 10 + 1,))
		processes.append(process)

	for process in processes:
		process.start()