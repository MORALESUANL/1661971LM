from heapq import heappop, heappush
from copy import deepcopy
import random

import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] # empty list that will store current permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

class Fila:
    def __init__(self):
        self.fila= []
    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

class Pila:
    def __init__(self):
        self.pila= []
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)

def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def BFS(self,ni):
        visitados =[]
        f=Fila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def DFS(self,ni):
        visitados =[]
        f=Pila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
        dist = dict() #diccionario de distancias 
        visited = set() #Conjunto de visitados
        while len(q) > 0: #mientras exista un nodo pendiente
            (l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
            if u not in visited: # si no lo hemos visitado
                visited.add(u) #se agrega a visitados
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	#agrega al diccionario
            p = (u, p) #Tupla del nodo y el camino
            for n in self.vecinos[u]: #Para cada hijo del nodo actual
                if n not in visited: #si no lo hemos visitado
                    el = self.E[(u,n)] #se toma la distancia del nodo acutal hacia el nodo hijo
                    heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
        return dist #regresa el diccionario de distancias

    def kruskal(self):
        e = deepcopy(self.E)
        arbol = Grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
        nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                #print('u ',u, 'v ',v ,'c ', c)
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol

    def vecinoMasCercano(self):
        lv = list(self.V)
        random.shuffle(lv)
        ni = lv.pop()
        le = dict()
        while len(lv)>0:
            ln = self.v[ni]
            for nv in ln:
                le[nv]=self.E[(ni,nv)]
            menor = min(le.values())
            lv.append(menor)
            del lv[menor]
        return lv
        			
g= Grafo()#Necesitamos un grafo que este conectado con todos para que pueda encontrar el camino 
g.conecta('a','b', 2)
g.conecta('a','c', 4)
g.conecta('c','d', 7)
g.conecta('b','d', 5)
g.conecta('a','e', 1)
g.conecta('a','d', 4)
g.conecta('e','d', 3)
g.conecta('e','b', 6)
g.conecta('c','b', 12)
g.conecta('e','c', 6)

print(g.kruskal())
print(g.shortest('a'))

print(g)
k = g.kruskal()
#print([print(x, k.E[x]) for x in k.E])

for r in range(50):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += g.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1],g.E[(dfs[f],dfs[f+1])] )
            
    c += g.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
    print('costo',c)



o= Grafo()
o.conecta('Salinas Victoria', 'Sabinas Hidalgo', 85)
o.conecta('Salinas Victoria', 'El Carmen', 9)
o.conecta('Salinas Victoria', 'Mina', 30)
o.conecta('Salinas Victoria', 'Anáhuac', 168)
o.conecta('Salinas Victoria', 'Agualeguas', 120)
o.conecta('Salinas Victoria', 'Abasolo', 13)
o.conecta('Salinas Victoria', 'Marin', 61)
o.conecta('Salinas Victoria', 'Bustamante', 74)
o.conecta('Salinas Victoria', 'Zuazua', 26)

o.conecta('Sabinas Hidalgo','El Carmen', 93)
o.conecta('Sabinas Hidalgo','Mina', 122)
o.conecta('Sabinas Hidalgo','Anáhuac', 137)
o.conecta('Sabinas Hidalgo','Agualeguas', 87)
o.conecta('Sabinas Hidalgo','Abasolo', 92)
o.conecta('Sabinas Hidalgo','Marin', 90)
o.conecta('Sabinas Hidalgo','Bustamante',42)
o.conecta('Sabinas Hidalgo','Zuazua', 80)

o.conecta('El Carmen','Mina',22)
o.conecta('El Carmen','Anáhuac', 178)
o.conecta('El Carmen','Agualeguas', 139)
o.conecta('El Carmen','Abasolo', 5)
o.conecta('El Carmen','Marin', 54)
o.conecta('El Carmen','Bustamante', 82)
o.conecta('El Carmen','Zuazua', 40)

o.conecta('Mina','Anáhuac', 197)
o.conecta('Mina','Agualeguas', 156)
o.conecta('Mina','Abasolo', 17)
o.conecta('Mina','Marin', 70)
o.conecta('Mina','Bustamante', 102)
o.conecta('Mina','Zuazua', 56)

o.conecta('Anáhuac','Agualeguas', 230)
o.conecta('Anáhuac','Abasolo', 180 )
o.conecta('Anáhuac','Marin', 203)
o.conecta('Anáhuac','Bustamante', 105)
o.conecta('Anáhuac','Zuazua', 194)

o.conecta('Agualeguas','Abasolo', 139)
o.conecta('Agualeguas','Marin', 90)
o.conecta('Agualeguas','Bustamante', 127)
o.conecta('Agualeguas','Zuazua', 98)

o.conecta('Abasolo','Marin', 56)
o.conecta('Abasolo','Bustamante', 88)
o.conecta('Abasolo','Zuazua', 42 )

o.conecta('Marin','Bustamante', 109)
o.conecta('Marin','Zuazua', 11)

o.conecta('Bustamante','Zuazua', 98)




k = o.kruskal()
for r in range(50):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += o.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], o.E[(dfs[f],dfs[f+1])] )
            
    c += o.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0],o.E[(dfs[-1],dfs[0])])
    print('costo',c,'\n')



import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] # empty list that will store current permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l


data = list('abcdefghij')
tim=time.clock()
per = permutation(data)
print(time.clock()-tim)
