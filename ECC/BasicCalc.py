from Crypto.Util.number import inverse

# y**2 = x**3 + a*x + b [mod p]

a = 497
b = 1768
p = 9739

def ValidCheck(a, b, p):
	a %= p
	b %= p
	return 4 * (a ** 3) + 27 * (b ** 2) != 0

def ZeroCheck(A, p):
	if A['x'] % p == 0 and A['y'] % p == 0:
		return True
	return False

def SumTwoPoint(P, Q):
	global a, b, p
	if not ValidCheck(a, b, p):
		return False

	if ZeroCheck(P, p):
		return {"x": Q['x'] % p, "y": Q['y'] % p}
	elif ZeroCheck(Q, p):
		return {"x": P['x'] % p, "y": P['y'] % p}

	if P['x'] == Q['x'] and (P['y'] + Q['y']) % p == 0:
		return {"x": 0, "y": 0}

	k = (Q['y'] - P['y']) * inverse(Q['x'] - P['x'], p)
	if P == Q:
		k = ((3 * (P['x'] ** 2)) + a) * inverse(2 * P['y'], p)
	k %= p
	x = k ** 2 - P['x'] - Q['x']
	return {"x": x % p, "y": (k * (P['x'] - x) - P['y']) % p}

def SumAList(PointList):
	tmp = {"x": 0, "y": 0}
	for i in range(len(PointList)):
		tmp = SumTwoPoint(tmp, PointList[i])
		if tmp is False:
			return False
	return tmp

def Multi(P, n):
	tmp = {"x": 0, "y": 0}
	for i in range(n):
		tmp = SumTwoPoint(tmp, P)
		if tmp is False:
			return False
	return tmp

P = {"x": 493, "y": 5564}
Q = {"x": 1539, "y": 4742}
R = {"x": 4403, "y": 5202}

print(SumAList([Multi(P, 2), Q, R])) # P + P + Q + R