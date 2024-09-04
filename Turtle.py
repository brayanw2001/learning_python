import turtle
import time

tart1 = turtle.Turtle()
tart2 = turtle.Turtle()

tart2.left(180)

tart1.forward(80)
tart2.forward(80)

tart1.left(90)
tart2.right(90)
tart1.forward(160)      # altura
tart2.forward(160)

tart1.left(90)
tart2.right(90)         # As tartarugas se cruzam e distanciam. -20 na largura
tart1.forward(90)
tart2.forward(90)

# desenham a fita
tart1.left(90)
tart2.right(90)
tart1.forward(160)
tart2.forward(160)

# desenham o chão
tart1.right(90)
tart2.left(90)
tart1.forward(160)
tart2.forward(160)

# voltam pra borda caixa
tart1.left(180)
tart2.right(180)
tart1.penup()
tart2.penup()
tart1.forward(90)
tart2.forward(90)

tart1.pendown()
tart2.pendown()
tart1.width(2)
tart2.width(2)
tart1.forward(90)
tart2.forward(90)
tart1.penup()
tart2.penup()
tart1.width(1)
tart2.width(1)

# sobem novamente
tart1.left(90)
tart2.right(90)
tart1.forward(160)
tart2.forward(160)

# desenham a tampa
tart1.right(90)
tart2.left(90)
tart1.pendown()
tart2.pendown()
tart1.forward(90)
tart2.forward(90)

tart1.left(90)
tart2.right(90)
tart1.forward(15)
tart2.forward(15)


tart1.left(90)
tart2.right(90)
tart1.forward(120)
tart2.forward(120)


tart1.right(90)
tart2.left(90)
tart1.forward(15)
tart2.forward(15)

tart1.right(90)
tart2.left(90)
tart1.forward(40)
tart2.forward(40)

tart1.hideturtle()
tart2.hideturtle()

time.sleep(3)
