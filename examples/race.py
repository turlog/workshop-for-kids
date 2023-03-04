import turtle
import random

s = turtle.getscreen()
distances = [1,2,3,4,5,6]

def draw_meta(cart):
    cart.home()
    cart.penup()
    cart.goto(300,60)
    cart.pendown()
    cart.circle(40)
    cart.penup()
    cart.home()

# Ready steady...
cart = turtle.Turtle()
cart.color("green")
draw_meta(cart) # TODO prepare function like draw_meta to set up cart position
cart.penup()
cart.goto(-200,100)
cart.pendown()

# GO!
while(True):
    if cart.pos() >= (300,100):            
        print("Race Finished!")
        break
    else:
        input("Press 'Enter' to go!")
        distance = random.choice(distances) * 20
        cart.forward(distance)

input("Press 'Enter' to exit...")

# TODO add second player 