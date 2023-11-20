'''
Criar um acesso de conta de usuário
    Deve conter:
        - Login
        - Senha
        - Cadastro
'''
import os
import sisDef, sisInterface

var = '7890'

with open('login.txt', 'a+') as logifile:
    logifile.write('123')
    log = logifile.read()
    print(log)

'''
while True:
    os.system('cls' if os.name == 'nt' else 'clean')
    
    resposta = sisInterface.opcoes(['Login', 'Cadastro', 'Sair'])

    if resposta == '1':
        sisDef.loginUsuario()

    elif resposta == '2':
        sisDef.cadastroUsuário()

    elif resposta == '3':
        sisInterface.mensage(2)

    else:
        sisInterface.mensage(1)'''