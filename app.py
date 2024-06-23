from metodos.avaliacao import SistemaDeAvaliacao


def main():
    sistema = SistemaDeAvaliacao()

    while True:
        print("\nMenu:")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Jurado")
        print("3. Avaliar Aluno")
        print("4. Mostrar Resultados")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do Aluno: ")
            categoria = input("Categoria (Miss/Mister): ")
            sistema.cadastrar_aluno(nome, categoria)
        elif escolha == '2':
            nome = input("Nome do Jurado: ")
            sistema.cadastrar_jurado(nome)
        elif escolha == '3':
            nome_aluno = input("Nome do Aluno: ")
            criterio = input("Critério (Elegância, Desenvoltura, Simpatia, Item Reciclável): ")
            nota = float(input("Nota: "))
            nome_jurado = input("Nome do Jurado: ")
            sistema.avaliar_aluno(nome_aluno, criterio, nota, nome_jurado)
        elif escolha == '4':
            sistema.mostrar_resultados()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()