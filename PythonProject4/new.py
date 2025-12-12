from Graphics import *
from Main import fractal_h_tree
from Queues import *

Version = "b"
max_depth = 6
start_length = 200
start_center_x = 300
start_center_y = 300

win = GraphWin("H-Tree Fractal b", 1000, 800)  # Creates a window 1000 x 800 pixels # Required in order for your shape to show up on screen
win.setBackground(color = "white")

def draw_h(win, x1, y1, length, d):

    half_length = length / 2

    x_l, x_r = x1 - length, x1 + length
    y_u, y_d = y1 - length, y1 + length

    line_width = 1 + (d // 2)

    Line(Point(x_l, y1), Point(x_r, y1)).draw(win)
    Line(Point(x_l, y_u), Point(x_l, y_d)).draw(win)
    Line(Point(x_r, y_u), Point(x_r, y_d)).draw(win)

    return [
        (x_l, y_u),
        (x_l, y_d),
        (x_r, y_u),
        (x_r, y_d)
    ]

if Version == "a":
    print("Run Version 'a': H-Tree version 1 (Recursive Versions)")
    fractal_h_tree(max_depth, start_center_x, start_center_y, start_length)

elif Version == "b":
    print("Run Version 'b': Queue H-Tree")

else:
    print("Invalid version selected. Just 'a' or 'b'.")

from math import *
def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)

q = Queue()

initial_draw = [max_depth, start_center_x, start_center_y, start_length]
q.enqueue(initial_draw)

while not q.empty():

    current_draw = q.dequeue
    d = current_draw[0]
    x = current_draw[1]
    y = current_draw[2]
    length = current_draw[3]

    corners = draw_h(win, x, y, length, d)

    if d > 1:
        new_depth = d - 1
        new_length = length / 2

        for new_x, new_y in corners:
            q.enqueue([new_depth, new_x, new_y, new_length])

win.getMouse()
win.close()




