from Graphics import *
from Queues import *

Version = "a"
max_depth = 6
start_length = 200
start_center_x = 500
start_center_y = 300

win = GraphWin("H-Tree Fractal", 1000, 800)  # Creates a window 1000 x 800 pixels # Required in order for your shape to show up on screen
win.setBackground(color = "white")

def draw_h(win, x1, y1, length, d):
    x_l, x_r = x1 - length, x1 + length
    y_u, y_d = y1 - length, y1 + length

    Line(Point(x_l, y1), Point(x_r, y1)).draw(win)
    Line(Point(x_l, y_u), Point(x_l, y_d)).draw(win)
    Line(Point(x_r, y_u), Point(x_r, y_d)).draw(win)

    return [
        (x_l, y_u),
        (x_l, y_d),
        (x_r, y_u),
        (x_r, y_d)
    ]

from math import *
def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)

def fractal_h_tree(d, x1, y1, length):
    if d == 0:
        return
    else:
        new_center = draw_h(win, x1, y1, length, d)

        new_length1 = length / 2

        for next_x1, next_y1 in new_center:
            fractal_h_tree(d - 1, next_x1, next_y1, new_length1)

version_input = input("Enter 'a' for Fractal H-Tree or 'b' for Queue H-Tree: ")
if version_input == "a":
    print("Run version 'a': Fractal H-Tree")
    fractal_h_tree(max_depth, start_length, start_center_x, start_center_y)
elif version_input == "b":
    print("Run version 'b': Queue H-Tree")
    Queue()

Version = "b"
max_depth = 6
start_length = 200
start_center_x = 500
start_center_y = 300
win = GraphWin("H-Tree Fractal Version b (Queue)", 1000, 800)  # Creates a window 1000 x 800 pixels # Required in order for your shape to show up on screen

def draw_h(win, x1, y1, length, d):
    x_l, x_r = x1 - length, x1 + length
    y_u, y_d = y1 - length, y1 + length

    Line(Point(x_l, y1), Point(x_r, y1)).draw(win)
    Line(Point(x_l, y_u), Point(x_l, y_d)).draw(win)
    Line(Point(x_r, y_u), Point(x_r, y_d)).draw(win)

    return [
        (x_l, y_u),
        (x_l, y_d),
        (x_r, y_u),
        (x_r, y_d)
    ]

q = Queue()

q.enqueue([max_depth, start_center_x, start_center_y, start_length])

while not q.empty():

    q0 = q.dequeue()
    d = q0[0]
    x = q0[1]
    y = q0[2]
    length = q0[3]

    corners = draw_h(win, x, y, length, d)

    if d > 1:
        new_depth = d - 1
        new_length = length / 2

        for new_x, new_y in corners:
            q.enqueue([new_depth, new_x, new_y, new_length])

print("Drawing in progress. Click window to close.")

fractal_h_tree(max_depth, start_center_x, start_center_y, start_length)
win.getMouse()
win.close()



