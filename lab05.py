# Leitura das especificações do cliente
K = int(input())
tem_ar = input()    
tem_dir_hid = input()
quant_cil_li, quant_cil_ls = map(int,input().split())
tem_vid_el = input()
cap_mal_li, cap_mal_ls = map(int,input().split())
tem_camb_auto = input()
quant_cav_li, quant_cav_ls = map(int,input().split())
quant_gar_li, quant_gar_ls = map(int,input().split())
tem_abs = input()
quant_lug_li, quant_lug_ls = map(int,input().split())
numero_de_modelos = int(input()) 

modelos = []

# Base de dados dos modelos;
for x in range(numero_de_modelos): 
    nome_do_modelo = input() 
    modelo = { # modelo["nome"] -> nome do carro
        "nome": nome_do_modelo,
        "tem_ar": input(),
        "tem_dir_hid": input(),
        "qtd_cil": int(input()),
        "tem_vid_el": input(),
        "capacidade_porta": int(input()),
        "tem_camb_aut": input(),
        "qtd_cav_li": int(input()),
        "quant_gar": int(input()),
        "tem_abs": input(),
        "qtd_lugares": int(input())
    }
    modelos.append(modelo)

print("Modelos selecionados:")

for modelo in modelos:
    count = 0
    if tem_ar == "I" or tem_ar == modelo["tem_ar"]:
        count += 1
    if tem_dir_hid == "I" or tem_dir_hid == modelo["tem_dir_hid"]:
        count += 1
    if tem_vid_el == "I" or tem_vid_el == modelo["tem_vid_el"]:
        count += 1
    if tem_camb_auto == "I" or tem_camb_auto == modelo["tem_camb_aut"]:
        count += 1
    if tem_abs == "I" or tem_abs == modelo["tem_abs"]:
        count += 1

    if quant_cil_li <= modelo["qtd_cil"] <= quant_cil_ls:
        count += 1
    if cap_mal_li <= modelo["capacidade_porta"] <= cap_mal_ls:
        count += 1
    if quant_cav_li <= modelo["qtd_cav_li"] <= quant_cav_ls:
        count += 1
    if quant_gar_li <= modelo["quant_gar"] <= quant_gar_ls:
        count += 1
    if quant_lug_li <= modelo["qtd_lugares"] <= quant_lug_ls:
        count += 1

    if count >= K:
        print(modelo["nome"])  
