#Iteration While loop

#The problem in which you are lost in a forest if you are going right
# and would get out of the forest if you go left

direction = input("You are lost in forest,Where to go? Left or Right?").lower()
while direction == "right":
    direction = input("You are lost in forest,Where to go? Left or Right?").lower()
print("You got out of the forest")

#Example 2 Displays all the positive numbers lower than the given number

n = int(input("Enter a positive number:"))

while n>0:
    print(n)
    n -= 1

#An example of infinite loop

# while True:
#     print("Hello")

# The example 1 is modified such that when the loop is repeated more than 2 times display sad face

count = 0
direction = input("You are lost in forest,Where to go? Left or Right?").lower()
while direction == "right":
    count += 1
    if count>2:
        print(":( ")
    direction = input("You are lost in forest,Where to go? Left or Right?").lower()

print("You got out of the forest")

#finding factorial using while loop

x = int(input("Enter the number to find factorial: "))
i = factorial = 1
while i<= x:
    factorial *=i
    i += 1
print(f"The factorial of {x} is {factorial}")

#Example 2 using for loop

n = int(input("Enter a positive number:"))

for j in range(n):
    print(i)

for i in range(1,4,1):
    print(i)
#displays 1 2 3

for j in range(1,4,2):
    print(j*2)
#displays 2 6

for me in range(4,0,-1):
    print("$"*me)
# $$$$
# $$$
# $$
# $

#Add all the values less than a number

sum = 0
for i in range(10):
    sum+=i
print(sum)

#Find sum of numbers between two numbers including both

sum = 0
a=8
b=11
for i in range(8,12):
    sum+= i
print(sum)

#Factorial using for loop

x = int(input("Enter the number to find factorial: "))
factorial = 1
for i in range(1,x+1):
    factorial *=i
print(f"The factorial of {x} is {factorial}")
