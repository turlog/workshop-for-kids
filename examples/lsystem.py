def generate(structure, rules, generations):
    print(structure)
    for n in range(generations):
        structure = "".join(rules.get(token, token) for token in structure)
        print(structure)
    return structure


def visualize(structure, traces, rotations):
    from turtle import Turtle

    turtle = Turtle()
    turtle.hideturtle()
    turtle.left(90)
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


visualize(
    structure=generate(
        structure="N", rules={"N": "YN", "Y": "OO[+N]O[-N]"}, generations=8
    ),
    traces={
        "N": ("#00ff00", 5),
        "Y": ("#00aa00", 10),
        "O": ("#005500", 10),
    },
    rotations={
        "+": +15,
        "-": -15,
    },
)
