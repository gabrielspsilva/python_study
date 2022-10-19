"""
    Faça um programa para uma loja de tintas. O programa deverá pedir o
    Tamanho em Metros Quadrados da área a ser pintada. Considere que a
    cobertura da tinta é de 1 litro para cada 3 metros quadrados e
    que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

    Informe ao usuário a quantidades de latas de tinta a serem compradas
    e o preço total.
"""
import math

metroquadrado = float(input('informe o tamanho em metros: '))

quantidadeLitros = metroquadrado/3
quantidadeLatas = math.ceil(quantidadeLitros / 18)
precoTotal = quantidadeLatas * 80.00

print('Quantidade Latas %0.1f ' % quantidadeLatas)
print('Valor total %0.2f ' % precoTotal)
