"""
Author: Nihal Wadhwa
Typography: This program's purpose is to create a phrase, "SPEEDY TOM," using turtle graphics to commemorate Tom's speed.
"""

import turtle as tt


def init() :
    """
    Moves the turtle 275 units to the left to set up for the beginning of the phrase.
    Precondition: turtle is down
    Precondition: turtle is at default position
    Postcondition: turtle is 275 units left of the default poistion, facing left.
    """
    tt.up()
    tt.left(180)
    tt.forward(275)
    tt.right(90)
    tt.forward(50)
    tt.left(90)
    tt.down()


def trans() :
    """
    Moves turtle from the top right of the previous letter to the top right of next letter to be drawn.
    Precondition: turtle is down.
    Precondition: turtle is located at the top right of the previous letter, facing left.
    Postcondition: turtle is located at the top right of the next letter.
    """
    tt.right(180)
    tt.up()
    tt.forward(75)
    tt.down()
    tt.right(180)
    

def write_S():
    """
    Turtle draws the letter S.
    Precondition: turtle is down.
    Precondition: turtle is located at the top right of the S, facing left.
    Postcondition: turtle has drawn the letter S, and is located at the top right of the letter.
    """

    tt.forward(50)
    tt.left(90)
    tt.forward(25)
    tt.left(90)
    tt.forward(50)
    tt.right(90)
    tt.forward(25)
    tt.right(90)
    tt.forward(50)
    tt.backward(50)
    tt.up()
    tt.right(90)
    tt.forward(50)
    tt.left(90)


def write_P():
    """
    Turtle draws the letter P.
    Precondition: turtle is down.
    Precondition: turtle is located at the top right of the P, facing left.
    Postcondition: turtle has drawn the letter P, and is located at the top right of the letter.
    """
    tt.forward(50)
    tt.left(90)
    tt.forward(50)
    tt.backward(25)
    tt.left(90)
    tt.forward(50)
    tt.left(90)
    tt.forward(25)
    tt.left(90)


def write_E():
    """
    Turtle draws the letter E.
    Precondition: turtle is down.
    Precondition: turtle is located at the top right of the E, facing left.
    Postcondition: turtle has drawn the letter E, and is located at the top right of the letter.
    """
    tt.forward(50)
    tt.left(90)
    tt.forward(25)
    tt.left(90)
    tt.forward(25)
    tt.backward(25)
    tt.right(90)
    tt.forward(25)
    tt.left(90)
    tt.forward(50)
    tt.left(90)
    tt.up()
    tt.forward(50)
    tt.left(90)


def write_D():
    """
    Turtle draws the letter D.
    Precondition: turtle is down.
    Precondition: turtle is located at the top right of the D, facing left.
    Postcondition: turtle has drawn the letter D, and is located at the top right of the letter.
    """
    tt.up()
    tt.left(90)
    tt.forward(25)
    tt.right(130)
    tt.down()
    tt.forward(40)
    tt.left(130)
    tt.forward(50)
    tt.left(130)
    tt.forward(40)
    tt.up()
    tt.left(50)
    tt.forward(25)
    tt.left(90)


def write_Y():
    """
    Turtle draws the letter Y.
    Precondition: turtle is down.
    Precondition: turtle is located at the top right of the Y, facing left.
    Postcondition: turtle has drawn the letter Y, and is located at the top right of the letter.
    """
    tt.left(90)
    tt.forward(25)
    tt.right(90)
    tt.forward(25)
    tt.left(90)
    tt.forward(25)
    tt.backward(25)
    tt.right(90)
    tt.forward(25)
    tt.right(90)
    tt.forward(25)
    tt.up()
    tt.right(90)
    tt.forward(50)
    tt.left(180)

    
def write_T():
    """
    Turtle draws the letter T.
    Precondition: turtle is down.
    Precondition: turtle is located at the top right of the T, facing left.
    Postcondition: turtle has drawn the letter T, and is located at the top right of the letter.
    """
    tt.forward(50)
    tt.backward(25)
    tt.left(90)
    tt.forward(50)
    tt.backward(50)
    tt.left(90)
    tt.forward(25)
    tt.left(180)


def write_O():
    """
    Turtle draws the letter O.
    Precondition: turtle is down.
    Precondition: turtle is located at the top right of the O, facing left.
    Postcondition: turtle has drawn the letter O, and is located at the top right of the letter.
    """
    tt.forward(25)
    tt.left(90)
    tt.forward(50)
    tt.left(90)
    tt.forward(25)
    tt.left(90)
    tt.forward(50)
    tt.left(90)


def write_M():
    """
    Turtle draws the letter M.
    Precondition: turtle is down.
    Precondition: turtle is located at the top right of the M, facing left.
    Postcondition: turtle has drawn the letter M, and is located at the top right of the letter.
    """
    tt.forward(50)
    tt.left(90)
    tt.forward(50)
    tt.backward(50)
    tt.left(90)
    tt.forward(25)
    tt.right(90)
    tt.forward(50)
    tt.backward(50)
    tt.left(90)
    tt.forward(25)
    tt.right(90)
    tt.forward(50)
    tt.backward(50)
    tt.left(90)

    
def main():
    """
    Turtle draws phrase "SPEEDY TOM" on the canvas.
    Precondition: turtle is up
    Precondition: turtle is at default position
    Postcondition: Turtle is at the top right corner of the letter M at the end of the phrase, facing left.
    """
    init()
    write_S()
    trans()
    write_P()
    trans()
    write_E()
    trans()
    write_E()
    tt.right(180)
    tt.up()
    tt.forward(50)
    tt.down()
    tt.right(180)
    write_D()
    trans()
    write_Y()
    trans()
    write_T()
    tt.right(180)
    tt.up()
    tt.forward(50)
    tt.down()
    tt.right(180)
    write_O()
    trans()
    write_M()
    tt.done()


main()
                
