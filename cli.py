import database
import cli

def main():
    while True:
        print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Concluir tarefa\n4. Remover Tarefa\n5. Sair")
        opcao = input("Escolha uma opcao\n->")
        
        if opcao == "1":
            descricao = input("Descricao da tarefa")
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
            print("Opcao invalida!")
        