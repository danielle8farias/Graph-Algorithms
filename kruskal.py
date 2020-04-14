def criar_matriz(n_linhas, n_colunas, valor):  # Cria uma matriz
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz


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

def menor_valor(peso):  # Função que calcula o menor valor das distâncias que ainda não foram fechadas
    menor = float("inf")
    menor_indice = 0
    for i in range(len(peso)):
        if menor > peso[i]:
            menor = peso[i]
            menor_indice = i
    return menor_indice


def mesma_aresta(i, j, arestas):  # Função para verificar se a aresta já foi adicionada a lista com todas as arestas
    r = False
    for k in arestas:
        if (k[2] == i and k[1] == j) or (k[1] == i and k[2] == j):
            r = True
            break
    return r


def encontrar_conjunto(i, conjunto):  # Função para encontrar o conjunto do vértice i
    for k in range(len(conjunto)):
        if i in conjunto[k]:
            return k


def kruskal(matriz_adjacencia):  # Função que recebe uma matriz de adjacência e retorna a matriz de adjacência da árvore geradora mínima
    arestas = []
    conjuntos = []
    arvore_geradora = criar_matriz(len(matriz_adjacencia), len(matriz_adjacencia), 0)

    for i in range(len(matriz_adjacencia)):
        lista = [i]
        conjuntos.append(lista)

    for i in range(len(matriz_adjacencia)):
        for j in range(len(matriz_adjacencia[i])):
            if matriz_adjacencia[i][j] != 0 and mesma_aresta(i, j, arestas) == False:
                t = (matriz_adjacencia[i][j], i, j)
                arestas.append(t)
    arestas.sort(key=lambda x: x[0])

    for cont in range(len(matriz_adjacencia)):
        i = encontrar_conjunto(arestas[cont][1], conjuntos)
        j = encontrar_conjunto(arestas[cont][2], conjuntos)
        if i != j:
            arvore_geradora[arestas[cont][1]][arestas[cont][2]] = arestas[cont][0]
            arvore_geradora[arestas[cont][2]][arestas[cont][1]] = arestas[cont][0]
            conjuntos[i] += conjuntos[j]
            conjuntos.remove(conjuntos[j])

    return arvore_geradora


matriz = criar_matriz_adjacencia("teste.txt")  # Criando a matriz de adjacência, aqui usamos um arquivo teste.txt
arvore_geradora = kruskal(matriz)  # Aqui pegamos a árvore geradora mínima

for linha in arvore_geradora:  # Printa o resultado na tela
    linha_resultado = ""
    for j in linha:
        linha_resultado += str(j)+","
    linha_resultado = linha_resultado[:-1]
    print(linha_resultado)



