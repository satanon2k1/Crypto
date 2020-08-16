from GramSchmidt import ScalaMulti, Size, SubtractVector, DemensionalMulti
# download GramSchmidt.py too :)

v1, v2 = [846835985, 9834798552], [87502093, 123094980]

while True:
	if Size(v1) > Size(v2):
		tmp = v1
		v1 = v2
		v2 = tmp

	m = ScalaMulti(v1, v2) // Size(v1)
	if m == 0:
		print(v1, v2)
		break

	v2 = SubtractVector(v2, DemensionalMulti(m, v1))

print(ScalaMulti(v1, v2))