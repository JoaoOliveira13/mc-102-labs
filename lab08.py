seq_acordes = input().split()  # ou sua lista já pronta

i = 0
while i < len(seq_acordes) - 1:
    atual = seq_acordes[i]
    proximo = seq_acordes[i + 1]

    letra = atual[0]
    remover = {
        "A": ("G", "A", "G"),
        "B": ("C", "B", "A"),
        "C": ("D", "C", "B"),
        "D": ("E", "D", "C"),
        "E": ("F", "E", "D"),
        "F": ("G", "F", "E"),
        "G": ("A", "G", "F")
    }

    if letra in remover and proximo.startswith(remover[letra]):
        del seq_acordes[i + 1]
    else:
        i += 1

print(seq_acordes)
