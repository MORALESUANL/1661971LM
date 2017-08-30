cnt=0

def minimo(arr):
    m=arr[0]
    global cnt
    for l in arr:
        cnt+=1
        if(l<m):
            m=l
    return m

def ordenar(arr):
    aux=arr[:]
    arrsort=[]
    for m in range(len(aux)):
        l=minimo(aux)
        aux.remove(l)
        arrsort.append(l)
    return arrsort

import random
p=random.sample(range(0,100),40)
print("Arreglo desordenado: ", p)
psort=ordenar(p)
print("\nNumero de operaciones: ", cnt)
print("\nArreglo ordenado:", psort)
input("Presione Enter para continuar")