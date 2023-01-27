from django.shortcuts import render
from visitantes.models import Visitante

def index(request):

    todos_visitantes = Visitante.objects.all()

    context = {
        "nome_pagina": "Dashboard Inicial",
        "todos_visitantes": todos_visitantes,
    }

    return render(request, "index.html", context)

