num_premios = int(input())

if num_premios < 1:
    exit()

premios = []

for n in range(num_premios):
    try:
        linha = input()
        linha = linha.split(" ")
        premios.append([int(linha[0]), linha[1]])
    except TypeError:
        exit()

qtd_sorteios = int(input())

forcas = [int(i) for i in input().split(" ")]

if min(forcas) <= 1:
    exit()

if len(forcas) != qtd_sorteios:
    exit()

if qtd_sorteios > num_premios:
    print("Não é possível realizar o sorteio.")
    exit()

ponteiro = -1
indice = 0

while len(forcas) > indice:
    inicial = ponteiro
    ponteiro = (ponteiro + forcas[indice]) % num_premios

    if premios[ponteiro]:
        print(f"{premios[ponteiro][0]} {premios[ponteiro][1]}", end=" ")
        premios[ponteiro] = None
    
    else:
        forcas.insert(indice + 1, forcas[indice] - 1)
        ponteiro = inicial

    indice += 1
