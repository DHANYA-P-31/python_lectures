# Exception and Assertions

# sum digits with exception handling

def sum_digits(s):
    '''
    add the digits in the string s
    :param s: a string
    :return: integer sun of digits in s
    '''
    total = 0
    for char in s:
        try:
            total += int(char)
        except:
            print("cant Convert",char)
    return total

print(sum_digits("123d5205h"))

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
except ValueError:
    print("cant Convert")
except ZeroDivisionError:
    print("Cant divide by zero")
except:
    print("Something went wrong")

def pairwise_division(a, b):
    '''
    a and b are lists of equal length divide each element of list a  by list b and return the list
    :param a: a list of integers
    :param b: a list of integers with equal length as a
    :return: list of pair wise divided integer
    '''
    ans = []
    for i in range(len(a)):
        try:
            d = a[i]/b[i]
            ans.append(d)
        except:
            raise ZeroDivisionError("Cant Divide",a[i],b[i])
    return ans
print(pairwise_division([12,4,55],[2,1,5]))

def sum_digit_assert(s):
    '''
        add the digits in the string s
        :param s: a string
        :return: integer sun of digits in s
    '''
    assert len(s) != 0,"S is empty"

    total = 0
    for char in s:
        try:
            total += int(char)
        except:
            print("cant Convert", char)
    return total

# print(sum_digit_assert(""))

def pairwise_division_assert(a, b):
    '''
    a and b are lists of equal length divide each element of list a  by list b and return the list
    :param a: a list of integers
    :param b: a list of integers with equal length as a
    :return: list of pair wise divided integer
    '''
    assert len(a) == len(b),"Lists are of equal length cant do pairwise division"
    ans = []
    for i in range(len(a)):
        try:
            d = a[i]/b[i]
            ans.append(d)
        except:
            raise ZeroDivisionError("Cant Divide",a[i],b[i])
    return ans
# print(pairwise_division_assert([12,4,55],[2,1]))