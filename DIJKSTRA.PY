#Evaluacio 5
#Matematicas Computacionales "Algoritmo Dijkstra"
#Leslie Jaressy Morales Ortiz 1661971

#instrucciones:implementar el Algoritmo Dijkstra para la busqueda del camino mas corto entre dos nodos

from heapq import heappop, heappush


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
     #Algoritmo Dijkstra
     def shortest1(self,v):
        q= [(0, v, ())]
        dist = dict()
        visited = set()
        while len(q) > 0:
            (l, u, p) = heappop(q)
            if u not in visited:
                visited.add(u)
                dist[u]= (1,u,list(flatten(p))[::-1]+[u])
            p= (u,p)
            for n in self.vecinos[u]:
                if n not in visited:
                    el = self.E[(u,n)]
                    heappush(q, (l+el, n, p))
        return dist
   
# primero 5 nodos con 10 aristas 
print("primer grafo")
g=Grafo()
g.conecta('a','b', 1)
g.conecta('a','c', 31)
g.conecta('a','d', 45)
g.conecta('a','e', 8)
g.conecta('b','c', 21)
g.conecta('b','d', 11)
g.conecta('b','e', 5)
g.conecta('c','d', 7)
g.conecta('d','e', 2)
g.conecta('e','c', 13)
print(g.vecinos['a'])
print(g.shortest('a'))


# primero 10 nodos con 20 aristas 
print("segundo grafo")
g1=Grafo()
g1.conecta('a','b', 1)
g1.conecta('a','c', 31)
g1.conecta('a','d', 45)
g1.conecta('a','e', 8)
g1.conecta('a','f', 21)
g1.conecta('a','g', 11)
g1.conecta('a','h', 5)
g1.conecta('a','i', 7)
g1.conecta('a','j', 2)
g1.conecta('b','c', 13)
g1.conecta('b','d', 1)
g1.conecta('b','e', 31)
g1.conecta('b','f', 45)
g1.conecta('b','g', 8)
g1.conecta('b','h', 21)
g1.conecta('b','i', 11)
g1.conecta('b','j', 5)
g1.conecta('c','d', 7)
g1.conecta('c','e', 2)
g1.conecta('c','f', 13)
print(g1.vecinos['b'])
print(g1.shortest('b'))


# primero 15 nodos con 30 aristas 
print("tercer grafo")
g2=Grafo()
g2.conecta('a','b', 1)
g2.conecta('a','c', 31)
g2.conecta('a','d', 45)
g2.conecta('a','e', 8)
g2.conecta('a','f', 21)
g2.conecta('a','g', 11)
g2.conecta('a','h', 5)
g2.conecta('a','i', 7)
g2.conecta('a','j', 2)
g2.conecta('a','k', 13)
g2.conecta('a','l', 1)
g2.conecta('a','m', 31)
g2.conecta('a','n', 45)
g2.conecta('a','o', 8)
g2.conecta('b','c', 21)
g2.conecta('b','d', 11)
g2.conecta('b','e', 5)
g2.conecta('b','f', 7)
g2.conecta('b','g', 2)
g2.conecta('b','h', 13)
g2.conecta('b','i', 1)
g2.conecta('b','j', 31)
g2.conecta('b','k', 45)
g2.conecta('b','l', 8)
g2.conecta('b','m', 21)
g2.conecta('b','n', 11)
g2.conecta('b','o', 5)
g2.conecta('c','d', 7)
g2.conecta('c','e', 2)
g2.conecta('c','f', 13)
print(g2.vecinos['a'])
print(g2.shortest('a'))

# primero 20 nodos con 40 aristas 
print("cuarto grafo")
g3=Grafo()
g3.conecta('a','b', 1)
g3.conecta('a','c', 11)
g3.conecta('a','d', 45)
g3.conecta('a','e', 8)
g3.conecta('a','f', 21)
g3.conecta('a','g', 8)
g3.conecta('a','h', 5)
g3.conecta('a','i', 7)
g3.conecta('a','j', 2)
g3.conecta('a','k', 9)
g3.conecta('a','l', 1)
g3.conecta('a','m', 31)
g3.conecta('a','n', 45)
g3.conecta('a','o', 8)
g3.conecta('a','p', 21)
g3.conecta('a','q', 11)
g3.conecta('a','r', 5)
g3.conecta('a','s', 7)
g3.conecta('a','t', 2)
g3.conecta('b','c', 13)
g3.conecta('b','d', 1)
g3.conecta('b','e', 31)
g3.conecta('b','f', 45)
g3.conecta('b','g', 8)
g3.conecta('b','h', 21)
g3.conecta('b','i', 11)
g3.conecta('b','j', 5)
g3.conecta('b','k', 7)
g3.conecta('b','l', 2)
g3.conecta('b','m', 13)
g3.conecta('b','n', 31)
g3.conecta('b','o', 30)
g3.conecta('b','p', 8)
g3.conecta('b','q', 16)
g3.conecta('b','r', 11)
g3.conecta('b','s', 5)
g3.conecta('b','t', 7)
g3.conecta('c','d', 2)
g3.conecta('c','e', 4)
g3.conecta('c','f', 1)
print(g3.vecinos['a'])
print(g3.shortest('a'))


# primero 25 nodos con 50 aristas 
print("quinto grafo")
g4=Grafo()
g4.conecta('a','b', 5)
g4.conecta('a','c', 14)
g4.conecta('a','d', 4)
g4.conecta('a','e', 8)
g4.conecta('a','f', 18)
g4.conecta('a','g', 8)
g4.conecta('a','h', 5)
g4.conecta('a','i', 7)
g4.conecta('a','j', 2)
g4.conecta('a','k', 9)
g4.conecta('a','l', 1)
g4.conecta('a','m', 31)
g4.conecta('a','n', 18)
g4.conecta('a','o', 8)
g4.conecta('a','p', 21)
g4.conecta('a','q', 11)
g4.conecta('a','r', 5)
g4.conecta('a','s', 7)
g4.conecta('a','t', 2)
g4.conecta('a','v', 13)
g4.conecta('a','w', 1)
g4.conecta('a','x', 31)
g4.conecta('a','y', 100)
g4.conecta('b','c', 8)
g4.conecta('b','d', 21)
g4.conecta('b','e', 11)
g4.conecta('b','f', 5)
g4.conecta('b','g', 7)
g4.conecta('b','h', 2)
g4.conecta('b','i', 13)
g4.conecta('b','j', 31)
g4.conecta('b','k', 30)
g4.conecta('b','l', 8)
g4.conecta('b','m', 2)
g4.conecta('b','n', 11)
g4.conecta('b','o', 5)
g4.conecta('b','p', 7)
g4.conecta('b','q', 2)
g4.conecta('b','r', 4)
g4.conecta('b','s', 1)
g4.conecta('b','t', 31)
g4.conecta('b','u', 2)
g4.conecta('b','v', 8)
g4.conecta('b','w', 4)
g4.conecta('b','x', 11)
g4.conecta('b','y', 5)
g4.conecta('c','d', 7)
g4.conecta('c','e', 2)
g4.conecta('c','f', 4)
g4.conecta('c','g', 1)
print(g4.vecinos['a'])
print(g4.shortest('a'))