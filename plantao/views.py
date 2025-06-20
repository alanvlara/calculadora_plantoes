from django.shortcuts import render, redirect
from .forms import PlantaoForm
from .models import Plantao


precos = {
    1: 130.00,
    2: 143.00,
    3: 150.00,
    4: 164.00,
    5: 130.00,
    6: 170.00
}

def registrar_plantao(request):
    if request.method == 'POST':
        form = PlantaoForm(request.POST)
        if form.is_valid():
            form.save()
            form = PlantaoForm()

    else:
        form = PlantaoForm()

    plantoes = Plantao.objects.all().order_by('-data')
    totais = {i: 0 for i in range(1, 7)}
    for p in plantoes:
        cat = p.categoria()
        horas = p.horas_trabalhadas()
        totais[cat] += horas

    valores_totais = {
        f'item_{cat}': totais[cat] * precos[cat]
        for cat in totais
    }

    total_geral = sum(valores_totais.values())

    context = {
        'form': form,
        'plantoes': plantoes,
        'valores_totais': valores_totais,
        'total_geral': total_geral,
    }

    return render(request, 'plantao/formulario.html', context)

# def exibir_dias_com_semana(dias_e_turnos_trabalhados):
#     dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    
#     for turno, data in dias_e_turnos_trabalhados.items():
#         data_formatada = data.strftime("%d/%m/%Y")
#         dia_semana = dias_semana[data.weekday()]
#         print(f"Dia {data_formatada} foi trabalhado no turno {turno} e era uma {dia_semana}.")