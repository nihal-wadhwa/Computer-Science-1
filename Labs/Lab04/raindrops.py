"""
Author: Nihal Wadhwa
Raindrops: The purpose of this program is to draw a picture of different colored raindrops in a pond. 
"""

import turtle as tt
import math
import random

POND_X = 500
POND_Y = 500

def setup():
    """
    Sets up the window and creates the pond part of the picture.
    Precondition: turtle at default state and position
    Postcondition: turtle draws pond and fills it with pale turquoise color. Turtle ends at the top right corner of the pond, facing up
    """
    tt.setworldcoordinates(-POND_X,-POND_Y,POND_X,POND_Y)
    tt.up()
    tt.fillcolor('pale turquoise')
    tt.begin_fill()
    tt.forward(POND_X)
    tt.left(90)
    tt.down()
    tt.forward(POND_Y)
    tt.left(90)
    tt.forward(POND_X*2)
    tt.left(90)
    tt.forward(POND_Y*2)
    tt.left(90)
    tt.forward(POND_X*2)
    tt.left(90)
    tt.forward(POND_X*2)
    tt.end_fill()


def raindrop(rad):
    """
    Draws a raindrop of random color at a random position in the pond with radius rad.
    Precondition: turtle is down
    Postcondition: turtle has drawn a colored raindrop, turtle ends at the bottom of the raindrop drawn, facing right. 
    """
    tt.up()
    tt.setpos(random.randint(-POND_X+(rad*8), POND_X-(rad*8)), random.randint(-POND_Y+(rad*8), POND_Y-(rad*8))) 
    tt.down()
    rand_color()
    tt.begin_fill()
    tt.circle(rad)
    tt.end_fill()
    tt.color('black')


def ripple(num_rip, rad):
    """
    Draws a specific number of ripples num_rip of each raindrop with radius rad
    Precondition: turtle is at the right-most point of the inner-most circle facing right
    Postcondition: turtle has drawn the ripples and is located at the left-most point of the inner-most circle facing right
    """
    irad = rad
    while (num_rip > 0):
        tt.up()
        tt.forward(irad)
        tt.down()
        tt.left(90)
        tt.circle(rad)
        tt.right(90)   
        num_rip -= 1
        rad += irad
    tt.up()
    tt.backward(rad)
        
            
def rand_color():
    """
    Sets the turtle to a random color
    Postcondition: turtle is set to random color
    """
    R = random.random()
    G = random.random()
    B = random.random()
    tt.color(R, G, B)


def raindrop_pic(num_drop):
    """
    Draws a picture of num_drop raindrops and returns the cumulative area of the raindrops.
    Precondition: num_drop must be a positive integer
    Postcondition: The turtle draws the raindrops and is located at the left-most point of the inner-most circle of the last drop, facing right
    """
    
    if(num_drop == 0):
        return 0
    else:
        rand_rad = random.randint(1,20)
        rand_rip = random.randint(3,8)
        raindrop(rand_rad)
        tt.up()
        tt.left(90)
        tt.forward(rand_rad)
        tt.right(90)
        ripple(rand_rip, rand_rad)
        return math.pi*(rand_rad**2) + raindrop_pic(num_drop-1)
        

    
def main():
    """
    Draws a picture of raindrops in a pond after asking the user for the amount of drops in the pond.
    Precondition: turtle is at default state and position
    Postcondition: turtle draws the raindrops and is located at the left-most point of the inner-most circle of the last drop, facing right
    Postcondition: prints the cumulative area of all raindrops
    """
    numDrop = int(input('Raindrops (1-100): '))
    if (numDrop > 100) or (numDrop < 0):
        print('Raindrops must be between 1 and 100 inclusive.')
    else:
        tt.speed(0)
        setup()
        print("The total area of the raindrops is", raindrop_pic(numDrop), "square units.")
        tt.done()

main()
