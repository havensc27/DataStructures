from Main import *
q = Queue()
q.enqueue([7, 100, 700, 500, 100, 900, 700])



if d > 0:
    q.enqueue([d - 1, x1, y1, (x1 + x1) / 2, (y1 + y1) / 2, (x1 + x1) / 2, (y1 + y1) / 2])
    q.enqueue([d - 1, x1, y1, (x1 + x1) / 2, (y1 + y1) / 2, (x1 + x1) / 2, (y1 + y1) / 2])
    q.enqueue([d - 1, x1, y1, (x1 + x1) / 2, (y1 + y1) / 2, (x1 + x1) / 2, (y1 + y1) / 2])

from math import *
def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)

def h_tree_queue(initial_d, initial_x, initial_y, initial_length):

    q = Queue()

    q.enqueue([initial_d, initial_x, initial_y, initial_length])

    while not q.empty():
        q0 = q.dequeue()
        d = q0[0]
        x1 = q0[1]
        y1 = q0[2]
        length = q0[3]




