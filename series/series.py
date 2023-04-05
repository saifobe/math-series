def fibonacci(n):
    """
    Compute the nth Fibonacci number.

    A Fibonacci number is defined as the sum of its two preceding terms.
    The first two Fibonacci numbers are 0 and 1.

    Args:
        n (int): The index of the Fibonacci number to compute.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
        
    """
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Lucas function

def lucas(n):
    """
    Compute the nth Lucas number.

    A Lucas number is defined as the sum of its two preceding terms.
    The first two Lucas numbers are 2 and 1.

    Args:
        n (int): The index of the Lucas number to compute.

    Returns:
        int: The nth Lucas number.

    Raises:
        ValueError: If n is negative.


    """
    if n==0:
        return 2
    if n==1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

#sum function

def sum_series(n, first=0, second=1):
    """
    Prints the nth element in a series.

    Parameters:
    n (int): The index of the element to be printed.
    first (int): The first element in the series. Default value is 0.
    second (int): The second element in the series. Default value is 1.

    Returns:
    int: The nth element in the series.
    """
    if first == 0 and second == 1:
        return fibonacci(n)

    elif first == 2 and second == 1:
        return lucas(n)

    else:
        if n == 0:
            return first
        elif n == 1:
            return second
        else:
            return sum_series(n-1, first, second) + sum_series(n-2, first, second)