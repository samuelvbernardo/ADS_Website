from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('documentos/', DocumentosView.as_view(), name='documentos'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('noticias/', NoticiasView.as_view(), name='noticias'),
    path('projetos/', ProjetosView.as_view(), name='projetos'),
    path('extensoes/', ExtensoesView.as_view(), name='extensoes'),
    path('monitorias/', MonitoriasView.as_view(), name='monitorias'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
