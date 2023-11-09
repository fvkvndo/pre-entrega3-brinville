from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo = "Hola"
    respuesta_http = HttpResponse(saludo)
    return HttpResponse

def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"{hoy.day} {hoy.month}"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludar_con_html(request):
    contexto = {
        "lugar":"Hospital 2",
    }
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response