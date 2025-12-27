def fib(x):
    if x==1 or x ==2:
        return 1
    else:
        return fib(x-1)+fib(x-2)

print(fib(6))

## Fibonacci with memoization

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
d = {1:1, 2:1}
print(fib_efficient(6, d))

def score_count(x):
    """
    Returns all the ways to make a score of x by adding 1,2, and/or 3 together.
    Order doesn't matter.
    """
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    else:
        return score_count(x-1) + score_count(x-2) + score_count(x-3)

print(score_count(4))

def total_recur(L):
    if L == []:
        return 0
    elif len(L) == 1:
        return L[0]
    else:
        return L[0] + total_recur(L[1:])
print(total_recur([30,40,50]))

def total_len_recur(L):
    if L == []:
        return 0
    elif len(L) == 1:
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(L[1:])

print(total_len_recur(["ab","c","def"]))

# Is an element im the list

def in_list(L,e):
    if L == []:
        return False
    elif L[0] == e:
        return True
    else:
        return in_list(L[1:], e)

print(in_list(["ab","c","def"],"c"))

def flatten(L):
    if len(L) == 0:
        return L
    elif len(L) == 1:
        return L[0]
    else:
        return L[0]+flatten(L[1:])

print(flatten([[1,2,3],[2,6],[8,10]]))

def is_in_list(L, e):
    if L == []:
        return False
    else:
        return in_list(flatten(L), e)

print(is_in_list([[1,2,3],[2,6],[8,10]],5))

def rev_list(L):
    if L == []:
        return []
    elif len(L) == 1:
        return L
    else:
        return rev_list(L[1:])+[L[0]]

print(rev_list([1,2,3]))

def my_rev(L):
    if L == []:
        return L
    elif len(L) == 1:
        if type(L[0]) is list:
            return [my_rev(L[0])]
        else:
            return L
    else:
        if type(L[0]) is list:
            return my_rev(L[1:])+[my_rev(L[0])]
        else:
            return my_rev(L[1:])+[L[0]]

print(my_rev([[1,2],3, [4], [7,9]]))
