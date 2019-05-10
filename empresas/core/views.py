from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests

def home(request):
    return render(request, 'index.html')


def consulta_cnpj(request):    
    if request.method == 'POST':
        url = 'http://www.transparencia.gov.br/api-de-dados/ceis?codigoSancionado='+request.POST['cnpj']
        url += '&pagina=1'
        response = requests.get(url)
        return render(request, 'index.html', {'result': response.json() })