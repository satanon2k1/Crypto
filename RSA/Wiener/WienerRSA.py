'''
require sage installed
'''

from sage.all import *

def main(e, n):
	cf = continued_fraction(e / n)
	conv = cf.convergents()
	q0 = 1
	c = pow(8101, e, n)
	for i in conv:
		q1 = int(i.denominator())
		if pow(c, q1, n) == 8101:
			return q1
		else:
			for r in range(30):
				for s in range(30):
					d = r * q1 + s * q0
					if pow(c, d, n) == 8101:
						return d
			q0 = q1
