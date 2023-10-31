'''
4.Faça um programa que solicite ao usuário informar uma hora, minuto e segundo no
formato “hh:mm:ss”. Crie uma função chamada “horaParaFloat” que recebe esses 3
parâmetros separadamente. Essa função deverá retornar um número float
representando as horas, minutos e segundos como um número fracionário. Ex:
“01:15:30” = 1,2583 ou “13:20:15” = 13,3375. Imprima o número fracionário a partir
do “main”;

'''

def _horaParaFloat(hora, minuto, segundo):
    pass


if __name__ == '__main__':
    print('Informe a hora atual(hh:mm:ss): \n')

    h = input()
    vetorHorario = []
    i = 0

    for n in range(0, len(h), 3):
        vetorHorario.append(h[i:n + 1])
        i += 3
        
    print(vetorHorario)
    
    pass