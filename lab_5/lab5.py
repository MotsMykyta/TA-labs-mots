INF = 9999999
V = 8

G_matrix = [
    [0,8,2,4,3,0,0,0],
    [8,0,0,0,6,3,0,0],
    [2,0,0,6,0,7,0,4],
    [4,0,6,0,1,0,0,0],
    [3,6,0,1,0,0,4,0],
    [0,3,7,0,0,0,3,1],
    [0,0,0,0,4,3,0,5],
    [0,0,4,0,0,1,5,0]
]


def prim_algorithm():
    print("=== РЕЗУЛЬТАТ РОБОТИ АЛГОРИТМУ ПРИМА ===")
    selected = [False] * V
    no_edge = 0
    selected[0] = True
    total_weight = 0

    print("Edge: Weight")
    while no_edge < V-1:
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if(not selected[j] and G_matrix[i][j] != 0):
                        if minimum > G_matrix[i][j]:
                            minimum = G_matrix[i][j]
                            x = i
                            y = j

        print(f"{x + 1} - {y + 1} : {G_matrix[x][y]}")
        total_weight += G_matrix[x][y]
        selected[y] = True
        no_edge += 1

    print(f"Загальна вага МКД (Прим): {total_weight}\n")

class GraphKruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.G = []
        self.T = []
        self.parent = [i for i in range(vertices + 1)]

    def add_weighted_edge(self, u, v, w):
        self.G.append((w, u, v))

    def find_set(self, i):
        if i == self.parent[i]:
            return i
        return self.find_set(self.parent[i])

    def union_set(self, u, v):
        self.parent[u] = self.parent[v]

    def kruskal(self):
        self.G.sort(key=lambda x: x[0])
        for w, u, v in self.G:
            u_rep = self.find_set(u)
            v_rep = self.find_set(v)
            if u_rep != v_rep:
                self.T.append((w, u, v))
                self.union_set(u_rep, v_rep)

    def print_mst(self):
        print("=== РЕЗУЛЬТАТ РОБОТИ АЛГОРИТМУ КРУСКАЛА ===")
        print("Edge : Weight")
        total_weight = 0
        for w, u, v in self.T:
            print(f"{u} - {v} : {w}")
            total_weight += w
        print(f"Загальна вага МКД (Крускал): {total_weight}\n")


if __name__ == "__main__":
    prim_algorithm()

    g=GraphKruskal(V)
    edges_v15 = [
        (1, 3, 2), (1, 2, 8), (1, 4, 4), (1, 5, 3),
        (2, 5, 6), (2, 6, 3), (3, 4, 6), (3, 6, 7),
        (3, 8, 4), (4, 5, 1), (5, 7, 4), (6, 7, 3),
        (6, 8, 1), (7, 8, 5)
    ]

    for u, v, w in edges_v15:
        g.add_weighted_edge(u, v, w)
    g.kruskal()
    g.print_mst()