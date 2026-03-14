#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    This function calculates the factorial of a given non-negative integer
    using recursion. The factorial of a number n is the product of all
    positive integers from 1 to n. For example, 5! = 5 × 4 × 3 × 2 × 1.

    Parameters:
    n (int): A non-negative integer whose factorial will be calculated.

    Returns:
    int: The factorial value of the input number n.
    """
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)