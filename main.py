opcao = ""
tarefas = []

while opcao != "3":

    print("============================")
    print("GERENCIADOR DE TAREFAS")
    print("============================")
    print()
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
    print("Você escolheu a opção: " + opcao)

    if opcao == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for tarefa in tarefas:
                print(tarefa)
    elif opcao == "3":
        print("Encerrando o programa. Até logo!")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")