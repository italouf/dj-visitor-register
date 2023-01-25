from django.shortcuts import render

def index(request):

    context = {
        "nome_pagina": "Dashboard Inicial",
    }

    return render(request, "index.html", context)

