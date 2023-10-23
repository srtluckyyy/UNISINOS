def minha_funcao(par1, par2):
    print('\nParâmetros recebidos:')
    print('par1 =', par1)
    print('par2 =', par2)
    print()

if __name__ == '__main__':
    # Uma ou mais instruções antes da chamada da função
    minha_funcao(1, 2.2)
    minha_funcao(par2='B', par1='A')
    # Uma ou mais instruções após a chamada da função