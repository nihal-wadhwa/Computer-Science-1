"""
Author: Nihal Wadhwa
Turtle Scenery: This program's purpose is to create a scenery with two houses of varying sizes and a tree.
"""

import turtle as tt
import math

def init() :
    """
    Moves the turtle 275 units to the left to set up for the beginning of the phrase.
    Precondition: turtle is down
    Precondition: turtle is at default position
    Postcondition: turtle is 275 units left of the default poistion, facing right.
    """
    tt.up()
    tt.left(180)
    tt.forward(275)
    tt.right(180)
    tt.down()


def rect(x,y):
    """
    Draws rectangle with width x, and height y
    Precondition: turtle is at the bottom left of the rectangle, facing right
    Postcondition: turtle has drawn the rectangle, ending at the bottom left of the rectangle, facing right
    """
    tt.down()
    tt.forward(x)
    tt.left(90)
    tt.forward(y)
    tt.left(90)
    tt.forward(x)
    tt.left(90)
    tt.forward(y)
    tt.left(90)


def triangle(b,h):
    """
    Draws an isosoceles triangle with base b and height h.
    Precondition: turtle is at the bottom left of the triangle, facing left
    Postcondition: turtle draws the triangle, ending at the bottom left of the triangle, facing left
    """
    L = math.sqrt((h**2)+((b/2)**2))
    angle = math.degrees(math.asin(h/L))
    tt.forward(b)
    tt.right(180-angle)
    tt.forward(L)
    tt.right(2*angle)
    tt.forward(L)
    tt.right(180-angle)


def house(base, height, h, hcolor):
    """
    Draws a house with a roof and windows. Takes in the parameters of base, height, height of roof (h), and color of house (hcolor)
    Precondition: turtle is located at the bottom left of the house, facing right
    Precondition: turtle is down
    Precondition: Paramaters base, height, and h are integers. hcolor is a string
    Postcondition: turtle draws the house, ending at the bottom right of the house, facing right
    """
    tt.color(hcolor)
    tt.begin_fill()
    rect(base,height)
    tt.end_fill()    
    tt.forward((base/2)-(base/10))
    tt.color('brown')
    tt.begin_fill()
    rect(base/5,height/4)
    tt.end_fill()
    tt.up()
    tt.forward((base/2)+(base/10))
    tt.left(90)
    tt.forward(height)
    tt.left(90)
    tt.down()
    tt.color('black')
    tt.begin_fill()
    triangle(base,h)
    tt.end_fill()
    tt.up()
    tt.left(90)
    tt.forward((height/10)*6)
    tt.right(90)
    tt.forward((base/10)*3)
    tt.right(180)
    tt.color('grey')
    tt.begin_fill()
    rect(base/5,base/5)
    tt.end_fill()
    tt.up()    
    tt.left(180)
    tt.forward((base/10)*6)
    tt.right(180)
    tt.color('grey')  
    tt.begin_fill()
    rect(base/5,base/5)
    tt.end_fill()
    tt.up()
    tt.forward((base/10)*9)

    if ((base/height) > 1):       
        tt.right(90)
        tt.forward((height/10)*4)
        tt.left(90)
        tt.color('black')
        return (base*height)
    else:
        tt.left(90)
        tt.forward((height/10)*3)
        tt.left(90)
        tt.forward((base/10)*3)
        tt.right(180)
        tt.color('grey')
        tt.begin_fill()
        rect(base/5,base/5)
        tt.end_fill()
        tt.up()    
        tt.left(180)
        tt.forward((base/10)*6)
        tt.right(180)
        tt.color('grey')  
        tt.begin_fill()
        rect(base/5,base/5)
        tt.end_fill()
        tt.up()        
        tt.forward((base/10)*9)
        tt.right(90)
        tt.forward((height/10)*7)
        tt.left(90)
        tt.color('black')
        return (base*height)


def tree (h,w,r):
    """
    Draws a tree of height h, width w, and radius r.
    Precondition: turtle is at the bottom of the tree, facing right
    Precondition: turtle is down
    Postcondition: turtle has drawn a tree, ending at the bottom of the tree, facing right
    """
    tt.color('brown')
    tt.pensize(w)
    tt.down()
    tt.left(90)
    tt.forward(h)
    tt.right(90)
    tt.color('green')
    tt.begin_fill()
    tt.circle(r)
    tt.end_fill()
    tt.up()
    tt.left(90)
    tt.backward(h)
    tt.right(90)
    tt.up()
    tt.pensize(1)
    tt.color('black')

    
def main():
    """
    Draws two houses and a tree.
    Precondition: turtle is up
    Precondition: turtle is at default position
    Postcondition: turtle has drawn two houses and a tree, ending at the bottom right of the second house.
    """
    init()
    print("big facade is", house(100,200,60,'yellow'), "square units.")
    tt.forward(100)
    tree(200,5,50)
    tt.forward(100)
    print("small facade is",house(150,100,80,'cyan'), "square units.")
   
 

main()
tt.done()
    
    
    
