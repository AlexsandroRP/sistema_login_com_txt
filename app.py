import os
import getpass



def menu():
    print("Bem-vindo a este sistema")
    print("Escolha uma opção")
    print("[1] - Fazer login")
    print("[2] - Cadastrar novo usuário")

def opcao_digitada():
      opcao = input("Digite uma das opções: ")
      return opcao  

def recebe_usuario_senha():
    nome = input("Digite um nome para usuário: ")
    senha = getpass.getpass("Digite uma senha para o usuário: ")
    return nome, senha

def cadastrar_usuario():
    while True:
        nome, senha = recebe_usuario_senha()    
        with open("usuarios.txt", 'r') as arquivo:
                for linha in arquivo:
                    if nome in linha:
                        print("Nome de usuário já cadastrado")
                        break

                if nome not in linha:
                    with open("usuarios.txt", 'a', newline='', encoding='utf-8') as arquivo:
                        arquivo.write(nome + ',' + senha + os.linesep)
                    print(f"Usuário {nome} cadastrado com sucesso!")
                    return False  

def autenticar_usuario():
    while True:
        usuario, senha = recebe_usuario_senha()
        login = usuario + ',' + senha + '\n'
        
        with open("usuarios.txt", 'r') as arquivo:
            for linha in arquivo:
                if linha == login:
                    print(f"Bem vindo {usuario}, login feito com sucesso!")
                    break
            if linha == login:
                return False
            else:
                print("Usuário ou senha incorreto")    
                    
                       
                        
# Main App
menu()
opcao = input("Digite uma das opções: ")
if opcao == '1':
    autenticar_usuario()
elif opcao == '2':
    cadastrar_usuario()
else:
    print("Opção inválida, tente novamente!")
     




