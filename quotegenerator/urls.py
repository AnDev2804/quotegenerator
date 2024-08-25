from django.urls import path
from quotegeneratorapp import views  # Importa tus vistas aquí

urlpatterns = [
    path('', views.home, name='home'),  # Aquí puedes definir tu vista principal
]