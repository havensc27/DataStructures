from Graphics import *

from math import *
def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)

Version = "c"
max_depth = 200
start_length = 300
start_center_x = 300
start_center_y = 200

win = GraphWin(Version, 1000, 900)
win.setBackground(color = "white")

def draw_rectangle(win, x1, y1, length):
    x_offset = length
    y_offset = length

    p1 = Point(x1 - x_offset, y1 - y_offset)
    p2 = Point(x1 + x_offset, y1 + y_offset)

    rect = Rectangle(p1, p2)
    rect.setOutline("pink")
    rect.setWidth(3)
    rect.draw(win)

    Line(Point(x1, y1), Point(x1, y1)).draw(win)
    Line(Point(x1, y1), Point(x1, y1)).draw(win)
    Line(Point(x1, y1), Point(x1, y1)).draw(win)

    return [
        (x1, y1),
        (x1, y1),
        (x1, y1),
        (x1, y1)
    ]

from math import *
def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)

def rectangle_fractal(d, x1, y1, length):
    if d == 0:
        return
    else:
        draw_rectangle(win, x1, y1, length)

        new_length = length / 2

        rectangle_fractal(d - 1, x1, y1, new_length)

rectangle_fractal(max_depth, start_center_x, start_center_y, start_length)
win.getMouse()
win.close()