from django.urls import path
from .views import home, cadastrarescola, listarescola
app_name = "app"

urlpatterns = [
    path('', home, name='home'),
    path('cadastrarescola/', cadastrarescola, name='cadastrarescola'),
    path('listarescola/', listarescola, name='listarescola'),
]