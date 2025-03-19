# Leitura da entrada:
k = int(input())
p = int(input()) 
x = int(input()) 
y = int(input()) 
z = int(input()) 

# Cálculos e comparação:
preco_A = float((k * p) * ((100-x) / 100))

quantidade_B = k % z
if quantidade_B == 0:
    preco_B = float((k / z) * (p * y))
else:
    preco_B = (k // z) * (p * y) + (p * quantidade_B)
    while preco_A < preco_B and k % z != 0: 
        k += 1
        conta_B = (k / z) * (p * y)
        if conta_B < preco_A: 
            preco_B = conta_B
            break
# Resultado:
if preco_A < preco_B:
    print(True)
else: 
		print(False)
