from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.
class BaseView(TemplateView):
    template_name = 'base.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class DisciplinasView(ListView):
    model = PostDisciplina
    template_name = 'disciplinas.html'
    context_object_name = 'disciplinas'
    ordering = ['periodo', 'nome_disciplina']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['periodos'] = range(1, 6)
        return context

class ExtensoesView(TemplateView):
    template_name = 'extensoes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extensoes_atuais'] = Extensao.objects.filter(tipo='Atual')
        context['extensoes_futuras'] = Extensao.objects.filter(tipo='Futura')
        return context

class NoticiasView(TemplateView):
    template_name = 'noticias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all()
        context['noticias'] = PostNoticia.objects.all().order_by('-data_publicacao')
        return context

class DocumentosView(TemplateView):
    template_name = 'documentos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Tenta pegar o documento fixo (exemplo: nome contendo 'matrícula')
        matricula_doc = Documentacao.objects.filter(nome_arquivo__icontains='matrícula').first()

        # Busca documentos do tipo 'Arquivo'
        documentos = Documentacao.objects.filter(tipo='Arquivo')
        if matricula_doc:
            # Exclui o documento fixo da lista para evitar duplicidade
            documentos = documentos.exclude(id=matricula_doc.id)

        context['eventos'] = Evento.objects.all()
        context['matricula_fixa'] = matricula_doc
        context['documentos_matricula'] = documentos
        return context


class ProjetosView(TemplateView):
    template_name = 'projetos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        return context

class MonitoriasView(TemplateView):
    template_name = "monitorias.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['monitorias'] = PostMonitoria.objects.all()
        return context


