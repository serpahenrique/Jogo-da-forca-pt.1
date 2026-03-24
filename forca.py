import sys

palavras = []
dicas = []

def Incluir_Palavra():
    palavra = input("Digite uma palavra: ")
    dica = input("Digite uma dica: ")
    palavras.append(palavra)
    dicas.append(dica)
    print("Palavra adicionada!")

def Listar_Palavras():
    for i in range(len(palavras)):
        print(f"{i+1} - {palavras[i]} - {dicas[i]}")

def Alterar_Dica():
    i = int(input("Número da palavra: ")) - 1
    nova_dica = input("Nova dica: ")
    dicas[i] = nova_dica
    print("Dica alterada!")

def Excluir_Palavra():
    i = int(input("Número da palavra: ")) - 1
    palavras.pop(i)
    dicas.pop(i)
    print("Excluído!")

def Finalizar_Jogo():
    print("Jogo finalizado!")
    sys.exit()

def menu():
    while True:
        print("\n-------- MENU CRUD ---------")
        print("1. Incluir Palavra")
        print("2. Listar Palavras")
        print("3. Alterar Dica")
        print("4. Excluir Palavra")
        print("5. Sair")

        opcao = input("Escolha: ")

        if opcao == '1':
            Incluir_Palavra()
        elif opcao == '2':
            Listar_Palavras()
        elif opcao == '3':
            Alterar_Dica()
        elif opcao == '4':
            Excluir_Palavra()
        elif opcao == '5':
            Finalizar_Jogo()
        else:
            print("Opção inválida")

menu()