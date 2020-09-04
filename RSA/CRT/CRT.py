from fractions import Fraction

def GCD(number1, number2):
	if number1 == 0:
		return number2
	if number2 == 0:
		return number1
	if number1 == number2:
		reuturn number1
	if number1 > number2:
		return GCD(number1 - number2, number2)
	return GCD(number1, number2 - number1)

def Inverse(number, modulo):
	number %= modulo
	if GCD(int(number), int(modulo)) != 1:
		return 0;

	x0, y0, x1, y1 = 0, 1, 1, 0
	while True:
		q, r = modulo // number, modulo % number
		x0, x1 = x1, x0 - q * x1
		y0, y1 = y1, y0 - q * y1

		if r == 0:
			break

		modulo, number = number, r

	return (x0, y0)

def CRT(nList, cList):
	if len(nList) != len(cList):
		print('Length of N and C invalid')
		return
	elif len(nList) == 0:
		print('Empty')
		return

	N = 1
	Sum = 0
	for n in nList:
		N *= n

	for i in range(len(cList)):
		Ni = Fraction(N, nList[i])
		Inv = Inverse(Ni, nList[i])[0]
		if Inv < 0:
			Inv += nList[i]

		Sum += cList[i] * Ni * Inv

	print(int(Sum % N))
	
nList = [10807,33109,44923]
cList = [3807,19501,24949]
# m = 8101
# e = 3
CRT(nList, cList)
