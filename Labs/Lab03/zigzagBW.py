"""
Author: Nihal Wadhwa
Zig Zag: This program's purpose is to create a pattern of zizags using recursion.
"""
import turtle as tt

def zig_zag(length):
    '''
    Draws a zigzag with sides the size of the parameter length
    Precondition: turtle is down
    Precondition: turtle is at origin, facing right
    Postcondition: turtle has drawn a zigzag, and has returned to the original position and heading.
    '''
    tt.left(90)
    tt.forward(length/2)
    tt.right(90)
    tt.forward(length)
    tt.backward(length)
    tt.left(90)
    tt.backward(length)
    tt.left(90)
    tt.forward(length)
    tt.backward(length)
    tt.right(90)
    tt.forward(length/2)
    tt.right(90)

def zz_recur(length,depth):
    '''
    Draws a pattern of zigzags with sides the size of the parameter length and recurs a given amount of time with the paramater depth.
    Precondition: turtle is down
    Precondition: turtle is at origin, facing right
    Postcondition: turtle has drawn a pattern of zigzags, and has returned to the original position and heading.
    '''
    if(depth==0):
        pass
    else:
        tt.left(90)
        tt.forward(length/2)
        tt.right(90)
        tt.forward(length)
        zz_recur(length/2,depth-1)
        tt.back(length)
        tt.left(90)
        tt.back(length)
        tt.right(90)
        tt.backward(length)
        zz_recur(length/2,depth-1)
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
    tt.done()
    
main()
