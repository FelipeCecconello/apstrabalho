from django.db import models

class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)

class Professor(Pessoa):
    pass

class Aluno(Pessoa):
    pass

class Atividade(models.Model):
    descricao = models.TextField()
    situacao = models.CharField(max_length=20)

class Relatorio(models.Model):
    descricao = models.TextField()

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    inicio = models.DateField()
    fim = models.DateField()
    situacao = models.CharField(max_length=100)
    coordenador = models.ForeignKey(Professor, on_delete=models.CASCADE)
    atividades = models.ManyToManyField(Atividade)
    relatorios = models.ManyToManyField(Relatorio)

class Reitor(Pessoa):
    pass
