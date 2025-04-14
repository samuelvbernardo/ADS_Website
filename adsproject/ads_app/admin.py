from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(PostDisciplina)
class PostDisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_disciplina','nome_professor', 'periodo')
    list_filter = ('nome_disciplina', 'nome_professor', 'periodo')