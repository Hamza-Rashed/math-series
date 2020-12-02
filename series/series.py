# function fibonacci
def fibonacci(n):
    """
    is a numeric series starting with the integers 0 and 1. In this series, 
    the next integer is determined by summing the previous two. This gives us:
    """
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

# function lucas
def lucas(n):
    """
    The Lucas Numbers are a related series of integers that start with 
    the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
    """
    if n == 1:
        return 1
    if n == 0:
        return 2  
    return lucas(n-1) + lucas(n-2)

# function sum_series
def sum_series(n,first_num=0,second_num=1):

    """
   this function take one required parameter and two optional parameters.
   The required parameter will determine which element in the series to print. 
   The two optional parameters will have default values of 0 and 1 and will 
   determine the first two values for the series to be produced.
    """

    if first_num == 2 and second_num == 1:
        return lucas(n)
    elif first_num == 0 and second_num == 1:
        return fibonacci(n)
    else:
        return fibonacci(n) + lucas(first_num)
