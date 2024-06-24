from metodos.alunos import Aluno

class SistemaDeAvaliacao:
    def __init__(self):
        self.alunos = {}
        self.jurados = set()

    def cadastrar_aluno(self, nome, categoria):
        if nome not in self.alunos:
            self.alunos[nome] = Aluno(nome, categoria)
            print(f"Aluno {nome} cadastrado com sucesso!")
        else:
            print(f"Aluno {nome} já está cadastrado.")

    def cadastrar_jurado(self, nome):
        if nome not in self.jurados:
            self.jurados.add(nome)
            print(f"Jurado {nome} cadastrado com sucesso!")
        else:
            print(f"Jurado {nome} já está cadastrado.")

    def avaliar_aluno(self, nome_aluno, notas, nome_jurado):
        if nome_aluno in self.alunos and nome_jurado in self.jurados:
            self.alunos[nome_aluno].adicionar_notas(notas, nome_jurado)
        else:
            if nome_aluno not in self.alunos:
                print(f"Aluno {nome_aluno} não encontrado.")
            if nome_jurado not in self.jurados:
                print(f"Jurado {nome_jurado} não encontrado.")

    def mostrar_resultados(self):
        for aluno in self.alunos.values():
            print(aluno)