""""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 6 metros quadrados e que a tinta é vendida em

- latas de 18 litros, que custam R$ 80,00 ou
- em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:

+ comprar apenas latas de 18 litros;
+ comprar apenas galões de 3,6 litros;

plus usar inteligencia artificial para determinar a melhor opcao de compra
"""

import math

metroquadrado = float(input('Informe o tamanho da área da pintura em m2: '))

quantidadeLitros = metroquadrado/6

quantidadeLatas = math.ceil(quantidadeLitros / 18)
quantidadeGaloes = math.ceil(quantidadeLitros / 3.6)

precoTotalLatas = quantidadeLatas * 80.00
precoTotalGaloes = quantidadeGaloes * 25.00

print('Valor total Latas %0.2f ' % precoTotalLatas)
print('Valor total Galoes %0.2f ' % precoTotalGaloes)


def inteligenciaArtificial(x, y):

    if (x > y):
        print("Sugestao Comprar Latas de Tinta! Melhor Preco! ")
    else:
        print("Sugestao Comprar Galoes de Tinta! Melhor Preco! ")


inteligenciaArtificial(precoTotalLatas, precoTotalGaloes)
