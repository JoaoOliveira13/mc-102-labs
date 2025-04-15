# Leitura dos parâmetros da batalha
hp_jinx = int(input())
hp_ekko = int(input())
atk_jinx = int(input())
atk_ekko = int(input())
regen_jinx = int(input())
regen_ekko = int(input())
crit_jinx = int(input())
crit_ekko = int(input())

# Váriaveis para regeneração da vida máxima
max_hp_jinx = hp_jinx
max_hp_ekko = hp_ekko

# Contadores de ataques para o crítico
crit_j = 0
crit_e = 0

# Lógica do programa
while hp_jinx > 0 and hp_ekko > 0:
    golpe = input()

    if golpe == "J":
        if crit_j == crit_jinx:
            hp_ekko -= atk_jinx * 2
            crit_j = 0
        else:
            hp_ekko -= atk_jinx
            crit_j += 1

        if hp_jinx != max_hp_jinx:
            hp_jinx += max_hp_jinx * (regen_jinx / 100)
            if hp_jinx > max_hp_jinx:
                hp_jinx = max_hp_jinx

    elif golpe == "E":
        if crit_e == crit_ekko:
            hp_jinx -= atk_ekko * 2
            crit_e = 0
        else:
            hp_jinx -= atk_ekko
            crit_e += 1

        if hp_ekko != max_hp_ekko:
            hp_ekko += max_hp_ekko * (regen_ekko / 100)
            if hp_ekko > max_hp_ekko:
                hp_ekko = max_hp_ekko

# Resultado
if hp_jinx <= 0:
    print('Ekko')
else:
    print('Jinx')
