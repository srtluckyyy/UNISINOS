import os
import sisInterface

def cadastroUsuário():
    listLog = sisInterface.login('cadastro')
    login = listLog[0]
    senha = listLog[1]

    with open('login.txt', 'a') as loginfile:
        loginfile.write(f'\n{login}')

    with open('senha.txt', 'a') as senhafile:
        senhafile.write(f'\n{senha}')


def loginUsuario():
    while True:
        os.system('cls' if os.name == 'nt' else 'clean')
        
        listLog = sisInterface.login()
        nameLogin = listLog[0]
        senhaLogin = listLog[1]

        with open('login.txt', 'a+') as loginfile:
            login = loginfile.readlines()

            for linha in login:
                if nameLogin in linha: 
                    with open('senha.txt', 'a+') as senhafile:
                        senha = senhafile.readlines(linha)
                        
                        if senha == senhaLogin:
                            main()

                        else: 
                            print('\nSenha incorreta.')
                            sisInterface.mensage(0)
                            break

            print('\nUsuário não encontrado. Cadastre-se primeiro.')
            sisInterface.mensage(0)
            return


def main():
    os.system('cls' if os.name == 'nt' else 'clean')

    print('\nVocê logou com sucesso!')
    input('\nInfelizmente não há nada aqui. Aperte ENTER para sair...')
    sisInterface.mensage(2)