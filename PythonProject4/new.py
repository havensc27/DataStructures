from Graphics import *

Version = "b"
max_depth = 6
start_length = 200
start_center_x = 300
start_center_y = 300

win = GraphWin("H-Tree Fractal b", 1000, 800)  # Creates a window 1000 x 800 pixels # Required in order for your shape to show up on screen
win.setBackground(color = "white")

def draw_h(win, x1, y1, length, d):
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

        new_length = length / 2

        for next_x1, next_y1 in new_center:
            fractal_h_tree(d - 1, next_x1, next_y1, new_length)


def queue():

    def h_tree_queue(initial_d, initial_x1, initial_y1, initial_length):

        q = queue()

        q.enqueue([initial_d, initial_x1, initial_y1, initial_length])

        while not q.empty():
            q0 = q.dequeue()
            d = q0[0]
            x1 = q0[1]
            y1 = q0[2]
            length = q0[3]

            corners = draw_h(win, x1 , y1, length, d)

            if d > 0:
                new_length = length / 2
                for next_x1, next_y1 in corners:
                    q.enqueue([d - 1, next_x1, next_y1, new_length])
        return

initial_params = [max_depth, start_center_x / 2, start_center_y / 2, start_length]

if Version == "a":
    print("Run Version 'a': H-Tree version 1")

elif Version == "b":
    print("Run Version 'b': Queue H-Tree")
else:
    print("Invalid version selected. Just 'a' or 'b'.")

fractal_h_tree(max_depth, start_center_x, start_center_y, start_length)
win.getMouse()
win.close()




