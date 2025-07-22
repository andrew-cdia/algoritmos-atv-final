"""
Entrada de Dados
"""

DIMENSOES = [int(a) for a in input().split(' ')]

TABULEIRO = []

for _ in range(DIMENSOES[0]):
    linha = input().split(' ')

    if len(linha) != DIMENSOES[1]:
        exit()
    
    TABULEIRO.append(linha)

PERIMETRO_MAXIMO = int(input())

"""
Funções
"""

def maior_perimetro(matriz : list) -> int:
    tesouros = []

    for linha in range(DIMENSOES[0]):
        for coluna in range(DIMENSOES[1]):

            calculo, p = 0, 0

            for i in range(linha, DIMENSOES[0]):
                for j in range(coluna, DIMENSOES[1]):
                    
                    p = 2 * ((i - linha) + (j - coluna) + 2)

                    if p > PERIMETRO_MAXIMO:
                        break
                    
                    soma = matriz[linha:i]
                    soma = [a[coluna:j] for a in soma]

                    for n in soma:
                        calculo += n.count("X")

            tesouros.append(calculo)

    return max(tesouros)

"""
Execução principal
"""

if __name__ == "__main__":
    print(maior_perimetro(TABULEIRO))