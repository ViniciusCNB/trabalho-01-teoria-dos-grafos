class Grafo:
    def __init__(self,
                 num_vert=0,
                 num_arestas=0,
                 lista_adj=None,
                 mat_adj=None,
                 arestas=None):
        self.num_vert = num_vert
        self.num_arestas = num_arestas
        if lista_adj == None:
            self.lista_adj = [[] for _ in range(num_vert)]
        else:
            self.lista_adj = lista_adj

        if mat_adj == None:
            self.mat_adj = [[0 for _ in range(num_vert)]
                            for _ in range(num_vert)]
        else:
            self.mat_adj = mat_adj

        if arestas == None:
            self.arestas = [[] for _ in range(num_arestas)]
        else:
            self.arestas = arestas

    # Função que adiciona aresta de u a v com peso w
    def add_aresta(self, u, v, w=1):
        if u < self.num_vert and v < self.num_vert:
            self.num_arestas += 1
            self.arestas.append((u, v, w))
            self.lista_adj[u].append((v, w))
            self.mat_adj[u][v] = w
        else:
            print("Aresta Inválida!")

    # Função que determina se v é adjacente a u
    def adjacente(self, u, v):
        if self.mat_adj[u][v] != 0:
            return True
        else:
            return False

    # Função que retorna a lista dos vertices adjacentes a u
    def adjacentes(self, u):
        adj = []
        for i in range(self.lista_adj[u]):
            (v, w) = self.lista_adj[u][i]
            adj.append(v)
        return adj

    # Função que lê arquivo de grafo no formato DIMACS
    def ler_arquivo(self, nome_arq):
        try:
            arq = open(nome_arq)
            # Leitura do cabeçalho
            str = arq.readline()
            str = str.split(" ")
            self.num_vert = int(str[0])
            self.num_arestas = int(str[1])
            # Inicialização das estruturas de dados
            self.lista_adj = [[] for _ in range(self.num_vert)]
            self.mat_adj = [[0 for _ in range(self.num_vert)]
                            for _ in range(self.num_vert)]
            # Lê cada aresta do arquivo
            for _ in range(0, self.num_arestas):
                str = arq.readline()
                str = str.split(" ")
                u = int(str[0])
                v = int(str[1])
                w = int(str[2])
                self.add_aresta(u, v, w)
        except IOError:
            print("Não foi possível encontrar ou ler o arquivo!")
            exit()

    # Função que retorna o vértice de menor distância em Q
    def menor_dist(self, dist, Q):
        u = None
        min_dist = float("inf")
        for i in Q:
            if dist[i] < min_dist:
                u = i
                min_dist = dist[i]
        return u

    # Algoritmo de Dijkstra
    def dijkstra(self, s, t):
        dist = [float("inf") for _ in range(len(self.lista_adj))]
        pred = [None for _ in range(len(self.lista_adj))]
        dist[s] = 0
        Q = [i for i in range(len(self.lista_adj))]

        while len(Q) != 0:
            u = self.menor_dist(dist, Q)
            Q.remove(u)
            for (v, w) in self.lista_adj[u]:

                if(u == t):
                    break

                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
        return (dist, pred)

    # Algoritmo de Bellman-Ford
    def bellman_ford(self, s):
        dist = [float("inf") for _ in range(len(self.lista_adj))]
        pred = [None for _ in range(len(self.lista_adj))]
        dist[s] = 0
        for i in range(0, self.num_vert-1):
            trocou = False
            for (u, v, w) in self.arestas:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    trocou = True
            if trocou == False:
                break
        return (dist, pred)

    # Algoritmo de Busca em Largura
    def busca_largura(self, s, t):
        dist = [float("inf") for _ in range(len(self.lista_adj))]
        pred = [None for _ in range(len(self.lista_adj))]
        Q = [s]
        dist[s] = 0
        while len(Q) != 0:
            u = Q.pop(0)
            for (v, w) in self.lista_adj[u]:
                if dist[v] == float("inf"):
                    Q.append(v)
                    dist[v] = dist[u] + 1
                    pred[v] = u
                    if pred[t] != None:
                        break
        return (dist, pred)

    # Função para recuperar o caminho entre um par de vértices s, t
    def recuperar_caminhos(self, s, t, pred):
        C = [t]
        aux = t
        while aux != s:
            aux = pred[aux]
            C.append(aux)
        C.reverse()
        return C
