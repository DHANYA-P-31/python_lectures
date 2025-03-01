# List comprehension

def f(L):
    Lnew = []
    for e in L:
        Lnew.append(e**2)
    return Lnew

L=[1,2,3,4]
Lnew = f(L)
print(Lnew)

# Equivalent list comprehension
L_new = [e**2 for e in L]
print(L_new)

def g(L):
    Lnew = []
    for e in L:
        if e%2 == 0:
            Lnew.append(e**2)
    return Lnew

L=[1,2,3,4]
Lnew = g(L)
print(Lnew)

# Equivalent list comprehension
L_new = [e**2 for e in L if e%2 ==0]
print(L_new)

L_new = [e**2 for e in range(6) if e%2 ==0]
print(L_new)

L1=[len(x) for x in ['xy','abcd',7,'4.0'] if type(x) == str]
print(L1)#L1 = [2,4,3]

def square_root(x,epsilon = 0.01):
    """
    Evaluates square root by using bisection search method
    :param x: x is an integer
    :param epsilon: has default value of 0.01 and can be changed
    :return: square root of the x
    """
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

print(square_root(123))
print(square_root(123,0.05))

def prod(a):
    def g(b):
        return a*b
    return g

val = prod(3)(5)
print(val)

mult = prod(3)
val = mult(5)
print(val)

