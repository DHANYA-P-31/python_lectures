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

#Using lambda function

print("no.of even numbers between 0 to 10",apply(lambda x:x%2==0,10))

#Outout for following code

def do_twice(n,fn):
    return fn(fn(n))

print(do_twice(3,lambda x:x**2))#prints 81

tuple_ex = (1,"Hello",6.5,(5,6))
print(len(tuple_ex))
print(tuple_ex)

for ex in tuple_ex:
    print(ex)

#Tuple return more than one value from a function

def division(x,y):
    """
    The function performs division and returns quotient and remainder
    :param x:  A positive integer , dividend
    :param y: A positive integer, divisor
    :return: quotient and remainder in form of tuple
    """
    q = x//y
    r = x%y
    return (q,r)
(quotient, remainder)= division(10,3)

print(f"quotient = {quotient}, remainder = {remainder}")

def char_count(s):
    """
    Counts the number of vowels and consonants in s
    :param s: A string of lower case letters
    :return: tuple - first element - no.of vowels, second element - no.of consonants
    """

    (v ,c) =(0,0)
    for i in s :
        if i in "aeiou":
            v+=1
        else:
            c+= 1
    return (v,c)

print(char_count("hello"))

def add(*args):
    sum = 0
    for i in args:
        sum+= i
    return sum

print(add(4,8,6,0,5,7))
print(add(7,0,4))

def list_sum(L):
    """
    Adds all the elements in the list
    :param L: A List of numbers
    :return: sum of all elements in list
    """
    sum = 0
    for i in L:
        sum+=i
    return sum

print(list_sum([1,9,6,8]))

def sum_product(L):
    """
    Adds all elements in List, Multiplies all elements in list.
    :param L: A list on numbers
    :return: Tuple first element sum of all numbers in list, second element product of all elements in list
    """

    (sum,product) = (0,1)

    for i in L:
        sum+=i
        product*=i

    return (sum,product)

ans = sum_product([6,9,4,2,1])

print(f"Sum = {ans[0]}, product = {ans[1]}")
