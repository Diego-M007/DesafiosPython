estoque = {
    
}

def Menu():
    print("=================")
    print("Opções")
    print("1- Ver estoque completo")
    print("2- Adicionar produto")
    print("3- Remover Produto")
    print("4- Sair do sistema")
    print("=================")

def Ver_Estoque():
    print("=================")
    print("Aqui está o estoque completo:")
    print(estoque)
    print("=================")

def Adicionar_Produtos():
    estoque[input("Digite o nome do produto: ")] = int(input("Digite a Quantidade do produto: "))
    print("Aqui está a lista de produtos atualizada:")
    print("=================")
    print(estoque)
    print("=================")

def Remover_Produtos():
    item_para_remover = input("Digite o nome do item a ser removido: ")
    
    if item_para_remover in estoque:
        estoque.pop(item_para_remover)
    else:
        print("Digite um produto existente")
        print("Aqui está a lista de todos os produtos existentes")
        for produtos in estoque:
            print(produtos)    



while True:
    Menu()
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        Ver_Estoque()
    elif opcao == 2:
        Adicionar_Produtos()
    elif opcao == 3:
        Remover_Produtos()
    elif opcao == 4:
        print("Obrigado por usar o sistema")
        break
    else:
        print("================")
        print("Digite uma opção válida")
        print("================")