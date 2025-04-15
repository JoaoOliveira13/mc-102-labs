# Leitura dos parametros da batalha
vida_jinx = int(input())
vida_ekko = int(input())
dano_jinx = int(input())
dano_ekko = int(input())
vida_recuperada_jinx = int(input())
vida_recuperada_ekko = int(input())
qtd_crit_jinx = int(input())
qtd_crit_ekko = int(input())

# Calculo da vida de Jinx e Ekko
vida_max_jinx = vida_jinx
vida_max_ekko = vida_ekko

# Leitura da sequência de ataques e determinação do vencedor
count_j = 0
count_e = 0

while vida_jinx > 0 and vida_ekko > 0:
    ataque = str(input())

    if ataque == "J":
        if count_j == qtd_crit_jinx:
            vida_ekko -= dano_jinx * 2
            count_j = 0
        else: 
            vida_ekko -= dano_jinx
            count_j += 1
        
        # Essa equação é para determinar a qtd. de vida regenerada;
        if vida_jinx != vida_max_jinx:
            vida_jinx += vida_max_jinx * (vida_recuperada_jinx / 100)
            if vida_jinx > vida_max_jinx:
                vida_jinx = vida_max_jinx

    elif ataque == "E":
        if count_e == qtd_crit_ekko:
            vida_jinx -= dano_ekko * 2
            count_e = 0
        else: 
            vida_jinx -= dano_ekko
            count_e += 1
        
        if vida_ekko != vida_max_ekko:
            vida_ekko += vida_max_ekko * (vida_recuperada_ekko / 100)
            if vida_ekko > vida_max_ekko:
                vida_ekko = vida_max_ekko

if vida_jinx <= 0:
    print('Ekko')
else: print('Jinx')



