from django.db import models

class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)

class Professor(Pessoa):
    pass

    def criar_projeto(self, nome, inicio, fim, situacao, aluno):
        aluno = Aluno.objects.get(cpf=aluno)
        projeto = Projeto(nome=nome, inicio=inicio, fim=fim, situacao=situacao, coordenador=self, aluno=aluno)
        projeto.save()  # Salvar o projeto no banco de dados

        return projeto

class Aluno(Pessoa):
    pass

class Atividade(models.Model):
    descricao = models.TextField()
    situacao = models.CharField(max_length=20)

    def executar(self):
        self.situacao="Feito"
        self.save()
        return self

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
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True)

    def criar_atividade(self, descricao):
        atv = Atividade(descricao=descricao, situacao="A Fazer")
        atv.save()
        self.atividades.add(atv)
        self.save()
        return atv
    
    def criar_relatorio(self, descricao):
        rlt = Relatorio(descricao=descricao)
        rlt.save()
        self.relatorios.add(rlt)
        self.save()
        return rlt

    def verificar_conclusao(self):
        """
            Retorna True caso o projeto satisfaz condições para ser concluído
        """
        for atv in self.atividades.all():
            if (atv.situacao == "A Fazer"):
                return False
        return True

    def finalizar_projeto(self):
        self.situacao = "Concluído"
        self.save()
        return self
        
    def aprovar_projeto(self):
        self.situacao = "Aprovado"
        self.save()
        return self

class Reitor(Pessoa):
    pass
