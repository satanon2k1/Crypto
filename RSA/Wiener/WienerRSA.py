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

def main(e, n):
	cf = ContinuedFraction(e, n)
	conv = Convergents(cf)
	q0 = 1
	c = pow(8101, e, n)
	for i in conv:
		k, q1 = i
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
