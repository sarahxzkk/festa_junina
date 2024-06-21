class Aluno:
    alunos = []

    def __init__(self, nome, turma, categoria):
        self._nome = nome
        self._categoria = categoria
        self._turma = turma
        self._notas = []

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._notas}'

    
    def cadastrar_aluno():
        nome = input('Nome do aluno: ')
        categoria = input('Categoria do aluno (Miss ou Mister): ')
        print(f'Aluno {nome} cadastrado com sucesso!')



Aluno.cadastrar_aluno()
# Aluno.listar_alunos()