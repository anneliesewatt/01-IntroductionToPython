"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Anneliese Watt.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

tom = rg.SimpleTurtle('turtle')
tom.pen = rg.Pen('yellow', 5)
tom.speed = 20

size = 130

for k in range(7):

    tom.draw_circle(size)

    tom.pen_up()
    tom.left(45)
    tom.forward(15)
    tom.left(45)

    tom.pen_down()
    size = size - 10

for k in range(15):
    tom.left(90)
    tom.forward(20)

sally = rg.SimpleTurtle('turtle')
sally.pen = rg.Pen('red', 20)
sally.speed = 20

size = 50

for k in range (2):
    sally.draw_square(size)
    sally.pen_up()
    sally.right (90)
    sally.forward (5)
    sally.right (90)

    sally.pen_down()
    size = size - 5
for k in range (15):
    sally.right (45)
    sally.forward(10)

window.close_on_mouse_click()
