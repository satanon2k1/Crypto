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
		
	k = 0
	while True:
		inverseMod = (modulo * k + 1) % number
		inverse = (modulo * k + 1) / number
		if inverseMod == 0:
			return int(inverse)
		else:
			k += 1
			
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
		Sum += cList[i] * Ni * Inverse(Ni, nList[i])
		
	print(int(Sum % N))
	
nList = [10807,33109,44923]
cList = [3807,19501,24949]
# m = 8101
# e = 3
CRT(nList, cList)
