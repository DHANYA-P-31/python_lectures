#Is even function with return

def is_even_with_return( n ):
    """

    :param n: Positive integer
    :return: Bool True if n is even else false
    """
    return n%2 == 0

# Is even function without return

def is_even_without_return(n):
    """

    :param n: Positive integer
    :return: None
    """
    print( f"{ n} is even?{n % 2 == 0}")

print(f"6 is even?{is_even_with_return(6)}")
print(f"87 is even?{is_even_with_return(87)}")

print("Without return")

print(is_even_without_return(9))#This will print None
print(is_even_without_return(62))#This will print None
is_even_without_return(52) #This is the way to call function without return value

def add(x,y):
    return x+y

def mult(x,y):
    print(x*y)

add(1,2) #This line is replaced by 3, doesn't display anything
print(add(2,3))# Displays 5
mult(3,4) #Displays 12
print(mult(4,5)) # print None after printing 20 in function


def is_triangular(n):
    """
    Checks whether n is triangular
    :param n: n is a positive integer
    :return: True if n is triangular(i.e. Equals a continuous summation of natural number)
            False if n is not triangular
    """
    total = 0
    for i in range(n):
        total += i
        if total == n:
            return True
    return False

print(f"is 6 triangular?{is_triangular(6)}")
print(f"is 5 triangular?{is_triangular(5)}")

def bisection_search_square_root(x):
    """
    Evaluates square root by using bisection search method
    :param x: x is an integer
    :return: square root of the x
    """
    epsilon = 0.01
    n = 0
    if x >= 1:
        low = 1
        high = x
    else:
        low = x
        high = 1
    guess = (low + high) / 2
    while abs(guess ** 2 - x) >= epsilon:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
        n += 1
    return guess

print(f"square root of 6 is close to {bisection_search_square_root(6)}")

def count(n,epsilon):
    """
    Count how many integers have square root within the range
    :param n: a positive int greater than 2
    :param epsilon: a positive number less than 1
    :return: no.of integers have square root within the range
    """
    countsquares = 0
    for i in range(n**3):
        sqrt = bisection_search_square_root(i)
        if abs(n - sqrt)<epsilon:
            print(i, sqrt)
            countsquares += 1
    return countsquares

print(count(15,0.1))

def f(x): #Here x formal parameter
    x += 1
    print("in f(x) x = ",x)
    return x

x = 3
z = f(x) #Actual parameter
print(f"In main x = {x} ,f(x) = {z}")

# Function as parameter

def calc(op , x, y):
    return op(x,y)

def add(x,y):
    return x + y

def div(x,y):
    if y!= 0:
        return x/y
    print("Denominator cannot be 0")

def mult(x,y):
    return x*y

print(calc(add,6,8))
print(calc(mult,6,8))
print(calc(div,6,8))

res = calc(div,2,0)#prints Denominator cannot be 0 and returns None
print(res)

def func_a():
    print("Inside func_a")

def func_b(y):
    print("Inside func_b")
    return y

def func_c(f,z):
    print("Inside func_c")
    return f(z)

print(func_a())#None
print(5 + func_b(2))#7
print(func_c(func_b,3))#3

def apply(criteria,n):
    """
    Function to count how many ints from 0 to n (inclusive)satisfies the criteria
    :param criteria: function
    :param n: inclusive upper bound n>0
    :return: how many ints from 0 to n (inclusive)satisfies the criteria
    """
    count = 0
    for i in range(n+1):
        if criteria(i):
            count += 1
    return count

def is_even(x):
    return  x%2 == 0

print(apply(is_even,8))