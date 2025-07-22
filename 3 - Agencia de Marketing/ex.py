"""
Entrada de Dados.
"""

ORCAMENTO = int(input())

INFLUENCIADORES = list()

for _ in range(int(input())):
    linha = input().split(", ")

    custo = int(linha[0])
    seguidores = set(linha[1:])

    INFLUENCIADORES.append([custo, seguidores])

"""
Métodos.
"""

def ingenua(influenciadores : list, orcamento : int) -> tuple:
    """
    Função que implementa o método ingênuo:
    inf : list = lista de influenciadores, onde inf[0] é o custo e inf[1] conjunto de seguidores.
    orc : int = orçamento total
    """
    custo = [influenciador[0] for influenciador in influenciadores]
    custo = dict(enumerate(custo))
    custo = sorted(custo.items(), key=lambda k: k[1])

    gasto, seguidores = 0, set()

    for index, valor in custo:
        if gasto + valor > orcamento:
            break
        gasto += valor
        seguidores |= influenciadores[index][1]

    return (gasto, len(seguidores))
    

def atual(influenciadores : list, orcamento : int) -> tuple:
    """
    Função que implementa o método atual:
    inf : list = lista de influenciadores, onde inf[0] é o custo e inf[1] conjunto de seguidores.
    orc : int = orçamento total
    """
    custo_beneficio = [influenciador[0] / len(influenciador[1]) for influenciador in influenciadores]
    custo_beneficio = dict(enumerate(custo_beneficio))
    custo_beneficio = sorted(custo_beneficio.items(), key=lambda k: k[1])

    gasto, seguidores = 0, set()

    for index, _ in custo_beneficio:
        if gasto + influenciadores[index][0] > orcamento:
            break
        gasto += influenciadores[index][0]
        seguidores |= influenciadores[index][1]       
    
    return (gasto, len(seguidores))


def nova(inf : list, orc : int) -> tuple:
    pass


"""
Execução principal do programa.
"""

if __name__ == "__main__":
    ing = ingenua(INFLUENCIADORES, ORCAMENTO)
    print(ing)
    print(f"Estratégia Ingênua: {ing[0]}.0, {ing[1]}")

    
    at = atual(INFLUENCIADORES, ORCAMENTO)
    print(at)
    print(f"Estratégia Atual: {at[0]}.0, {at[1]}")

    """
    nv = nova(INFLUENCIADORES, ORCAMENTO)
    print(nv)
    print(f"Estratégia Nova: {nv[0]}.0, {nv[1]}")
    """
