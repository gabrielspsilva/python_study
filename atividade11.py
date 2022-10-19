# Faça um Programa que peça 
# - 2 números inteiros e 
# - 1 número real.
#
# Calcule e Exiba: 
# 1-Produto do 
# 2-Dobro do primeiro 
# 3-Com metade do segundo 
# 4-A soma do 
# 5-Triplo do primeiro mais o terceiro.
# 6-Com o terceiro elevado ao cubo

numero1 = int(input("informe um numero inteiro: "))
numero2 = int(input("informe um numero inteiro: "))
numero3 = float(input("informe um numero float: "))

calculo1 = (numero1*2) * (numero2/2)
calculo2 = (numero1 + pow(numero3, 3))*3

print('Resultado1: ', calculo1)
print('Resultado2: ', calculo2)
