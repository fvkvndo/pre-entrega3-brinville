from django.urls import path
from control_brinville.views import listar_medicos

urlpatterns = [
    path("medicos/", listar_medicos)
]
