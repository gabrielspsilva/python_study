# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este
# link (em minutos)

tamanhoarquivo = float(input('informe o tamanho do arquivo em MB '))
velocidadeInternet = float(input('informe a velocidade em Segundos '))
calculoTempoSeg = tamanhoarquivo / (velocidadeInternet/8)
calculoTempoMin = calculoTempoSeg/60

print("Tempo de Download e segundos: ", calculoTempoSeg)
print("Tempo em Minutos: ", calculoTempoMin)
