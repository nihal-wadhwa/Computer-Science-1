"""
Author: Nihal Wadhwa
Favorite Song Program
"""


import turtle as tt

def square(i1, i2, i3):
    """
    Draws a single square of a color taken by parameter color
    Precondition: turtle is at top left corner of square, facing right
    Precondition: turtle is down
    Precondition: i1, i2, i3 are all numbers.
    Postcondition: turtle has drawn a colored sqaure, ending at the top right corner facing right 
    """
    tt.color(i1, i2, i3)
    tt.begin_fill()
    tt.forward(10)
    tt.right(90)
    tt.forward(10)
    tt.right(90)
    tt.forward(10)
    tt.right(90)
    tt.forward(10)
    tt.right(90)
    tt.forward(10)
    tt.end_fill()

def paint_line(line):
    """
    Draws a line of colored squares based on the line of text that is taken as parameter line.
    Precondition: line is a line of text
    Precondition: turtle starts at the leftmost side of the picture, facing right
    Postcondition: turtle draws colored squares based on one line of lyrics, ends at the rightmost square in the left corner facing down
    
    """
    i = 0
    for index in range(len(line)-1):
        if(ord(line[index]) < 70):
            square(1,0.6,1)
        elif (70 <= ord(line[index]) < 100):
            square(0.2,1,0.2)
        elif (100 <= ord(line[index]) < 110):
            square(1,1,0.4)
        elif (110 <= ord(line[index]) < 122):
            square(0.2,1,1)
        else:
            tt.colormode(255)
            square(255,113,181)
            tt.colormode(1.0)
        index += 1
        i += 1
    tt.right(90)
    tt.forward(10)
    tt.right(90)
    tt.forward(i*10)
    tt.right(180)

def picture(file):
    """
    Draws a picture of colored squares based on the text file of lyrics that is taken as parameter file.
    Precondition: file is a .txt file located in same directory as program
    Precondition: turtle starts at origin, facing east
    Postcondition: turtle draws colored squares based on the lyrics in file, ends at the last square in the left corner facing down    
    """
    tt.up()
    tt.tracer(100,30)
    tt.goto(-375, 310)
    song = open(file)
    for line in song:
        paint_line(line)

def main():
    """
    Takes input for the text file and executes the picture function.
    Precondition: input is the name of a .txt file located in same directory as program
    Precondition: turtle starts at origin, facing east
    Postcondition: turtle draws colored squares based on the lyrics in file, ends at the last square in the left corner facing down    
    """
    inp = input('Enter file name: ')
    picture(inp)

main()
