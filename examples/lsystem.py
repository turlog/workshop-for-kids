def generate(structure, rules, generations):
    print(0, structure)
    for n in range(generations):
        structure = "".join(rules.get(token, token) for token in structure)
        print(n+1, structure)
    return structure


def visualize(structure, traces, rotations, initial=(0, -300)):
    from turtle import Turtle

    turtle = Turtle()
    turtle._delay(0)
    turtle.hideturtle()
    turtle.left(90)
    turtle.penup()
    turtle.goto(*initial)
    turtle.pendown()
    turtle.pensize(3)
    turtle.speed(0)
    stack = []
    for token in structure:
        if token in rotations:
            turtle.right(rotations[token])
        if token in traces:
            turtle.pencolor(traces[token][0])
            turtle.forward(traces[token][1])
        if token == "[":
            stack.append((turtle.pos(), turtle.heading()))
        if token == "]":
            pos, heading = stack.pop(-1)
            turtle.penup()
            turtle.setposition(pos)
            turtle.setheading(heading)
            turtle.pendown()
    turtle.screen.exitonclick()

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
        structure="P", rules={"P": "G[-P][+P]", "G": "GG"}, generations=4
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
        structure="A", rules={"A": "+BF-AFA-FB+", "B": "-AF+BFB+FA-"}, generations=7
    ),
    traces={
        "F": ("#009900", 6),
    },
    rotations={
        "+": +90,
        "-": -90,
    },
    initial=(-400, -400)
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
        "F": ("#990099", 10),
        "G": ("#009900", 10),
        "X": ("#0000ff", 5)
    },
    rotations={
        "+": +45,
        "-": -45,
    },
    initial=(-200, -100)
)
