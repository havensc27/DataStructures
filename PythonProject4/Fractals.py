from Graphics import *

from math import *
def find_point(p1, distance, angle):
    rad_angle = -1 * radians(angle)
    xcor = cos(rad_angle) * distance + p1.getX()
    ycor = sin(rad_angle) * distance + p1.getY()
    return Point(xcor, ycor)

def fractal_tree(d, x1, y1, x2, y2, x3, y3):
    if d == 2:
        return
    else:
        Line(Point(x1, y1), Point(x2, y2)).draw(win)
        Line(Point(x1, y1), Point(x3, y3)).draw(win)
        Line(Point(x2, y2), Point(x3, y3)).draw(win)
        fractal_tree(d - 1, x1, y1, (x1 + x2) / 2, (y1 + y2) / 2, (x1 + x3) / 2, (y1 + y3) / 2)
        fractal_tree(d - 1, x2, y2, (x1 + x2) / 2, (y1 + y2) / 2, (x2 + x3) / 2, (y2 + y3) / 2)
        fractal_tree(d - 1, x3, y3, (x1 + x3) / 2, (y1 + y3) / 2, (x2 + x3) / 2, (y2 + y3) / 2)
