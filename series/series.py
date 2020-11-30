# function fibonacci
def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

# function lucas
def lucas(n):
    if n == 1:
        return 1
    if n == 0:
        return 2  
    return lucas(n-1) + lucas(n-2)

# function sum_series
def sum_series(n,first_num=0,second_num=1):

    if first_num == 2 and second_num == 1:
        return lucas(n)
    elif first_num == 0 and second_num == 1:
        return fibonacci(n)
    else:
        return fibonacci(n) + lucas(first_num)
