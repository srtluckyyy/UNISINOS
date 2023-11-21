import os
import sisInterface

def cadastroUsuário():
    listLog = sisInterface.login('cadastro')
    login = listLog[0]
    senha = listLog[1]

    with open('login.txt', 'a') as loginfile:
        loginfile.write(f'{login}\n')
        loginfile.flush()

    with open('senha.txt', 'a') as senhafile:
        senhafile.write(f'{senha}\n')
        senhafile.flush()


def loginUsuario():
    while True:
        os.system('cls' if os.name == 'nt' else 'clean')
        senhaLogin = []

        listLog = sisInterface.login()
        nameLogin = listLog[0]
        senhaLogin.append(listLog[1])

        print(f'nameLogin {nameLogin}, senhaLogin {senhaLogin}')

        with open('login.txt', 'r') as loginfile:
            login = loginfile.readlines()
            
        print(f'lenLogin {len(login)}')
        print('arquivo aberto')

        if len(login) == 0: input('\nNão há usuários cadastrados.'); return

        for linha in range(len(login)):
            print(f'linha {linha}, login[linha] {login[linha]}')
            if nameLogin in login[linha]: 

                print(f'linha {linha}')

                with open('senha.txt', 'r') as senhafile:
                    print(senhafile.readlines(linha))
                    senha = senhafile.readlines(linha)

                print(f'senha {senha}, senhaLogin {senhaLogin}')
                        
                if senha == senhaLogin:
                    input('logado?')
                    main()

                else: 
                    print('\nSenha incorreta.')
                    sisInterface.mensage(0)
                    break          
        
        print('\nUsuário não encontrado. Cadastre-se primeiro.')
        sisInterface.mensage(0)
        return


def vetorLogs():
    pass #transformar o txt em vetor


def main():
    os.system('cls' if os.name == 'nt' else 'clean')

    print('\nVocê logou com sucesso!')
    input('\nInfelizmente não há nada aqui. Aperte ENTER para sair...')
    sisInterface.mensage(2)