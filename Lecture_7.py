# Function

def is_even(n):
    """
    :param n: n is a positive integer
    :return: Bool True if n is even , False if n is odd
    """
    return n%2 == 0

print(is_even(5))
print(is_even(62))

def div_by(n, d):
    """

    :param n: n is a positive integer
    :param d: d is another positive integer
    :return: Bool, True if d divides n , else return false
    """
    return n%d == 0

print(div_by(51,3))
print(div_by(6,4))

for i in range(1,10):
    if is_even(i):
        print(i, "Even")
    else:
        print(i, "Odd")

def sum_odd(a,b):
    """

    :param a: Lower limit for starting to sum the odd numbers
    :param b: Upper limit for ending to sum the odd numbers
    :return: Sum of odd numbers between a and b
    """
    ans = 0
    for j in range(a,b+1):
        if not is_even(j):
            ans += j
    return ans

print(sum_odd(1,9))