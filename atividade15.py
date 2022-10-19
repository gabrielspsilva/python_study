# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados
# 11% para o Imposto de Renda,
# 8% para o INSS e
# 5% para o sindicato,
#
# Faça um  programa que nos dê:
# 1-salário bruto
# 2-quanto pagou ao INSS.
# 3-quanto pagou ao sindicato.
# 4-o salário líquido.

salarioporhora = float(input('Informe o valor hora: '))
numerohoras = int(input('Numero de horas trabalhado: '))
salariobruto = salarioporhora * numerohoras

inss = salariobruto * 0.08
sindicato = salariobruto * 0.11
salarioliquido = salariobruto - inss - sindicato

print('+ Salario Bruto: %0.2f ' % salariobruto)
print('- Sindicato %0.2f ' % sindicato)
print('- Inss %0.2f ' % inss)
print('= Salario Liquido %0.2f ' % salarioliquido)
