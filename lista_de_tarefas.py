def adicionar_tarefas(tarefas):

    descricao = input("Qual tarefa deseja adicionar? ").lower().strip()
    
    while True:
        prioridade = input("Qual a prioridade da tarefa? (baixa/media/alta) ").lower().strip()
        
        if prioridade == "baixa" or prioridade == "media" or prioridade == "alta":
            break
        else:  
            print("Prioridade inválida.")
    
    while True:
        status = input("Está pendente ou concluida? ").lower().strip()
    
        if status == "concluida":
            status = "[x]"
            break
        elif status == "pendente":
            status = "[ ]"
            break
        else:
            print("Comando inválido.")
    
    tarefa = {
        "descricao": descricao,
        "prioridade": prioridade,
        "status": status
    }
    
    tarefas.append(tarefa)
    print("Tarefa adicionada.")


def listar_tarefas(tarefas):
    
    if len(tarefas) == 0:
        print("Nenhuma tarefa foi adicionada.")
        return
        
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(i, "-", tarefa["status"], "-", tarefa["descricao"], "(", tarefa["prioridade"], ")")


def concluir_tarefa(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa foi adicionada.")
        return
    
    print("\nTarefas atuais:")
    listar_tarefas(tarefas)
    
    opcao = input("\nDigite 1 para concluir, ou 2 para marcar como pendente: ").strip()

    if opcao != "1" and opcao != "2":
        print("Opção inválida.")
        return
    
    numero = int(input("Qual número da tarefa deseja alterar? "))

    if numero < 1 or numero > len(tarefas):
        print("Número inválido.")
        return

    indice = numero - 1

    if opcao == "1":
        if tarefas[indice]["status"] == "[x]":
            print("A tarefa já foi concluída.")
        else:
            tarefas[indice]["status"] = "[x]"
            print("Tarefa concluída com sucesso!")
    
    elif opcao == "2":
        if tarefas[indice]["status"] == "[ ]":
            print("A tarefa já está marcada como pendente.")
        else:
            tarefas[indice]["status"] = "[ ]"
            print("Tarefa marcada como pendente.")


def remover_tarefa(tarefas):
        
    if len(tarefas) == 0:
        print("Nenhuma tarefa foi adicionada.")
        return
    
    print("\nTarefas atuais:")
    listar_tarefas(tarefas)
    
    remover = int(input("Qual tarefa deseja remover? "))
    
    if remover < 1 or remover > len(tarefas):
        print("Número inválido.")
        return

    indice = remover - 1
    
    tarefas.pop(indice)
    print("Tarefa removida com sucesso.")


def mostrar_pendentes_concluidas(tarefas):
    
    if len(tarefas) == 0:
        print("Nenhuma tarefa foi adicionada.")
        return
    
    encontrou = False
    
    pend_conc = input("1 - Mostrar apenas as pendentes / 2 - Mostrar apenas as concluídas: ")
    
    if pend_conc == "1":
        for tarefa in tarefas:
            if tarefa["status"] == "[ ]":
                print(tarefa["status"], "-", tarefa["descricao"], "(", tarefa["prioridade"], ")")
                encontrou = True
            
        if not encontrou:
            print("Nenhuma tarefa pendente.")    
                
    elif pend_conc == "2":
        for tarefa in tarefas:
            if tarefa["status"] == "[x]":
                print(tarefa["status"], "-", tarefa["descricao"], "(", tarefa["prioridade"], ")")
                encontrou = True
                
        if not encontrou:
            print("Nenhuma tarefa concluída.")          
                
    else:
        print("Opção inválida.")


def ordenar_por_prioridade(tarefas):
    
    if len(tarefas) == 0:
        print("Nenhuma tarefa foi adicionada.")
        return
    
    ordenar = input("Ordenar por: 1 - Maior prioridade / 2 - Menor prioridade: ").strip()
    
    if ordenar != "1" and ordenar != "2":
        print("Opção inválida.")
        return
    
    valores = {
        "baixa": 1,
        "media": 2,
        "alta": 3
    }
    
    tarefas_ordenadas = tarefas.copy()
    
    if ordenar == "1":
        tarefas_ordenadas.sort(key=lambda tarefa: valores[tarefa["prioridade"]], reverse=True)
    else:
        tarefas_ordenadas.sort(key=lambda tarefa: valores[tarefa["prioridade"]])
        
    print("\nTarefas ordenadas por prioridade:")
    for tarefa in tarefas_ordenadas:
        print(tarefa["status"], "-", tarefa["descricao"], "(", tarefa["prioridade"], ")")


#------------- Menu -------------

tarefas = []

while True:
    
    print("\n----- Menu -----")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Concluir Tarefa ou marcar como pendente")
    print("4 - Remover Tarefa")
    print("5 - Mostrar apenas pendentes ou concluídas")
    print("6 - Ordenar por prioridade")
    print("0 - Sair")
    opcao = input("Digite uma opção: ")
    
    if opcao == "1":
        adicionar_tarefas(tarefas)
        
    elif opcao == "2":
        listar_tarefas(tarefas)
        
    elif opcao == "3":
        concluir_tarefa(tarefas)
        
    elif opcao == "4":
        remover_tarefa(tarefas)
        
    elif opcao == "5":
        mostrar_pendentes_concluidas(tarefas)
        
    elif opcao == "6":
        ordenar_por_prioridade(tarefas)
    
    elif opcao == "0":
        print("Encerrando...")
        break
    
    else: 
        print("Comando inválido.")
