def karatsuba(x,y):
	if (len(str(x))==1 or len(str(y))==1):
		return x*y
	else:
		n = max(len(str(x)), len(str(y)))
		nby2 = n/2

		a = x/(10**nby2)
		b = x%(10**nby2)
		c = y/(10**nby2)
		d = y%(10**nby2)

		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		adplusbc = karatsuba(a+b,c+d)-ac-bd

		#(2*nby2) converts the odd number to even number
		prod = (10**(2*nby2))*ac + (10**nby2)*adplusbc + bd
		return prod
print(karatsuba(125,10))
