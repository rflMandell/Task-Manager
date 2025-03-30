from models import *


def menu():
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            adicionar_tarefa(descricao)
        elif opcao == "2":
            for tarefa in listar_tarefas():
                print(tarefa)
        elif opcao == "3":
            tarefa_id = int(input("ID da tarefa a concluir: "))
            concluir_tarefa(tarefa_id)
        elif opcao == "4":
            tarefa_id = int(input("ID da tarefa a remover: "))
            remover_tarefa(tarefa_id)
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")