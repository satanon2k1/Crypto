from fractions import Fraction

def CoprimeCheck(number1, number2):
	lowerNumber = number1
	if number1 > number2:
		lowerNumber = number2
		
	for i in range(2, lowerNumber+1):
		if number1 % i == 0 and number2 % i == 0:
			return False
			
	return True

def Inverse(number, modulo):
	number %= modulo
	if not CoprimeCheck(int(number), int(modulo)):
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
