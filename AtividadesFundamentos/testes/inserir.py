def _extrato(txt):
    print('\n\n--------------------------------------------------',
        txt,
        '\n\n--------------------------------------------------')



valorFreteTotal = 0
vFSeguro = 1
valorFinal = 9

txt = '\n Frete | R$ ', valorFreteTotal, '\n Seguro | R$ ', vFSeguro, '\n\n--------------------------------------------------\n O valor total do transporte ficou R$', valorFinal,
_extrato(txt)