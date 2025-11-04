from Graphics import *
win = GraphWin("My Circle", 1000, 800)  # Creates a window 1000 x 800 pixels
c = Circle(Point(50, 50), 10)  # A 10-pixel radius circle centered at 50,50
c.draw(win)  # Required in order for your shape to show up on screen
win.getMouse()  # Pause to view result
win.close()  # Close window when done

