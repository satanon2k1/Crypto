from fractions import Fraction

def ContinuedFraction(e, n):
	result = []
	while True:
		q, r = n // e, n % e
		result.append(q)
		if r == 0:
			return result
		n, e = e, r

def Recursive(cf, first, i):
	if first <= i:
		return Fraction(1, cf[first] + Recursive(cf, first + 1, i))
	else:
		return 0

def Convergents(cf):
	result = []
	for i in range(len(cf)):
		node = Recursive(cf, 0, i)
		result.append(node)
	return result

def main(e, n):
	cf = ContinuedFraction(e, n)
	conv = Convergents(cf)
	q0 = 1
	c = pow(8101, e, n)
	for i in conv:
		q1 = i.denominator
		if pow(c, q1, n) == 8101:
			return q1
		else:
			for r in range(30):
				for s in range(30):
					d = r * q1 + s * q0
					if pow(c, d, n) == 8101:
						return d
			q0 = q1

print(main(17993, 90581))
