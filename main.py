tipos_movimentacao = ("receita", "despesa")
movimentacoes = []


def adicionar_movimentacao(tipo, descricao, valor):

    if tipo in tipos_movimentacao and valor > 0 :
        movimentacao = {
            "tipo" : tipo,
            "descricao" : descricao,
            "valor" : valor
        }
        movimentacoes.append(movimentacao)
  
    elif tipo not in tipos_movimentacao:
        print("Tipo de movimentação inválido")
    else:
        print("Valor não permitido.")
    

while True:
    print("""
        ===========================
            CONTROLE FINANCEIRO
        ===========================
        """)

    print("""
        1 - Adicionar receita
        2 - Adicionar despesa
        3 - Listar movimentações
        4 - Consultar saldo
        5 - Sair
        """)

    opcao = input("Escolha uma opção: ")