"""Tendo como dados de entrada a altura e o sexo de uma pessoa, construa
    um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        1. Para homens: (72.7*h) - 58
        2. Para mulheres: (62.1*h) - 44.7 (h = altura)
        3. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo
            do peso."""

sexo = input("Qual teu sexo? Masculino (M) ou Feminino (F)? ")
altura = float(input("Digite tua altura: "))

peso_ideal_m = (72.7 * altura) - 58
peso_ideal_f = (62.1 * altura) - 44.7

if sexo == "M":
    print("Teu peso ideal eh %.2f: " % peso_ideal_m)
elif sexo == "F":
    print("Teu peso ideal eh %.2f: " % peso_ideal_f)
else:
    print("Sexo invalido!")

# determinar se esta sobre peso ou nao F
if sexo == "F":
    if (peso_ideal_m > 18.5 and peso_ideal_m < 24.9):
        print("Peso Normal")
    elif (peso_ideal_m > 25 and peso_ideal_m < 29.9):
        print("Sobropeso")
    elif (peso_ideal_m > 30 and peso_ideal_m < 34.9):
        print("Obesidade grau I")
    elif (peso_ideal_m > 35 and peso_ideal_m < 40):
        print("Obesidade grau II")
    elif (peso_ideal_m > 40):
        print("Obesidade grau III")

# determinar se esta sobre peso ou naoM
if sexo == "M":
    if (peso_ideal_f > 18.5 and peso_ideal_f < 24.9):
        print("Peso Normal")
    elif (peso_ideal_f > 25 and peso_ideal_f < 29.9):
        print("Sobropeso")
    elif (peso_ideal_f > 30 and peso_ideal_f < 34.9):
        print("Obesidade grau I")
    elif (peso_ideal_f > 35 and peso_ideal_f < 40):
        print("Obesidade grau II")
    elif (peso_ideal_f > 40):
        print("Obesidade grau III")