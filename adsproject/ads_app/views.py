from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.
class BaseView(TemplateView):
    template_name = 'base.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class DisciplinasView(TemplateView):
    model = PostDisciplina
    template_name = 'disciplinas.html'
    context_object_name = 'disciplinas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disciplinas'] = PostDisciplina.objects.all()
        return context

class ExtensoesView(TemplateView):
    template_name = 'extensoes.html'

class NoticiasView(TemplateView):
    template_name = 'noticias.html'

class DocumentosView(TemplateView):
    template_name = 'documentos.html'

class ProjetosView(TemplateView):
    template_name = 'projetos.html'

