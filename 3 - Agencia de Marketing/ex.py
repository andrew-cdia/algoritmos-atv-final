"""
Entrada de Dados.
"""

ORCAMENTO = int(input())

INFLUENCIADORES = dict()

for _ in range(int(input())):
    linha = input().split(",")

    custo = int(linha[0])
    seguidores = set(linha[1:])

    INFLUENCIADORES.update({custo : seguidores})

"""
Métodos.
"""

def ingenua(influenciadores : list, orcamento : int) -> tuple:
    """
    Função que implementa o método ingênuo:
    inf : list = lista de influenciadores, onde inf[0] é o custo e inf[1] conjunto de seguidores.
    orc : int = orçamento total
    """
    influenciadores = sorted(influenciadores.items())

    gasto, seguidores = 0, set()

    for custo, seguidor in influenciadores:
        if gasto + custo > orcamento:
            break
        gasto += custo
        seguidores |= seguidor

    return (gasto, len(seguidores))
    

def atual(influenciadores : list, orcamento : int) -> tuple:
    """
    Função que implementa o método atual:
    inf : list = lista de influenciadores, onde inf[0] é o custo e inf[1] conjunto de seguidores.
    orc : int = orçamento total
    """
    custo_beneficio = [{
            'custo' : a,
            'seguidores' : b,
            'custo-beneficio' : a / len(b)
        } for a, b in influenciadores.items()]
    custo_beneficio = sorted(custo_beneficio, key=lambda k : k['custo-beneficio'])

    gasto, seguidores = 0, set()

    for relacao in custo_beneficio:
        if gasto + relacao['custo'] > orcamento:
            continue
        gasto += relacao['custo']
        seguidores |= relacao['seguidores']

    return (gasto, len(seguidores))

def nova(influenciadores : list, orcamento : int) -> tuple:
    
    gasto, seguidores = 0, set()

    residual = [{
            'custo' : a,
            'seguidores' : b,
            'custo-beneficio' : a / len(b)
        } for a, b in influenciadores.items()]

    while True:
        for relacao in residual:
            relacao['seguidores'] -= seguidores
            if len(relacao['seguidores']) > 0:
                relacao['custo-beneficio'] = relacao['custo'] / len(relacao['seguidores'])
            else:
                relacao['custo-beneficio'] = 0
        
        residual = sorted(residual, key=lambda k : k['custo-beneficio'])

        if len(residual) == 0 or gasto + residual[0]['custo'] > orcamento:
            break
        
        if residual[0]['custo-beneficio'] == 0:
            residual.pop(0)
            continue
        
        gasto += residual[0]['custo']
        seguidores |= residual[0]['seguidores']

        residual.pop(0)
    
    return (gasto, len(seguidores))

"""
Execução principal do programa.
"""

if __name__ == "__main__":
    ing = ingenua(INFLUENCIADORES, ORCAMENTO)
    print(f"Estratégia Ingênua: {ing[0]}.0, {ing[1]}")
    
    at = atual(INFLUENCIADORES, ORCAMENTO)
    print(f"Estratégia Atual: {at[0]}.0, {at[1]}")

    nv = nova(INFLUENCIADORES, ORCAMENTO)
    print(f"Estratégia Nova: {nv[0]}.0, {nv[1]}")