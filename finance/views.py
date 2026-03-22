from django.shortcuts import render
from .service import get_bitcoin_price

def home(request):
    preco = get_bitcoin_price()
    return render(request, 'finance/home.html', {'price': preco})





