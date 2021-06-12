import turtle as tt
import math

def triangle_recur(length, depth):
    """
    Draws a patterns of shrinking triangles. Takes the parameters length for the length of the sides of the intial triangle and the depth for the recursion depth.
    Preconditon: turtle is down
    Precondition: turtle is at the the bottom corner of the initial triangle, facing right
    Precondition: Parameters are integers
    Postcondition: turtle as drawn a pattern of shrinking triangles, ending in the same state as it was in the precondition.
    """
    if (depth == 0):
        pass
    else:
        tt.left(120)
        tt.forward(length)
        tt.right(120)
        triangle_recur(length/2,depth-1)
        tt.forward(length)
        triangle_recur(length/2,depth-1)
        tt.right(120)
        tt.forward(length)
        tt.right(240)

def main():
    """
    Impliments the triangle recur function to create shrinking triangles based on the user's input for the depth and length.
    Preconditon: turtle is down
    Precondition: turtle is at the the bottom corner of the initial triangle, facing right
    Postcondition: turtle as drawn a pattern of shrinking triangles, ending in the same state as it was in the precondition.
    """
    length = int(input('Enter length: '))
    depth = int(input('Enter depth: '))
    triangle_recur(length,depth)
    
main()
