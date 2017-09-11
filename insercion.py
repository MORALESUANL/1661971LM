 cnt=0
#Leslie Jaressy Morales Ortiz.
#Insercion
def orden_por_insercion(array):
	global cnt
	for indice in range (1,len(array)):
		valor=array[indice]#valor es el elemento que estamos comparando
		i=indice-1	#i es el valor anterior al elemento que estamos comparando 
		while i>=0:
			cnt+=1
			if valor<array[i]:#comparamos valor con el elemento anterior
				array[i+1]=array[i]#intercambiamos  los valores
				array[i]=valor
				i-=1#Decrementamos en 1 el valor de i
			else:
				break
	return array

>>> A=[56,5,48,1]
>>> orden_por_insercion(A)
[1, 5, 48, 56]
>>> 
