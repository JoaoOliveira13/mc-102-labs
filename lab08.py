entrada_usuario = input()   
lista_acordes = []

for caractere in entrada_usuario:
    if caractere == "M" or caractere == "m":
        indice = entrada_usuario.index(caractere)
        lista_acordes.append(entrada_usuario[:indice + 1])
        entrada_usuario = entrada_usuario[indice + 1:]

# Dicionário de regras para remoção de acordes;
regras_remocao = {
    "A": ("G", "A", "G"),
    "B": ("C", "B", "A"),
    "C": ("D", "C", "B"),
    "D": ("E", "D", "C"),
    "E": ("F", "E", "D"),
    "F": ("G", "F", "E"),
    "G": ("A", "G", "F")
}

indice_atual = 0
while indice_atual < len(lista_acordes) - 1:
    acorde_atual = lista_acordes[indice_atual]
    proximo_acorde = lista_acordes[indice_atual + 1]

    nota_base = acorde_atual[0]
    if proximo_acorde.startswith(regras_remocao[nota_base]):
        lista_acordes.pop(indice_atual + 1)
    else:
        indice_atual += 1

# Saída formatada dos acordes resultantes;
print(' '.join(map(str, lista_acordes)))

