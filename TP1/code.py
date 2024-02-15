import sys

#Variáveis de inicialização

data = []
modalDif = []
faixasEt = {}
apto = 0
inapto = 0

#Parsing

lines = sys.stdin.readlines()

header = lines[0].strip().split(',')

indModal = header.index('modalidade')
indIdade = header.index('idade')
indResultado = header.index('resultado')

for line in lines[1:]:
    data.append(line.strip().split(','))

for line in data:

    #Contagem de atletas aptos

    resultado = line[indResultado]
    if (resultado == 'true'): apto += 1 
    else: inapto += 1

    #Idades e faixas etárias:

    idade = int(line[indIdade])
    faixa = (idade // 5) * 5
    faixaEt = f'{faixa}-{faixa + 4}'

    if faixaEt not in faixasEt:
        faixasEt[faixaEt] = 1
    else: faixasEt[faixaEt] +=1

    #Listagem das modalidades

    modal = line[indModal]
    if modal not in modalDif:
        (modalDif.append(modal))

aptoPercent = (apto / (apto + inapto)) * 100
inaptoPercent = (inapto / (apto + inapto)) * 100
sortedModal = sorted (modalDif)

print(f"Modalidades praticadas: {sortedModal}")
print(f"Percentagem de atletas aptos: {aptoPercent}%")
print(f"Percentagem de atletas inaptos: {inaptoPercent}%")
print(f"Distribuição por escalão de idades: {faixasEt}")