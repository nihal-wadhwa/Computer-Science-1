"""
Author: Nihal Wadhwa
Zig Zag: This program's purpose is to create a pattern of tilted zizags that alternate in color from red to green.
"""

import turtle as tt

def setcolor(depth):
    '''
    Sets the turtle color to alternate between red and green in the zz_recur function
    Postcondition: turtle changes from original color to the alternate color (red or green)
    '''
    
    if((depth % 2)== 0):
        tt.color('green')
    else:
        tt.color('red')


def zz_recur(length,depth):
    '''
    Recursively prints a pattern of zigzags that alternate between green and red colors.
    Precondition: turtle is down
    Precondition: turtle is at default state and position
    Precondition: length and depth are integers
    Postcondition: turtle prints pattern and ends at same state as precondition
    '''
    
    if(depth==0):
        pass
    else:
        tt.left(90)
        tt.forward(length/2)
        tt.right(90)
        tt.forward(length)
        tt.left(45)
        zz_recur(length/2,depth-1)
        setcolor(depth)
        tt.right(45)
        tt.back(length)
        tt.left(90)
        tt.back(length)
        tt.right(90)
        tt.back(length)
        tt.left(45)
        zz_recur(length/2,depth-1)
        setcolor(depth)
        tt.right(45)
        tt.forward(length)
        tt.left(90)
        tt.forward(length/2)
        tt.right(90)
        
        
def main():
    '''
    Tests the zz-recur function by taking the user input for length and depth.
    Precondition: turtle is down
    Precondition: turtle is at origin, facing right
    Postcondition: turtle has executed a pattern of zigzags and has returned to its previous location and state.
    '''
    length = int(input('Enter length: '))
    depth = int(input('Enter depth: '))
    zz_recur(length,depth)
    tt.color('black')
    tt.done()

    
main()
