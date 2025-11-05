from Graphics import *

def h_tree(d, center_x,center_y, length):
    if d == 0:
        return
    else:
        half_l = length / 2

        p1 = Point(center_x - half_l, center_y - half_l)
        p2 = Point(center_x - half_l, center_y + half_l)
        p3 = Point(center_x + half_l, center_y - half_l)
        p4 = Point(center_x + half_l, center_y + half_l)

        Line(Point(center_x - half_l, center_y), Point(center_x + half_l, center_y)).draw(win)
        Line(p1, p2).draw(win)
        Line(p3, p4).draw(win)

        new_length = half_l

        h_tree(d - 1, p1.getX(), p1.getY(), new_length)
        h_tree(d - 1, p2.getX(), p2.getY(), new_length)
        h_tree(d - 1, p3.getX(), p3.getY(), new_length)
        h_tree(d - 1, p4.getX(), p4.getY(), new_length)

from queue import *
q = Queue()
q.enqueue([7, 100, 700, 500, 100, 900, 700])

while not q.empty():

   q0 = q.dequeue()
   d = q0[0]
   x1 = q0[1]
   y1 = q0[2]
   x2 = q0[3]
   y2 = q0[4]
   x3 = q0[5]
   y3 = q0[6]
   Line(Point(x1, y1), Point(x2, y2)).draw(win)
   Line(Point(x1, y1), Point(x3, y3)).draw(win)
   Line(Point(x2, y2), Point(x3, y3)).draw(win)







