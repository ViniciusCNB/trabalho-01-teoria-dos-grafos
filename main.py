import grafo
import time

G = grafo.Grafo()

print("#==============================#")
arquivo = input("Informe o arquivo: ")
vertOrigem = int(input("Origem: "))
vertDestino = int(input("Destino: "))

G.ler_arquivo(arquivo)

# Iniciação do cronômetro
timerStart = time.time()
print("Processando...")

match arquivo:
    case "facebook_combined.txt":
        print("Arquivo: facebook_combined.txt")
        print("Algoritmo: Busca Largura")
        result = G.busca_largura(vertOrigem, vertDestino)
    case "toy.txt":
        print("Arquivo: toy.txt")
        print("Algoritmo: Dijkstra")
        result = G.dijkstra(vertOrigem, vertDestino)
    case "rg300_4730.txt":
        print("Arquivo: rg300_4730.txt")
        print("Algoritmo: Dijkstra")
        result = G.dijkstra(vertOrigem, vertDestino)
    case "rome99c.txt":
        print("Arquivo: rome99c.txt")
        print("Algoritmo: Bellman-Ford")
        result = G.bellman_ford(vertOrigem)
    case "USA-road-dt.DC.txt":
        print("Arquivo: USA-road-dt.DC.txt")
        print("Algoritmo: Bellman-Ford")
        result = G.bellman_ford(vertOrigem)
    case "USA-road-dt.NY.txt":
        print("Arquivo: USA-road-dt.NY.txt")
        print("Algoritmo: Bellman-Ford")
        result = G.bellman_ford(vertOrigem)
    case "web-Google.txt":
        print("Arquivo: web-Google.txt")
        print("Algoritmo: Bellman-Ford")
        result = G.bellman_ford(vertOrigem)

# Desestruturação da var result
(dist, pred) = result

# Obtenção do custo do caminho mínimo
custo = dist[vertDestino]

# Obtenção do caminho mínino entro o par de vértices
caminho = G.recuperar_caminhos(vertOrigem, vertDestino, pred)

print("Caminho:", caminho)
print("Custo:", custo)

# Finalização do cronômetro
timerEnd = time.time()

print("Tempo:", timerEnd-timerStart, "segundos")
print("#==============================#")
