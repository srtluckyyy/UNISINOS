import math

print("___1. Implemente um programa que solicita dois números ao usuário e exibe na tela: ")
print("----")

a = float(input("Informe um número qualquer: "))
b = float(input("Informe outro número: "))

print("------------------------------------")
print("___a) A soma destes dois números")
print("A soma desses números é: ", a + b)

print("------------------------------------")
print("___b) A subtração destes dois números")
print("A subtração dos números é: ", a - b)

print("------------------------------------")
print("___c) A multiplicação destes dois números")
print("O produto desses números é: ", a * b)

print("------------------------------------")
print("___d) A divisão destes dois números")
print("A divisão desses números é: ", a / b)

print("------------------------------------")
print("___e) A divisão inteira destes dois números")
print("A divisão inteira desses números é: ", a // b)

print("------------------------------------")
print("___f) O resto da divisão inteira destes dois números")
print("O resto da divisão desses números é: ", a % b)

print("------------------------------------")
print("___g) A exponenciação destes dois números")
print("A exponenciação desses números é: ", a ** b)

print("------------------------------------")
print("___h) O maior destes dois números")
print("O maior número é: ", max(a, b))

print("------------------------------------")
print("___i) O menor destes dois números")
print("O menor número é: ", min(a, b))


print("------------------------------------")

print("2. Solicite um número ao usuário. Sendo este número uma temperatura em graus Celsius, faça um programa"
" que converte esta temperatura para graus Fahrenheit e exibe o resultado na tela. Fahrenheit = Celsius * 1.8"
" + 32")

print("----")
c = float(input("Agora, digite a temperatura atual: "))
print("A temperatura atual em Fahrenheit é: ", c * 1.8 + 32)


print("------------------------------------")

print("3. Solicite um número ao usuário. Sendo este número uma temperatura em graus Fahrenheit, faça um"
" programa que converte esta temperatura em graus Celsius e exibe o resultado na tela. Celsius ="
" (Fahrenheit - 32) / 1.8")

print("----")
f = float(input("Digite a temperatura atual em Fahrenheit: "))
print("Essa temperatura em graus Celsius é: ", (f - 32) / 1.8)


print("------------------------------------")

print("4. Implemente um programa que solicita um número ao usuário. Sendo este número uma velocidade em"
" km/h, faça um programa para converter esta velocidade em m/s e exiba o resultado na tela.")

print("----")
v = float(input("Digite uma velocidade em km/h: "))
print("Essa velocidade em m/s é: ", v / 3.6)

print("------------------------------------")

print("5. Implemente um programa que solicita ao usuário o preço de um calçado e o percentual de desconto. Em"
" seguida, calcule o valor do desconto e o valor final a ser pago pelo calçado.")

print("----")
precoCalcado = float(input("Digite o preço de um calçado: "))
pDesconto = float(input("Digite o percentual de desconto: "))
pFinal = precoCalcado - (precoCalcado * (pDesconto / 100))

print("O valor descontado é: ", precoCalcado * pDesconto / 100)
print("O valor do calçado com o desconto é: ", pFinal)

print("------------------------------------")

print("6. Desenvolva um programa que solicite ao usuário o raio de um círculo e exiba o diâmetro, circunferência e a"
" área deste círculo na tela")

print("----")
raioCirculo = float(input("Digite o número do raio de um circulo: "))
diametro = raioCirculo * 2
area = (raioCirculo ** 2) * 3.14

print("O diametro do circulo é: ", diametro)
print("E a area do circulo é: ", area)

print("------------------------------------")

print("7. Desenvolva um programa que solicite ao usuário a altura e a largura de um retângulo e exiba o"
" perímetro e a área deste retângulo na tela")

print("----")
aRetangulo = float(input("Qual a altura do retângulo? "))
lRetangulo = float(input("Qual a largura do retângulo? "))

pRetangulo = aRetangulo + lRetangulo
aRetangulo = aRetangulo * lRetangulo

print("O perímetro e a área desse retângulo é, respectivamente: ", pRetangulo, ", ", aRetangulo)

print("------------------------------------")

print("8. Desenvolva um programa que solicite ao usuário a base e a altura de um triângulo e exiba o valor da"
" área deste triângulo na tela")

print("----")
aTriangulo = float(input("Digite a altura do triangulo: "))
bTriangulo = float(input("Digite a base do triângulo: "))

print("O valor da área desse triângulo é: ", (bTriangulo * aTriangulo) / 2)

print("------------------------------------")

print("9. Desenvolva um programa que solicite dois números ao usuário e que exiba o resultado do primeiro"
" número elevado ao segundo, ou seja, potência")

print("----")
baseE = float(input("Digite um número qualquer: "))
expoenteE = float(input("Digite outro número qualquer: "))

print("O primeiro número elevado ao segundo é: ", baseE ** expoenteE)


print("------------------------------------")


print("10.Desenvolva um programa que solicite dois números ao usuário. Estes números são os catetos de um"
" triângulo retângulo. Sendo assim, apresente ao usuário:")

print("----")

c1 = float(input("Digite um número que represente o cateto 1 de um triângulo retângulo: "))
c2 = float(input("Digite outro número para representar outro cateto: "))

print("------------------------------------")
print("___a) Hipotenusa")

h = math.sqrt(c1 ** 2 + c2 **2)
print("A Hipotenusa desse triângulo é: ", h)

print("------------------------------------")
print("___b)Perímetro")

print("O perímetro desse triângulo é: ", h + c1 + c2)

print("------------------------------------")
print("___c) Área")

print("A área desse triângulo é: ", (c1 * c2) / 2)

print("------------------------------------")
print("___d)Seno")

s = c1 / h
print("O seno do ângulo é: ", math.degrees(c1 / h))

print("------------------------------------")
print("___e)Cosseno")

print("O cosseno do ângulo é: ", math.degrees(c2 / h))

print("------------------------------------")
print("___f) Tangente")

print("A tangente do triângulo é: ", math.degrees(c1 / c2))