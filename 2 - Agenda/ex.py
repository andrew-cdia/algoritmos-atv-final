"""
Variáveis Importantes
"""

LEN_SPACE = 12

DIAS = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

semana = []


"""
Procedimento de entrada dos dados
1. Restrições
2. Formato
3. Adequação
"""

for _ in range(5):
    dia = input("").split(" ")

    if len(dia) != 10:
        exit()
    
    semana.append(dia)

qtd_comandos = int(input())

comandos = []

for _ in range(qtd_comandos):
    comando = input("").split(" ")

    if comando[0].lower() == "remover" and len(comando) != 4:
        print("Comando inválido")
        exit()

    elif comando[0].lower() == "adicionar" and len(comando) != 3:
        print("Comando inválido")
        exit()

    comandos.append(comando)

"""
Funções utilizadas
"""

def teste(timetable : list, day : int, inicio : int, fim : int) -> list:
    try:
        for activity in timetable[day][inicio : fim]:
            if activity != "Livre":
                return False
        return True
    except IndexError:
        return False

def muda(timetable : list, day : int, inicio: int, fim : int, name="Livre") -> list:
    i = 0
    while i < (fim - inicio):
        timetable[day][inicio + i] = name
        i += 1

    return timetable

def acha_posicao(timetable : list, qtd : int) -> int|None:
    for day in range(len(timetable)):
        for hour in range(len(timetable[day]) - qtd + 1):
            if teste(timetable, day, hour, hour + qtd):
                return (day, hour)
    return None 

def print_tabela(semana : list) -> None:
    cab = ["Horário"] + DIAS
    for n in cab:
        print(f"{n}{" " * (LEN_SPACE - len(n))}", end='')
    print()
    inicial = 8
    for atv in range(len(semana[0])):
        horario = f"{inicial}-{inicial+1}"
        print(f"{horario}{" " * (LEN_SPACE - len(horario))}", end="")
        for day in range(len(DIAS)):
            print(f"{semana[day][atv]}{" " * (LEN_SPACE - len(semana[day][atv]))}", end="")
        inicial += 1
        print()

"""
Loop Principal
"""

for comando in comandos:
    if comando[0].lower() == "adicionar":
        qtd = int(comando[2])
        data = acha_posicao(semana, qtd)

        if not data:
            print(f"Não foi possível alocar a atividade {comando[1]}")
            continue
        
        dia = data[0]
        hora = data[1]

        print(dia, hora)

        semana = muda(semana, dia, hora, hora + qtd, name=comando[1])

    elif comando[0].lower() == "remover":
        dia = DIAS.index(comando[1])
        inicio = int(comando[2]) - 8
        fim = int(comando[3]) - 8

        if teste(semana, dia, inicio, fim):
            semana = muda(semana, dia, inicio, fim)
    
    else:
        continue

"""
Resultado
"""

print_tabela(semana)