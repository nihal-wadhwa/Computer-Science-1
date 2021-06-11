import math

def quadratic_roots(a, b, c):
    """
    Takes three numbers (a,b,c) and prints a quadratic function in the form of ax2+bx+c. Then, the function prints the number of roots possible as well as the roots itself.
    Precondition: The parameters are integers.
    Postcondition: The quadratic function, number of roots, and roots are printed.
    """
    if (((math.pow(b,2))-(4*a*c))> 0):
        print("Equation: ",str(a),"x^2 + ",str(b),"x + ",str(c), sep="")
        print("Two roots.")
        print("x =",((-b + math.sqrt(math.pow(b,2)-4*a*c))/(2*a)))
        print("x =",((-b - math.sqrt(math.pow(b,2)-4*a*c))/(2*a)))
        
    elif (((math.pow(b,2))-4*a*c) == 0):
        print("Equation: ",str(a),"x^2 + ",str(b),"x + ",str(c), sep="")
        print("One root.")
        print("x =",((-b + math.sqrt(math.pow(b,2)-4*a*c))/(2*a)))
        
    else :
        print("Equation: ",str(a),"x^2 + ",str(b),"x + ",str(c), sep="")
        print("No roots.")
    

def main():
    """
    Takes three inputs from user and stares as integers a,b, and c. Then uses those integers to print the quadratic equation and its roots.
    Precondition: The user inputs only integers
    Postcondition: The quadratic function created using variables a,b and c, number of roots, and roots are printed.
    """
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    quadratic_roots(a, b, c)
    

def test_cases():
    """
    Tests the quadratic_roots() function by calling the function ten times with ten different pairs of numbers.
    Precondition: The parameters are integers.
    Postcondition: The quadratic function, number of roots, and roots are printed for each test case.
    """
    quadratic_roots(1,3,-21)
    quadratic_roots(2,-4,-6)
    quadratic_roots(1,4,-12)
    quadratic_roots(4,12,9)
    quadratic_roots(-2,-11,-21)
    quadratic_roots(4,1,4)
    quadratic_roots(1,1,0)
    quadratic_roots(1,0,-16)
    quadratic_roots(1,-14,-49)
    quadratic_roots(1,10,25)
    
       
main()
