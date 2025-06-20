from datetime import datetime


preco_hora_item_1 = 130.00
preco_hora_item_2 = 143.00
preco_hora_item_3 = 150.00
preco_hora_item_4 = 164.00
preco_hora_item_5 = 130.00
preco_hora_item_6 = 170.00

horas_item_1 = 0
horas_item_2 = 0
horas_item_3 = 0
horas_item_4 = 0
horas_item_5 = 0
horas_item_6 = 0

def obter_dias_trabalhados():
    dias_e_turnos_trabalhados = {}
    ano_atual = datetime.now().year

    while True:
        entrada_data = input("Digite o dia de trabalho com horario (dd/mm) ou 'fim' para encerrar: ").strip().lower()
        if entrada_data == 'fim':
            break
        entrada_turno = input("Digite o horario inicial e final no formato hora inicio - hora fim: ").strip().lower()
        try:
            data = datetime.strptime(f"{entrada_data}/{ano_atual}", "%d/%m/%Y")
            dias_e_turnos_trabalhados[entrada_turno] = data
        except ValueError:
            print("Formato inválido. Use o formato dd/mm.")
    
    return dias_e_turnos_trabalhados

# def exibir_dias_com_semana(dias_e_turnos_trabalhados):
#     dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    
#     for turno, data in dias_e_turnos_trabalhados.items():
#         data_formatada = data.strftime("%d/%m/%Y")
#         dia_semana = dias_semana[data.weekday()]
#         print(f"Dia {data_formatada} foi trabalhado no turno {turno} e era uma {dia_semana}.")

def verificar_dias_de_cada_item():
    global horas_item_1, horas_item_2, horas_item_3, horas_item_4, horas_item_5, horas_item_6
    for turno, data in dias_e_turnos_trabalhados.items():
        hora_inicio_str, hora_fim_str = turno.split('-')
        hora_inicio = int(hora_inicio_str.strip())
        hora_fim = int(hora_fim_str.strip())
        horas_trabalhadas = abs(hora_inicio - hora_fim)
        if data.weekday() < 5:
            if hora_inicio < 19:
                horas_item_1 += horas_trabalhadas
            else:
                horas_item_2 += horas_trabalhadas
        else:
            if hora_inicio < 19:
                horas_item_3 += horas_trabalhadas
            else:
                horas_item_4 += horas_trabalhadas

def calcular_valores_do_plantao():
    preco_total_item_1 = horas_item_1 * preco_hora_item_1  
    preco_total_item_2 = horas_item_2 * preco_hora_item_2     
    preco_total_item_3 = horas_item_3 * preco_hora_item_3      
    preco_total_item_4 = horas_item_4 * preco_hora_item_4      
    preco_total_item_5 = horas_item_5 * preco_hora_item_5      
    preco_total_item_6 = horas_item_6 * preco_hora_item_6
    preco_total = preco_total_item_1 + preco_total_item_2 + preco_total_item_3 + preco_total_item_4 + preco_total_item_5 + preco_total_item_6
    print('preco_total_item_1: ', preco_total_item_1)
    print('preco_total_item_2: ', preco_total_item_2)
    print('preco_total_item_3: ', preco_total_item_3)
    print('preco_total_item_4: ', preco_total_item_4)
    print('preco_total_item_5: ', preco_total_item_5)
    print('preco_total_item_6: ', preco_total_item_6)
    print('preco_total_plantoes: ', preco_total)


# Execução
dias_e_turnos_trabalhados = obter_dias_trabalhados()
verificar_dias_de_cada_item()
calcular_valores_do_plantao()
