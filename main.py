opcao = ""
tarefas = []

def mostrar_menu():
    print("============================")
    print("GERENCIADOR DE TAREFAS")
    print("============================")
    print()
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Sair")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        for tarefa in tarefas:
            print(tarefa)

def editar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        for tarefa in tarefas:
            print(tarefa)
    indice = int(input("Digite o número da tarefa que deseja editar: "))
    novo_nome = input("Digite o novo nome da tarefa: ")
    tarefas[indice-1] = novo_nome    

while opcao != "4":
    mostrar_menu()

    opcao = input("Escolha uma opção: ")
    print("Você escolheu a opção: " + opcao)

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        editar_tarefas()
    elif opcao == "4":
        print("Encerrando o programa. Até logo!")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")