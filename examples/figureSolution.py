import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def nagon(n):
    angle = 360 / n
    side = 500 / n

    for i in range(n):
        t.right(angle)
        t.forward(side)

nagon(4)
nagon(5)
nagon(6)
nagon(10)

input("Press Enter to exit...")
