# Bloco dado pelo Susy;
agenda = [input().split() for _ in range(5)]
def print_agenda(agenda):
    print(' '.join([j.ljust(10) for j in ['Horário', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']]))
    horario = list(range(8, 19))
    for i in range(10):
        saida = [(str(horario[i]) + '-' + str(horario[i+1])).ljust(10)]
        saida = saida + [agenda[j][i].ljust(10) for j in range(5)]
        print(' '.join(saida))

# Mapeamento dos nomes dos dias para índices;
dias_da_semana = {'Segunda': 0, 'Terça': 1, 'Quarta': 2, 'Quinta': 3, 'Sexta': 4}

# Tratamento de dados;
qtd_modificacoes = int(input())

for _ in range(qtd_modificacoes):
    instrucao = input().split()

    if instrucao[0] == 'Remover':
        hora_inicial = int(instrucao[2])
        hora_final = int(instrucao[3])
        nome_dia = instrucao[1]
        indice_dia = dias_semana[nome_dia]
        for h_atual in range(hora_inicial, hora_final):
            indice_horario = h_atual - 8 # Índice 0 é as 08h;
            if 0 <= indice_horario < 10:
                agenda[indice_dia][indice_horario] = 'Livre'

    elif instrucao[0] == 'Adicionar':
        nome_atividade = instrucao[1]
        qtd_horas = int(instrucao[2])
        inserido = False # Atividade à ser inserida;

        for _ in range(5):
            # Lê toda os horários do dia;
            for h in range(0, 11 - qtd_horas):
                intervalo = agenda[d][h:h + qtd_horas]
                if all(t == 'Livre' for t in intervalo):
                    for k in range(h, h + qtd_horas):
                        agenda[d][k] = nome_atividade
                    inserido = True
                    break
            if inserido:
                break
        if not inserido: # Caso o loop não consiga colocar a atv. na agenda;
            print(f'Não foi possível alocar a atividade {nome_atividade}')

# Impressão final da agenda organizada;
print_agenda(agenda)
