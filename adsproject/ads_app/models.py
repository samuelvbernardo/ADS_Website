from django.db import models

# Create your models here.


class PostDisciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome_professor = models.CharField(max_length=100)
    nome_disciplina = models.CharField(max_length=100)
    img_professor = models.FileField(upload_to='professores/')
    periodo = models.IntegerField()

    def __str__(self):
        return self.nome_professor + ' - ' + self.nome_disciplina
    