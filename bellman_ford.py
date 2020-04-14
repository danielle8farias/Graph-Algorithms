def criar_matriz_adjacencia(arquivo):  # Função que lê o arquivo e adiciona a matriz de adjacência dada a uma matriz
    input = open(arquivo, "r")
    matriz_adjacencia = []
    for line in input:
        linha_aux = line.split(",")
        linha = []
        for j in linha_aux:
            linha.append(int(j))
        matriz_adjacencia.append(linha)
    return matriz_adjacencia


def inicializar(tamanho_matriz, distancias, vertice_origem):  # Inicializa a lista das distâncias
    inf = float("inf")
    for i in range(tamanho_matriz):
        if i != vertice_origem:
            distancias.append(inf)
        else:
            distancias.append(0)

    return distancias


def bellman_form(matriz_adjacencia, vertice_origem): # Função que recebe a matriz de adjacência e o vértice de origem e retorna uma lista com os caminhos mínimos entre o vértive de origem e os demais vértices
    vertice_origem -= 1
    distancias = []

    distancias = inicializar(len(matriz_adjacencia[vertice_origem]), distancias, vertice_origem)

    for i in range(len(matriz_adjacencia[vertice_origem])-1):
        for u in range(len(matriz_adjacencia[vertice_origem])):
            for v in range(len(matriz_adjacencia[vertice_origem])):
                if matriz_adjacencia[u][v] != 0:
                    soma = distancias[u] + matriz_adjacencia[u][v]
                    if soma < distancias[v]:
                        distancias[v] = soma

    return distancias


def mostrar_distancias(distancias, vertice_origem):  # Função que printa a lista de distâncias na tela
    for i in range(len(distancias)):
        print("D(" + str(vertice_origem) + "," + str(i+1) + "): " + str(distancias[i]))


matriz_adjacencia = criar_matriz_adjacencia("teste3.txt")  # Criando a matriz de adjacência, aqui usamos um arquivo teste3.txt
vertice_origem = 1  # Decidimos o vértice de origem; nesse caso, o primeiro, já que a numeração é de 1 a N
distancias = bellman_form(matriz_adjacencia, vertice_origem)  # Pegamos a lista contendo as distâncias do vértice de origem aos outros vértices
mostrar_distancias(distancias, vertice_origem)  # Usamos essa função para printar a lista na tela
