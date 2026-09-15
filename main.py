receitas = 0
despesas = 0
saldo = 0
estado = True
descricao = ""

print("### Controle financeiro ###")

while estado == True:
    print("""
        1 - Registrar receita
        2 - Registrar despesa
        3 - Consultar saldo
        4 - Sair 
        """)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        descricao = input("Descrição: ")
        receitas += float(input("Valor:  "))
        print("Receita registrada com sucesso!")
    elif opcao == 2:
        descricao = input("Descrição: ")
        despesas += float(input("Valor:  "))
        print("Despesa registrada com sucesso!")
    elif opcao == 3:
        saldo = receitas - despesas
        print(f"Seu saldo é: {saldo}")
    elif opcao == 4:
        print("Obrigado por utilizar!")
        estado = False
    else:
        print("Opção inválida!")