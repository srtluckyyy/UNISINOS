print ("Atividade 1 - n1")

print ("Abrahão")
nome = input("escreva seu nome: ")
print (nome)

print ("----------------")
print ("Atividade 1 - n2")

idade = int(input('Qual sua idade, {}? '.format(nome)))
print (idade)

print ("----------------")
print ("Atividade 1 - n3")

altura = float(input("Digite sua altura: "))
print ("Sua altura é: {:.2f}".format(altura))

print ("----------------")
print ("Atividade 1 - n4")

um = 1
dez = 10
cem = 100
mil = 1000

print("{:<7} {:<7} {:<7} {:<7}".format(um, dez, cem, mil))
print("{:^7} {:^7} {:^7} {:^7}".format(um, dez, cem, mil))
print("{:>7} {:>7} {:>7} {:>7}".format(um, dez, cem, mil))

print ("----------------")
print ("Atividade 1 - n5")

diaNascimento = int(input("Qual o dia do seu nascimento? "))
print (diaNascimento)

print ("----------------")
print ("Atividade 1 - n6")

mesNascimento = int(input("Qual mês do seu nascimento? "))
print(mesNascimento)

print ("----------------")
print ("Atividade 1 - n7")

anoNascimento = input("Qual ano do seu nascimento? ")
print ('{}/{:02d}/{}'.format(diaNascimento, mesNascimento, anoNascimento))

print ("----------------")
print ("Atividade 1 - n8")

nFracionario = float(input("Digite um número fracionário qualquer: "))
print (int(nFracionario))
print ("{:.3f}".format(nFracionario))

print ("----------------")
print ("Atividade 1 - n9")

moeda = input("Informe um caractere que represente uma moeda: ")
valorMoeda = float(input("Informe um valor para essa moeda: "))
print ("+ {} + {:.2f}".format(moeda, valorMoeda))

