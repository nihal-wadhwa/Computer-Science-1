'''
Author: Nihal Wadhwa
GCD Two Ways
'''

import math

def gcd_rec(a,b):
    """
    Finds the greatest common denominator between two numbers a and b using recursion
    Precondition: a and b are positive integers
    Postcondition: Returns the greatest common denominator of numbers a and b
    """
    if (b==0):
        return a
    else:
        return gcd_rec(b, a % b)


def test_gcd_rec():
    """
    Tests the gcd_rec function using 6 diverse test cases.
    Postcondition: Prints the each of the 6 test cases of the gcd_recur function
    """
    print('1. The GCD of 5 and 5 is:', gcd_rec(5,5))
    print('2. The GCD of 23 and 4 is:', gcd_rec(23,4))
    print('3. The GCD of 20 and 40 is:', gcd_rec(20,40))
    print('4. The GCD of 15 and 10 is:', gcd_rec(15,10))
    print('5. The GCD of 18 and 12 is:', gcd_rec(18,12))
    print('6. The GCD of 580 and 26 is:', gcd_rec(580,26))
   


def gcd_iter(a,b):
    """
    Finds the greatest common denominator between two numbers a and b using iteration
    Precondition: a and b are positive integers
    Postcondition: Returns the greatest common denominator of numbers a and b
    """
    while (b != 0):
        temp = b
        b =  a%b
        a = temp
    return a

        
def test_gcd_iter():
    """
    Tests the gcd_iter function using 6 diverse test cases.
    Postcondition: Prints the each of the 6 test cases of the gcd_iter function
    """
    print('1. The GCD of 5 and 5 is:', gcd_iter(5,5))
    print('2. The GCD of 23 and 4 is:', gcd_iter(23,4))
    print('3. The GCD of 20 and 40 is:', gcd_iter(20,40))
    print('4. The GCD of 15 and 10 is:', gcd_iter(15,10))
    print('5. The GCD of 18 and 12 is:', gcd_iter(18,12))
    print('6. The GCD of 580 and 26 is:', gcd_iter(580,26))


def main():
    """
    Finds the greatest common denominator between two numbers a and b using either recursion or iteration
    Precondition: a and b are positive integers, function can ONLY be values 1 or 2
    Postcondition: Returns the greatest common denominator of numbers a and b using specified method   
    """
    print('Select the GCD function to use: \n \n1. Recursive \n2. Iterative\n')
    function = int(input('Please select a function: '))
    a = int(input('\nPlease enter the first number: '))
    b = int(input('Please enter the second number: '))
    if (function == 1):
        print('\nThe greatest common denominator is', gcd_rec(a,b))
    else:
        print('\nThe greatest common denominator is', gcd_iter(a,b))
        
          
if __name__ == "__main__":
    test_gcd_rec()
    test_gcd_iter()
    main()
    
