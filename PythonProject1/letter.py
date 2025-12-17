import turtle

screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("lightblue")

yertle = turtle.Turtle()
yertle.speed(30)
yertle.shape("turtle")

def draw_triangle(size, color):
    yertle.color("green", color)
    yertle.begin_fill()
    for i in range(3):
        yertle.forward(size)
        yertle.left(120)
    yertle.end_fill()

def draw_ornament(x, y, color):
    yertle.up()
    yertle.goto(x, y)
    yertle.down()
    yertle.color(color)
    yertle.begin_fill()
    yertle.circle(10)
    yertle.end_fill()

def draw_star(x, y, size, color):
    yertle.up()
    yertle.goto(x, y)
    yertle.setheading(0)
    yertle.down()
    yertle.color(color)
    yertle.begin_fill()
    for i in range(4):
        yertle.forward(size)
        yertle.right(130)
    yertle.end_fill()

def draw_present(y, x, color, size):
    yertle.up()
    yertle.goto(x, y)
    yertle.setheading(0)
    yertle.down()
    yertle.color(color)
    yertle.begin_fill()
    for i in range(5):
        yertle.forward(size)
        yertle.left(90)
    yertle.end_fill()

    yertle.color("red")

    yertle.up()
    yertle.goto(x, y + size/2)
    yertle.setheading(0)
    yertle.down()
    yertle.forward(size)

    yertle.up()
    yertle.goto(x + size/2, y)
    yertle.setheading(90)
    yertle.down()
    yertle.forward(size)

def draw_bow(y, x, size, color):
    yertle.up()
    yertle.goto(x + size/2, y + size)
    yertle.down()
    yertle.color(color)
    yertle.begin_fill()
    yertle.circle(15, 100)
    yertle.end_fill()

    yertle.begin_fill()
    yertle.circle(-15, 180)
    yertle.end_fill()

yertle.up()
yertle.goto(-200, -100)
yertle.down()
draw_triangle(400, "green")

yertle.up()
yertle.goto(-160, 20)
yertle.down()
draw_triangle(330, "green")

yertle.up()
yertle.goto(-125, 120)
yertle.down()
draw_triangle(260, "green")

yertle.up()
yertle.goto(-30, -170)
yertle.setheading(0)
yertle.down()
yertle.color("brown", "brown")
yertle.begin_fill()
for i in range(2):
    yertle.forward(60)
    yertle.left(90)
    yertle.forward(70)
    yertle.left(90)
yertle.end_fill()

ornaments = [
    (-30, 10, "purple"), (0, 45, "yellow"), (50, 10, "brown"),
    (-50, 80, "red"), (50, 90, "pink"),
    (-20, 150, "orange"), (30, 150, "cyan"),
    (-90, 40, "red"), (50, 90, "pink"),
    (90, 130, "orange"), (30, 150, "cyan")
]

for x, c, y in ornaments:
    draw_ornament(x, c ,y)

draw_star(-20, 350, 60, "gold")

draw_present(-200, -200,"dark blue", 70)

draw_bow(-200, -200, 70, "purple")

yertle.up()
yertle.goto(-250, -250)
yertle.color((0.5, 0, 1))
yertle.write("Merry Christmas DeVon! This is your only gift btw.", move=True, font=("Calibri", 30, "italic"))
yertle.forward(15)

yertle.up()
yertle.goto(-300, -300)
yertle.color((0.5, 0, 1))
yertle.write("From, Conner!", move=True, font=("Calibri", 30, "italic"))

turtle.done()





