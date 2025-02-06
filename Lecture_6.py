#Finding square root of a number using bisection search:

x = 54321
epsilon = 0.01
n = 0

low = 0
high = x
guess = (low+high)/2
increment = 0.0001
while abs(guess**2-x)>=epsilon :
    if guess**2<x:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2
    n += 1
print(f"No.of guesses: {n}")
print(f"square root of {x} is close to {guess}")

#The optimised program so that it could handle values between 0 and 1.

x = 0.5
epsilon = 0.01
n = 0
if x>= 1:
    low = 1
    high = x
else:
    low = x
    high = 1
guess = (low+high)/2
while abs(guess**2-x)>=epsilon :
    if guess**2<x:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2
    n += 1
print(f"No.of guesses: {n}")
print(f"square root of {x} is close to {guess}")

#Bisection search algorithm to find cube root of a positive  cube

cube = 27
epsilon = 0.01
n=0
if cube>=1:
    low = 1
    high = cube
else:
    high = 1
    low = cube
guess = (high + low)/2
while abs(guess**3- cube) > epsilon:
    if guess**3>cube:
        high = guess
    else:
        low = guess
    n+= 1
    guess = (high + low) / 2
print(f"No.of guesses: {n}")
print(f"cube root of {cube} is close to {guess}")

#Finding square root of polynomial using Newton Raphson method
#p(x) = x^2 - k
#p'(x) = 2x
#better guess is g - (g^2 - k)/2g

epsilon = 0.01
k = 54321
guess = 24/2.0
n=0
while abs(guess**2-k)>=epsilon:
    n+=1
    guess -= (guess**2-k)/(2*guess)
print(f"No.of guesses: {n}")
print(f"square root of {k} is {guess}")