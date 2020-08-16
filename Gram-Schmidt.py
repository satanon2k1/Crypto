def ScalaMulti(u, v):
	if len(u) != len(v):
		return "None"

	scala = 0
	for i in range(len(u)):
		scala += u[i] * v[i]

	return scala

def DemensionalMulti(k, u):
	newU = []
	for i in u:
		newU.append(i * k)

	return newU

def SubtractVector(u, v):
	if len(u) != len(v):
		return "None"

	newU = []
	for i in range(len(u)):
		newU.append(u[i] - v[i])

	return newU

def Size(u):
	size = 0
	for i in u:
		size += i * i

	return size

V = [
[4,1,3,-1],
[2,1,-3,4],
[1,0,-2,7],
[6,2,9,-5]
]

U = [V[0]]

for i in range(1, len(V)):
	ui = V[i]
	for j in range(i):
		uij = ScalaMulti(V[i], U[j]) / Size(U[j])
		ui = SubtractVector(ui, DemensionalMulti(uij, U[j]))

	U.append(ui)

print(U)