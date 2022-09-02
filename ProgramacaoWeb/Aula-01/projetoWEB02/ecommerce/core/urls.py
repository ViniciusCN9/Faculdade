from django.urls import path
from .views import home, produtos, fornecedores, sobre, login, registrar

urlpatterns = [
    path('login/', login, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('home/', home, name='home'),
    path('produtos/', produtos, name='produtos' ),
    path('fornecedores/', fornecedores, name='fornecedores' ),
    path('sobre/', sobre, name='sobre' )
]