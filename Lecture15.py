def mult_rec(a,b):
    if b == 1:
        return a
    else:
        return a+mult_rec(a,b-1)

print(mult_rec(2,3))

def power_recur(n,p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n*power_recur(n,p-1)
print(power_recur(2,3))

def fact_recur(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact_recur(n-1)

print(fact_recur(6))