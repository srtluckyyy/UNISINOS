'''
Peça para o usuário digitar uma frase contendo diversas palavras. 
Em seguida, peça para que ele informe uma única palavra. 
Caso a palavra não exista na frase, mostre um texto informando que a palavra não foi localizada. 
Caso essa palavra esteja na frase, mostre na tela a quantidade de vezes que ela aparece, remova todas as ocorrências da
palavra na frase e mostre a frase alterada na tela.
'''

'''Acabei por fazer dessa forma, não consegui resolver da forma 'simples'/'''

resposta = 1
fraseV = []
frase = ''
while resposta != 0:
    resposta = input('Digite palavras para o texto: (0 para sair): \n')
    if resposta == '0': break
    fraseV.append(resposta)
    frase += resposta

palavra = input('Informe uma palavra: ')

if palavra not in frase:
    print('\nA palavra não foi localizada.')

else: 
    print(f'\nA palavra escolhida aparece no texto {frase.count(palavra)} vezes.')
    for i in range(frase.count(palavra)): fraseV.remove(palavra)
    print(fraseV)

