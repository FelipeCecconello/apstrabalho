from django.shortcuts import render, get_object_or_404
from .models import Aluno, Professor, Atividade, Projeto, Reitor

def listar_usuarios(request):
    alunos = Aluno.objects.all()
    professores = Professor.objects.all()
    reitores = Reitor.objects.all()
    return render(request, 'listar_usuarios.html', {'alunos': alunos, 'professores': professores, 'reitores':reitores})

def adicionar_usuario(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        if tipo == 'aluno':
            Aluno.objects.create(cpf=cpf, nome=nome)
        elif tipo == 'professor':
            Professor.objects.create(cpf=cpf, nome=nome)
        elif tipo == 'reitor':
            Reitor.objects.create(cpf=cpf, nome=nome)
        return render(request, 'adicionar_usuario.html', {'success': True})
    return render(request, 'adicionar_usuario.html')

def criar_projeto(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        inicio = request.POST.get('inicio')
        fim = request.POST.get('fim')
        projeto = professor.criar_projeto(nome, inicio, fim)
        return render(request, 'projeto_criado.html', {'projeto': projeto})
    return render(request, 'criar_projeto.html')

def criar_atividade(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        atividade = projeto.criar_atividade(descricao)
        return render(request, 'atividade_criada.html', {'atividade': atividade})
    return render(request, 'criar_atividade.html', {'projeto': projeto})

def criar_relatorio(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        relatorio = projeto.criar_relatorio(descricao)
        return render(request, 'relatorio_criado.html', {'relatorio': relatorio})
    return render(request, 'criar_relatorio.html', {'projeto': projeto})

def executar_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    atividade.executar_atividade()
    return render(request, 'atividade_executada.html', {'atividade': atividade})

def finalizar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if projeto.verificar_conclusao():
        projeto.finalizar_projeto()
        return render(request, 'projeto_finalizado.html', {'projeto': projeto})
    else:
        return render(request, 'atividades_pendentes.html', {'projeto': projeto})