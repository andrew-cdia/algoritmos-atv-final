ORCAMENTO = int(input())

inf = []

for _ in range(int(input())):
    linha = input().split(", ")

    custo = int(linha[0])
    seguidores = set(linha[1:])

    inf.append([custo, seguidores])

def ingenua(inf : list, orc : int) -> tuple:
    pass

def atual(inf : list, orc : int) -> tuple:
    pass

def nova(inf : list, orc : int) -> tuple:
    pass


ing = ingenua(inf, ORCAMENTO)
print(ing)
print(f"Estratégia Ingênua: {ing[0]:.01}, {ing[1]}")

at = atual(inf, ORCAMENTO)
print(at)
print(f"Estratégia Atual: {at[0]:.01}, {at[1]}")

nv = nova(inf, ORCAMENTO)
print(nv)
print(f"Estratégia Nova: {nv[0]:.01}, {nv[1]}")