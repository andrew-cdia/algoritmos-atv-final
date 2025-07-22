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


"""
Execução principal
"""

if __name__ == "__main__":
    pass