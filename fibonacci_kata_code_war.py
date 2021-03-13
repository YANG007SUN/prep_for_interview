# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python

# ============================
# fib positive n by iteration
# ============================

def fib(n):
    """Calculates the nth Fibonacci number"""
    if n==0: return 0
    if n==1 or n==2: return 1
    n_2, n_1, temp = 0,1,1
    for _ in range(abs(n)-1):
        temp = n_2+n_1
        n_2, n_1 = n_1, temp
    if n>0:
        return temp
    elif n%2==0:
        return -temp
    else:
        return temp


# ============================
# fib positive n by recursion
# ============================

def fib(n):
    """n is positive #
    """
    if n==0: return 0
    if n==1 or n==2: return 1
    return fib(n-2) + fib(n-1)

