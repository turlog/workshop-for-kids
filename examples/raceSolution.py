import turtle
import random

s = turtle.getscreen()
distances = [1,2,3,4,5,6]

def draw_meta(cart, line):
    cart.home()
    cart.penup()
    cart.goto(300,line - 40)
    cart.pendown()
    cart.circle(40)
    cart.penup()
    cart.home()

def set_start(cart, line):
    cart.penup()
    cart.goto(-200,line)
    cart.pendown()

# Ready steady...
cart1 = turtle.Turtle()
cart2 = cart1.clone()
cart1.color("green")
cart2.color("blue")
draw_meta(cart1, 100)
draw_meta(cart2, -100)
set_start(cart1, 100)
set_start(cart2, -100)

# GO!
while(True):
    if cart1.pos() >= (300,100):            
        print("Race Finished! Player 1 wins!")
        break
    elif cart2.pos() >= (300,-100):            
        print("Race Finished! Player 2 wins!")
        break
    else:
        input("Press 'Enter' to go!")
        distance1 = random.choice(distances) * 20
        distance2 = random.choice(distances) * 20
        cart1.forward(distance1)
        cart2.forward(distance2)

input("Press 'Enter' to exit...")
