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


def prim(matriz_adjacencia): # Função que recebe uma matriz de adjacência e retorna a matriz de adjacência da árvore geradora mínima
    vertices = [0]
    coluna = 0
    linha = 0
    arvore_geradora = criar_matriz(len(matriz_adjacencia), len(matriz_adjacencia[0]), 0)

    for k in range(len(matriz_adjacencia)-1):
        menor = 0
        for i in vertices:
            for j in range(len(matriz_adjacencia[i])):
                if j not in vertices:
                    if menor == 0 and matriz_adjacencia[i][j] != 0:
                        menor = matriz_adjacencia[i][j]
                        linha = i
                        coluna = j
                    elif matriz_adjacencia[i][j] < menor and matriz_adjacencia[i][j] != 0:
                        menor = matriz_adjacencia[i][j]
                        linha = i
                        coluna = j

        arvore_geradora[linha][coluna] = menor
        arvore_geradora[coluna][linha] = menor
        vertices.append(coluna)
    return arvore_geradora


matriz = criar_matriz_adjacencia("teste.txt")  # Criando a matriz de adjacência, aqui usamos um arquivo teste.txt
arvore_geradora = prim(matriz)  # Aqui pegamos a árvore geradora mínima

for linha in arvore_geradora:  # Printa o resultado na tela
    linha_resultado = ""
    for j in linha:
        linha_resultado += str(j)+","
    linha_resultado = linha_resultado[:-1]
    print(linha_resultado)



