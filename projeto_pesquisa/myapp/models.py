from django.db import models

class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)

class Professor(Pessoa):
    pass

    def criar_projeto(self, nome, inicio, fim, situacao, atividades_ids, relatorios_ids):
        projeto = Projeto(nome=nome, inicio=inicio, fim=fim, situacao=situacao, coordenador=self)
        # Adicionar atividades ao projeto
        atividades = Atividade.objects.filter(id__in=atividades_ids)
        projeto.atividades.set(atividades)

        # Adicionar relatórios ao projeto
        relatorios = Relatorio.objects.filter(id__in=relatorios_ids)
        projeto.relatorios.set(relatorios)

        projeto.save()  # Salvar o projeto no banco de dados

        return projeto

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

    def criar_atividade(self, descricao):
        atv = Atividade(descricao=descricao, situacao="A Fazer")
        atv.save()

        self.atividades.add(atv)
        self.save()

        return atv

class Reitor(Pessoa):
    pass
