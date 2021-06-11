"""
Nihal Wadhwa
This program is designed to draw a series of 12 hexagons in a circular format.
After one circle of six hexagons, the turtle shifts downward and completes another
circle of hexagon that are intertwined with the previous hexagons.

"""

import turtle

def hex_line():
    """
    Draws one side of a single hexagon with size 50
    precondition: turtle is down
    precondition: turtle is facing direction of previous side drawn OR default state.
    postcondition: turtle is at the opposite end of side drawn
    """
    turtle.down()
    turtle.forward(50)
    turtle.left(60)

def hex():
    """
    Draws one single hexagon with sides of size 50
    precondition:turtle is down
    precondition:turtle is at the bottom left corner of the previous hexagon facing right OR default state.
    postcondition: turtle ends at bottom left corner after current hexagon is
    drawn
    """
    hex_line()
    hex_line()
    hex_line()
    hex_line()
    hex_line()
    hex_line()

def trans():
    """
    Shifts the turtle to create next hexagon in a circle
    precondition: turtle is down
    precondition:turtle is at the bottom left corner of previous hexagon facing right
    postcondition:turtle has shifted to the top right corner of next hexagon in the sequence
    """
    turtle.forward(50)
    turtle.right(60)

def hex_circle():
    """
    Creates a single circle of hexagons
    precondition: turtle is down
    precondition: turtle is at default state OR at the bottom left corner of first hexagon of previous circle of hexagons facing right
    postcondition: turtle is at the at the bottom left corner of the first hexagon of the circle of hexagons just created
    """
    hex()
    trans()
    hex()
    trans()
    hex()
    trans()
    hex()
    trans()
    hex()
    trans()
    hex()
    trans()

def main():
    """
    Creates the two circles of hexagons
    precondition: turtle is at default state
    postcondition: turtle is at the bottom left corner of the first hexagon of the second circle of hexagons
    """
    turtle.pensize(4)
    hex_circle()
    turtle.right(60)
    hex_circle()
    

main()
