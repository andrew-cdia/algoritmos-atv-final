"""
Variáveis importantes
"""

SPACE = 12
QTD_DIAS = 5
QTD_ATIVIDADES = 10

DAYS = {
        "Segunda" : 0,
        "Terça" : 1,
        "Quarta" : 2,
        "Quinta" : 3,
        "Sexta" : 4
    }

def remove(timetable : list, day : int, hour : int, quantity : int) -> list:
    for n in range(hour, hour + quantity):
        timetable[day][n] = "Livre"
    return timetable

def add(timetable : list, day : int, hour : int, quantity : int, nome : str) -> list:
    for n in range(hour, hour + quantity):
        timetable[day][n] = nome
    return timetable

def find(timetable : list, quantity):
    for day in range(len(timetable)):
        for hour in range(len(timetable[day]) - quantity + 1):
            if test(timetable, day, hour, quantity):
                return (day, hour)
    return None

def test(timetable : list, day : int, hour : int, quantity : int) -> bool:
    try:
        for hour in timetable[day][hour : hour + quantity]:
            if hour != "Livre":
                return False
        return True    
    except IndexError:
        return False

semana = []

for _ in range(QTD_DIAS):
    dias = input().split(" ")

    if len(dias) != 10:
        exit()

    semana.append(dias)

comandos = []

for _ in range(int(input(""))):
    comando = input().split(" ")

    if len(comando) != 3 and len(comando) != 4:
        exit()
    
    comandos.append(comando)

for comando in comandos:
    if comando[0].lower() == "adicionar":
        nome = comando[1]
        quantidade = int(comando[2])

        data = find(semana, quantidade)
    
        if not data:
            print(f"Não foi possível alocar a atividade {nome}")
            continue
        
        semana = add(semana, data[0], data[1], quantidade, nome)

    elif comando[0].lower() == "remover":
        dia = DAYS[comando[1]]
        hora = int(comando[2]) - 8
        final = int(comando[3]) - 8
        quantidade = final - hora

        if quantidade > 0 and hora >= 0 and final <= QTD_ATIVIDADES:
            semana = remove(semana, dia, hora, quantidade)

        # Verificar Lógica
    
    else:
        continue

def print_table(table) -> None:
    print("Horário".ljust(SPACE), end="")
    for dia in DAYS.keys():
        print(f"{dia.ljust(SPACE)}", end='')
    print()

    horario_inicial = 8
    for atividade in range(QTD_ATIVIDADES):
        print(f"{horario_inicial} - {horario_inicial + 1}".ljust(SPACE), end="")
        for dia in range(QTD_DIAS):
            print(f"{semana[dia][atividade].ljust(SPACE)}", end="")
        horario_inicial += 1
        print()

print_table(semana)