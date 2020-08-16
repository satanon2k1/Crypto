import random

def QuickSR(number, prime):
	return pow(number, (prime + 1) // 4, prime)

def QandS(prime):
	s = 0
	tmpPrime = prime - 1
	while tmpPrime % 2 == 0:
		s += 1
		tmpPrime //= 2

	return s, (prime - 1) // pow(2, s)

def RandomQNR(prime):
	z = random.randint(1, prime - 1)
	while LegendreCheck(z, prime):
		z = random.randint(1, prime - 1)

	return z

def LegendreCheck(number, prime):
	if pow(number, (prime - 1) // 2, prime) == 1:
		return True

	return False

def Tonelli_Shanks(number, prime):
	S, Q = QandS(prime)
	z = RandomQNR(prime)
	M, c, t, R = S, pow(z, Q, prime), pow(number, Q, prime), pow(number, (Q + 1) // 2, prime)
	while True:
		if t == 0:
			return 0
		elif t == 1:
			return R

		i = 0
		for j in range(1, M):
			if pow(t, pow(2, j), prime) == 1:
				i = j
				break

		b = pow(c, pow(2, M - i - 1), prime)
		M, c, t, R = i, (b * b) % prime, (t * b * b) % prime, (R * b) % prime

def main(number, prime):
	isQNR = LegendreCheck(number, prime)
	if isQNR and prime % 4 == 3:
		return QuickSR(number, prime)
	elif isQNR and prime % 4 == 1:
		return Tonelli_Shanks(number, prime)
	else:
		return "None"

print(main(4, 29))
