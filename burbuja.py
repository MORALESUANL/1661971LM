#Python 3.6.2
#Leslie Jaressy Morales Ortiz.

def burbuja(A):
	for i in range(1, len(A)):
		for j in range(0,len(A)-1):
			if(A[j+i]<A[j]):
				aux=A[j]
				A[j]=A[j+1]
				A[j+1]=aux
	print(A)

#programa principaL
A=[6,5,3,1,8,7,2,4]
burbuja(A)
input("presione enter para continuar")