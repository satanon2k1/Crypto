from Crypto.Util.number import GCD

def PollardProcess(a, N):
	for j in range(1, N):
		a = pow(a, j, N)
		d = GCD(a - 1, N)
		if 1 < d and d < N:
			return d
	return 1

def Pollard(N):
	for i in range(2, 10):
		result = PollardProcess(i, N)
		if result != 1:
			return result
	return None

print(Pollard(168441398857))