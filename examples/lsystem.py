from turtle import Turtle, onscreenclick


def generate(structure: str, rules: dict, generations: int) -> str:
    """
    structure - startowa konfiguracja symbol
    rulse - reguły zamieniania symboli
    generations - ilość cykli podman
    """
    print(0, structure)
    for n in range(generations):
        structure = "".join(rules.get(token, token) for token in structure)
        # wiersz powyżej działa tak jak poniższy prostszy kod:
        # structure = ""
        # for token in structure:
        #     if token in rules:
        #         structure += rules[token]
        #     else:
        #         structure += token
        print(n+1, structure)
    return structure


def waitforclick(screen):
    """
    Funkcja pomocnicza - czekanie na kliknięcie
    """
    screen.waiting = True

    def stop_waiting(*_):
        screen.waiting = False

    onscreenclick(stop_waiting)

    while screen.waiting:
        screen.update()


def visualize(structure: str, traces: dict, rotations: dict, initial: tuple =(0, -300)):
    """
    structure - układ do wizualizacji
    traces - symbole, któe mają być wizualizowane symbol -> (kolor, długość)
    rotations - kąty (w stopniach) odpowiadające symbolom
    initial - pozycja początkowa na ekranie
    """

    stack = []  # stos na którym odkładana będzie zapamiętana pozycja

    turtle = Turtle()  # nowy żółw
    turtle._delay(0)  # szybkie rysowanie
    turtle.speed(0)
    turtle.hideturtle()  # ukryj żółwia
    turtle.left(90)  # ustaw do góry ekranu
    turtle.penup()  # przesuń na pozycję początkową bez rysowania
    turtle.goto(*initial)
    turtle.pendown()
    turtle.pensize(3) # grubość linii

    for token in structure:
        if token in rotations:  # skręć o przypisany symbolowi kąt
            turtle.right(rotations[token])
        if token in traces:  # ustaw kolor i narysuj
            turtle.pencolor(traces[token][0])
            turtle.forward(traces[token][1])
        if token == "[":  # zapamiętaj pozycję
            stack.append((turtle.pos(), turtle.heading()))
        if token == "]":  # wróć do ostatnio zapamiętanej pozycji
            pos, heading = stack.pop(-1)
            turtle.penup()
            turtle.setposition(pos)
            turtle.setheading(heading)
            turtle.pendown()

    waitforclick(turtle.screen)
    turtle.clear()

# klasyczny przykład

generate('A', {'A': 'B', 'B': 'BA'}, 9)

# przykład z obumieraniem

generate('A', {'A': 'B', 'B': 'CA', 'C': 'AD', 'D': 'E', 'E': ' '}, 10)

# trawka

visualize(
    structure=generate(
        structure="N", rules={"N": "YN", "Y": "O[+N][-N]", "O": "OO"}, generations=8
    ),
    traces={
        "N": ("#00ff00", 15),
        "Y": ("#00aa00", 10),
        "O": ("#005500", 5),
    },
    rotations={
        "+": +20,
        "-": -15,
    },
)

# proste drzewko

visualize(
    structure=generate(
        structure="P", rules={"P": "G[-P][+P]", "G": "GG"}, generations=5
    ),
    traces={
        "P": ("#00ff00", 20),
        "G": ("#00aa00", 20),
    },
    rotations={
        "+": +15,
        "-": -15,
    },
)

# większe drzewko

visualize(
    structure=generate(
        structure="TP", rules={"P": "G[--G+L]L", "L": "G[++G-P]P" , "G": "RG", "T": "TT"}, generations=9
    ),
    traces={
        "G": ("#00aa00", 2),
        "R": ("#005500", 6),
        "T": ("#555500", 0.5),
    },
    rotations={
        "+": +30,
        "-": -25,
    },
)


# krzaczek

visualize(
    structure=generate(
        structure="F", rules={"F": "FF-[-F+F+F]+[+F-F-F]"}, generations=3
    ),
    traces={
        "F": ("#009900", 20),
    },
    rotations={
        "+": +22.5,
        "-": -22.5,
    },
)

# krzaczek z owocami

visualize(
    structure=generate(
        structure="X", rules={"X": "F-[[X]+X]+F[+FX]+[[X]-X]-F[-FX]", "F": "FF"}, generations=3
    ),
    traces={
        "F": ("#009900", 15),
        "X": ("#0000ee", 3),
    },
    rotations={
        "+": +25,
        "-": -25,
    },
)

# krzywa Hilberta

visualize(
    structure=generate(
        structure="A", rules={"A": "+BF-AFA-FB+", "B": "-AF+BFB+FA-"}, generations=6
    ),
    traces={
        "F": ("#009900", 10),
    },
    rotations={
        "+": +90,
        "-": -90,
    },
    initial=(-300, -300)
)

# trójkąt Sierpińskiego

visualize(
    structure=generate(
        structure="A", rules={"A": "B-A-B", "B": "A+B+A"}, generations=6
    ),
    traces={
        "A": ("#999900", 10),
        "B": ("#000099", 10),
    },
    rotations={
        "+": +60,
        "-": -60,
    },
    initial=(-200, -300)
)

# dragon curve

visualize(
    structure=generate(
        structure="F", rules={"F": "F+X+G", "G": "F-X-G"}, generations=10
    ),
    traces={
        "F": ("#990099", 9),
        "G": ("#009900", 9),
        "X": ("#0000ff", 5)
    },
    rotations={
        "+": +45,
        "-": -45,
    },
    initial=(-200, -100)
)
