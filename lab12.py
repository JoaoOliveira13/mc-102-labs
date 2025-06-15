###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - A Grande Caçada aos Tesouros Perdidos
# Nome: João Pedro Nogueira Oliveira
# RA: 278646
###################################################

# Leitura da entrada no formato especificado
M, N = map(int, input().split())
matriz = []
for _ in range(M):
    linha = input().strip().split()
    matriz.append(linha)
P = int(input())

# Lógica do código
def max_tesouros(mapa, M, N, P):
    if P % 2 == 1:
        P -= 1

    prefix_sum = [[0] * (N + 1) for _ in range(M + 1)]

    for i in range(M):
        for j in range(N):
            prefix_sum[i + 1][j + 1] = (
                prefix_sum[i][j + 1] +
                prefix_sum[i + 1][j] -
                prefix_sum[i][j] +
                (1 if mapa[i][j] == 'X' else 0)
            )

    def contar_x(x1, y1, x2, y2):
        return (
            prefix_sum[x2][y2]
            - prefix_sum[x1][y2]
            - prefix_sum[x2][y1]
            + prefix_sum[x1][y1]
        )

    max_tesouros = 0

    for altura in range(1, M + 1):
        for largura in range(1, N + 1):
            perimetro = 2 * (altura + largura)
            if perimetro > P:
                continue

            for i in range(M - altura + 1):
                for j in range(N - largura + 1):
                    x1, y1 = i, j
                    x2, y2 = i + altura, j + largura
                    quantidade_x = contar_x(x1, y1, x2, y2)
                    max_tesouros = max(max_tesouros, quantidade_x)

    return max_tesouros

# Impressão da saída
print(max_tesouros(matriz, M, N, P))
