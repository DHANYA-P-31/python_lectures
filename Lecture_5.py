#converting decimal into binary

x = 0.625

p =0
while((2**p)*x)%1 != 0:
    print("Remainder ="+ str((2**p)*x -int((2**p)*x )))
    p+=1

num = int(x*(2**p))

result = ""
if num == 0:
    result = "0"
while num>0:
    result = str(num%2) + result
    num //= 2

for i in range(p - len(result)):
    result = "0" + result

result = result[0:-p] + "." + result[-p:]

print(f"The binary representation of {x} is {result}")

x = 0
for i in range(10):
    x += 0.125
print(x == 1.25)#true

x = 0
for i in range(10):
    x += 0.1
print(x == 1)#False

#Square root using guess and check

x = 36
epsilon = 0.01
n = 0
guess = 0
increment = 0.0001
while abs(guess**2-x)>=epsilon:
    guess += increment
    n += 1
print(f"No.of guesses: {n}")
print(f"square root of {x} is close to {guess}")

# x = 54321
# epsilon = 0.01
# n = 0
# guess = 0
# increment = 0.0001
# while abs(guess**2-x)>=epsilon:
#     guess += increment
#     n += 1
#     if n%10000 == 0:
#         print(f"Current guess:{guess}")
#         print(f"Difference between guess^2 and number: {abs(guess**2-x)}")
#     if n % 100000 == 0:
#         input("Continue?")
# print(f"No.of guesses: {n}")
# print(f"square root of {x} is close to {guess}")

x = 54321
epsilon = 0.01
n = 0
guess = 0
increment = 0.0001
while abs(guess**2-x)>=epsilon and guess**2<= x:
    guess += increment
    n += 1
print(f"No.of guesses: {n}")
if abs(guess**2-x)>=epsilon:
    print("Cannot find square root of", x)
    print("Last guess was ", guess, 'and its square', guess**2)
else:
    print(f"square root of {x} is close to {guess}")

