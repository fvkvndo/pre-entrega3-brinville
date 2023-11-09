from django.shortcuts import render

# Create your views here.
def listar_medicos(request):
    contexto = {
        "medico":"", 
            "pacientes": [
                {"nombre":"", "apellido":"", "dni":""}
            ]
    }
    http_response = render(
        request=request,
        template_name='control_brinville/lista_medicos.html',
        context=contexto,
    )
    return http_response