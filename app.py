from metodos import alunos

def main():
    while True:
        print('\n### Sistema de Avaliação ###')
        print('1. Cadastrar Aluno')
        print('2. Cadastrar Jurado')
        print('3. Dar Notas')
        print('4. Mostrar Notas')
        print('5. Sair')
        
        opcao = input('Digite a opção desejada: ')
        
        if opcao == '1':
            alunos()
        # elif opcao == '2':
        #     listar_alunos()
        