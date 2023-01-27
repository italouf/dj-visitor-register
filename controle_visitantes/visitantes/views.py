from django.shortcuts import render
from visitantes.forms import VisitanteForm

def registrar_visitante(request):
    
    form = VisitanteForm()

    context = {
        "nome_pagina": "Registrar Visitante",
        "form": form,
    }

    return render(request, "registrar_visitante.html", context)
