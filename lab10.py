# Importando numpy para facilitar e agilizar o script
import numpy as np

# Leitura de dados
tamanho = int(input())
valores = []
for _ in range(tamanho):
    elementos = list(map(int, input().split()))
    valores.extend(elementos)

grade = np.array(valores).reshape(tamanho, tamanho)

# Processamento de dados
def obter_submatrizes_3x3(grade_maior):
    limite = len(grade_maior)
    subgrades = []
    for linha in range(limite - 2):
        for coluna in range(limite - 2):
            bloco = [grade_maior[i][coluna:coluna+3] for i in range(linha, linha+3)]
            bloco = np.array(bloco)
            subgrades.append(bloco)
    return subgrades

subgrades_3x3 = obter_submatrizes_3x3(grade)
quantidade_magicos = 0

for bloco in subgrades_3x3:
    soma_referencia = np.sum(bloco[0])  # Soma da primeira linha

    linhas_validas = all(np.sum(bloco[i]) == soma_referencia for i in range(3))
    colunas_validas = all(np.sum(bloco[:, j]) == soma_referencia for j in range(3))
    diagonal_principal_valida = np.sum(np.diag(bloco)) == soma_referencia
    diagonal_secundaria_valida = np.sum(np.diag(np.fliplr(bloco))) == soma_referencia

    if linhas_validas and colunas_validas and diagonal_principal_valida and diagonal_secundaria_valida:
        quantidade_magicos += 1

# Saída de dados
print(f'Número de quadrados mágicos: {quantidade_magicos}')
