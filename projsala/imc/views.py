from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index (request):
    return render(request,'index.html')
def meu_nome(request):
    return HttpResponse("<h1>Меня зовут cавио<h1/>")
def tabuada2(request):
    n = 2
    texto = ''
    for numero in range(1, 11):
        resultado = n*numero
        texto += f'<h1>{n} x {numero} ={resultado}</h1>'
    return HttpResponse(texto)

def mensagem(request):
    dicionario={'mensagem':'olá IMC - DEV WEB'}
    return JsonResponse(dicionario)

def calcular_imc(request):
    altura=float(request.GET.get("altura"))
    peso=float(request.GET.get("peso"))
    altura=altura/100.0
    imc=peso/(altura*altura)
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc < 24.9:
        classificacao = 'Peso normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade'
    contexto={
        'imc': f'{imc:.2f}',
        'classificacao': classificacao,
        'altura': altura,
        'peso': peso,
    }
    #response=f'Расчет ИМТ: {peso/(altura*altura):.2f}'
    return render(request,'resultado.html', context=contexto)