from django.shortcuts import render, get_object_or_404
from .models import Aluno, Professor, Atividade, Projeto, Reitor, Pessoa

def listar_usuarios(request):
    alunos = Aluno.objects.all()
    professores = Professor.objects.all()
    reitores = Reitor.objects.all()
    return render(request, 'listar_usuarios.html', {'alunos': alunos, 'professores': professores, 'reitores':reitores})

def visualizar_usuario(request, usuario_id):
    usuario = Pessoa.objects.filter(id=usuario_id).first()
    # Verificar se é um reitor
    is_reitor = Reitor.objects.filter(id=usuario_id).exists()
    # Verificar se é um professor
    is_professor = Professor.objects.filter(id=usuario_id).exists()
    # Verificar se é um aluno
    is_aluno = Aluno.objects.filter(id=usuario_id).exists()
    # Exemplo de uso
    tipo = "Não Definido"
    if is_reitor:
        tipo = "Reitor"        
    elif is_professor:
        tipo = "Professor"
    elif is_aluno:
        tipo = "Aluno"

    return render(request, 'visualizar_usuario.html', { 'cpf': usuario.cpf, 'nome': usuario.nome, 'tipo': tipo, 'id': usuario.id })

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

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'listar_projetos.html', { 'projetos': projetos })

def visualizar_projeto(request, projeto_id):
    projeto = Projeto.objects.filter(id=projeto_id).first()
    atividades = projeto.atividades.all()
    
    return render(request, 'adicionar_projeto.html', { 'success': False, 'edit': True, 'projeto': projeto, 'professor': projeto.coordenador, 'atividades': atividades})


def criar_projeto(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    alunos = Aluno.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        inicio = request.POST.get('inicio')
        fim = request.POST.get('fim')
        situacao = 'Aguardando aprovação'
        aluno = request.POST.get('aluno')
        projeto = professor.criar_projeto(nome, inicio, fim, situacao, aluno)
        return render(request, 'adicionar_projeto.html', { 'success': True, 'edit': True, 'projeto': projeto, 'professor': projeto.coordenador})
    return render(request, 'adicionar_projeto.html', { 'success': False, 'edit': False, 'professor': professor, 'alunos': alunos})

def criar_atividade(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        projeto.criar_atividade(descricao)
        return visualizar_projeto(request, projeto_id)
    return render(request, 'adicionar_atividade.html', {'projeto': projeto})

def criar_relatorio(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        projeto.criar_relatorio(descricao)
        return visualizar_projeto(request, projeto_id)
    return render(request, 'adicionar_relatorio.html', {'projeto': projeto})

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