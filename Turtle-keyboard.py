import turtle
import random

# variável de controle
running = True

def stop_program():
    global running
    running = False

def turn_left():
  player.color('light green')
  player.setheading(180)
  player.forward(10)

def turn_right():
  player.color('white')
  player.setheading(0)
  player.forward(10)

def turn_up():
  player.color('red')
  player.setheading(90)
  player.forward(10)

def Obstacle():
   obstacle.setpos(500, 0)
   obstacle.showturtle()
   obstacle.setheading(180)
   obstacle.forward(500)
   obstacle.hideturtle()

def RandomNum ():
    global running
    while running:
        randomResult = random.randint(1, 1000)
        if randomResult%2 == 0:
           Obstacle()
        if player.pos() == obstacle.pos():
            style = ('Courier', 30, 'italic')
            turtle.write('Hello!', font=style, align='center')

window = turtle.Screen()
window.bgcolor('midnight blue')

player = turtle.Turtle()
player.shape('turtle')
player.color('white')
player.penup()

obstacle = turtle.Turtle('square')
obstacle.hideturtle()
obstacle.penup()
obstacle.color('white')
RandomNum()
  
window.onkeypress(turn_left, "Left")
window.onkeypress(turn_right, "Right")
window.onkeypress(turn_up, "Up")
window.onkeypress(stop_program, "Escape")
window.listen()
  
turtle.done()