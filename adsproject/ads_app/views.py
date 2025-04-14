from django.shortcuts import render
from django.views.generic import *

# Create your views here.
class BaseView(TemplateView):
    template_name = 'base.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class DisciplinasView(TemplateView):
    template_name = 'disciplinas.html'

class ExtensoesView(TemplateView):
    template_name = 'extensoes.html'

class NoticiasView(TemplateView):
    template_name = 'noticias.html'

class DocumentosView(TemplateView):
    template_name = 'documentos.html'

class ProjetosView(TemplateView):
    template_name = 'projetos.html'

class MonitoriasView(TemplateView):
    template_name = "monitorias.html"

