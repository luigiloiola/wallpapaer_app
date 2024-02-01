
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='api_home')
    # Outras URLs do CRUD de usuário, se necessário
]
