# Grafos
# Representación de un grafo con listas de adyacencia y una búsqueda en profundidad (DFS):
# Ejemplo 1
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
visited = set()
# g.dfs(1, visited)  # Output: 1 2 4 3

# Ejemplo 2
# Crear un grafo
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# Recorrer el grafo con búsqueda en anchura (BFS)
from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(nodo)
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

bfs(grafo, "A")  # A, B, C, D, E, F
