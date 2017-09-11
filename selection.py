#Lealie Jaressy Morales Ortiz 1661971
#Matematicas Computacionales

>>> cnt=0
>>> def selection(arr):
	global cnt
	for i in range(0,len(arr)-1):
		val=i
		for j in range (i+1,len(arr)):
			cnt=cnt+1
			if arr[j]<arr[val]:
				val=j
		if val!=i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return arr

>>> A=[3,1,89,7]
>>> selection(A)
[1, 3, 7, 89]
>>> 