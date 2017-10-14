global contador
contador = 0
cache = {0: 0, 1: 1}

def fib(m):
	global contador
	contador = contador +1
	if m not in cache:
		cache[m] = fib(m-1) + fib(m-2)
	return cache[m]

y=[]
e=[]
for i in range(1,100):
	y.append(i)
	contador=0
	cache = {0: 0, 1: 1}
	fib(i)
	e.append(contador)


#>>> y
#>>> e
