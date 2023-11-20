import os

def mensage(num = 0):
    if num == 0:
        input('\nAperte ENTER para continuar...')

    elif num == 1:
        print('\nInput não reconhecido, tente novamente!')
        input('\nAperte ENTER para continuar...')

    elif num == 2:
        os._exit(os.EX_OK)


def _linha(num = 40):
    linha = print('-' * num)
    return linha


def titulo(txt, num = 40):
    _linha(num)
    print(txt.center(num))
    _linha(num)


def opcoes(opc: list, num = 40):
    _linha(num)
    for i in range(len(opc)):
        print(f'{i + 1} - {opc[i]}')
    _linha(num)

    resposta = input()
    return resposta


def login(opc = 'login',num = 40):
    vetLog = []
    
    if opc == 'login':
        _linha(num)
        log = input('Login: ')
        senha = input('Senha: ')
        _linha(num)

        vetLog.append(log)
        vetLog.append(senha)

    elif opc == 'cadastro':
        while True:
            os.system('cls' if os.name == 'nt' else 'clean')

            _linha(num)
            log = input('Login: ')
            senha = input('Senha: ')
            confSenha = input('Confirme sua senha: ')
            _linha(num)

            if senha == confSenha: 
                vetLog.append(log)
                vetLog.append(senha)
                break
            else: 
                print('\nAs senhas não correspondem.')
                mensage(0)

    return vetLog
