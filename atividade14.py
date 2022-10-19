# João Papo-de-Pescador, homem de bem, comprou um microcomputador para
# controlar o rendimento  diário de seu trabalho. Toda vez que ele traz
# um peso de peixes maior que o estabelecido pelo  regulamento de pesca
# do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por
# quilo  excedente.
#
# João precisa que você faça um programa que leia a
# variável PESO (peso de peixes) e  calcule o excesso. Gravar na variável
# EXCESSO a quantidade de quilos além do LIMTE e na variável MULTA
# o valor da multa que João deverá pagar.
#
# Imprima os dados do programa com as mensagens  adequadas

peso = float(input('informe o peso do peixe: '))
limite = 50
excesso = peso - limite

if (peso > 50):
    multa = (peso-50)*4.00
else:
    multa = 0.00

print('Valor da multa: %0.2f ' % multa)
