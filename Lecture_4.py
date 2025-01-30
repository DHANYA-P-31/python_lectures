#Break statement

Sum = 0
for i in range(5, 11, 2):#i = 5, 7, 9
    Sum += i #Sum = 5
    if Sum == 5:
        break #Since the sum is 5 the loop terminates
        Sum +=1 # This line will not be executed
print(Sum) #Displays 5

#prints the no.of even numbers in range

even = 0
for i in range(5): #i = 0,1,2,3,4
    if i%2 == 0: #Condition is true for i = 0, 2, 4
        even += 1
print(even) #Displays 3

even = 0
for i in range(10): #i = 0,1,2,3,4,5,6,7,8,9
    if i%2 == 0: #Condition is true for i = 0, 2, 4, 6, 8
        even += 1
print(even) #Displays 5

even = 0
for i in range(2,9,3): #i = 2,5,8
    if i%2 == 0: #Condition is true for i = 2,8
        even += 1
print(even) #Displays 2

even = 0
for i in range(-4,6,2): #i = -4,-2,0,2,4
    if i%2 == 0: #Condition is true for i = -4,-2,0,2,4
        even += 1
print(even) #Displays 5

even = 0
for i in range(5,6): #i = 5
    if i%2 == 0: #Condition is false
        even += 1
print(even) #Displays 0

#Strings and loops
#Example 1 : To check if there is i or u in a string
#method 1 - uses range to iterate through index
s = "This is the string you want to check"
for i in range(len(s)):
    if s[i] == 'i' or s[i]  == 'u':
        print("There is i or u")

#method 2 - Iterates through character directly
for char in s:
    if char == 'i' or char =='u':
        print("There is i or u")

#method 3
for char in s:
    if char in 'iu':
        print("There is i or u")

#cheer leader robot example

an_letters = "aeiouAEIOUfhlmnrsFHLMNRS"
word = input("Enter a noun:")
times = int(input("Enthusiasm level(1-10):"))

for w in word:
    if w in an_letters:
        print(f"Give me an {w} : {w}")
    else:
        print(f"Give me an {w} : {w}")
print("What does it spell?")
for i in range(times):
    print(word,"!!!")

#Find no.of unique letters in strings

s = "ancdccaam"
w =""
count = 0
for char in s:
    if char not in w:
        count += 1
    w += char
print(count)

#Guess and check - square root

guess = 0
x = int(input("Enter a number:"))
while guess**2 < x:
    guess += 1

if guess**2 == x:
    print(f"Square root of {x} is {guess}")
else:
    print(f"{x} is not a perfect square number")

#Handling negative numbers

guess = 0
neg = False
x = int(input("Enter a number:"))
if x<0:
    neg = True
while guess**2 < x:
    guess += 1

if guess**2 == x:
    print(f"Square root of {x} is {guess}")
else:
    print(f"{x} is not a perfect square number")
    if neg == True:
        print(F"Did uou mean {-x}")

#Find the secret number

secret = 6

Found = False
for i in range(1,11):
    if i == secret:
        Found = True
        print(f"Found:{secret}")
        break
if Found == False:
    print("The number not in range 1 to 10")

#Guess and check cube root

x = int(input("Enter a number:"))
Flag = False
for i in range(abs(x)+1):
    if i**3 == abs(x):
        Flag = True
        if x< 0:
            i = - i
        print(f"Cube root of {x} is {i}")

if Flag == False:
    print(f"{x} is not a perfect cube number")

#Little faster code

x = int(input("Enter a number:"))
for i in range(abs(x)+1):
    if i**3 >= abs(x):
        break
if i**3 != abs(x):
    print(f"{x} is not a perfect cube number")
else:
    if x < 0:
        i = - i
    print(f"Cube root of {x} is {i}")

#Another word problem example
#Condition 1 Ben sell 2 tickets lesser than Alyssa
#Condition 2 Cindy sells twice as many as Alyssa
#Condition 3 10 Tickets total Find tickets sold by Alyssa

for alyssa in range(11):
    for ben in range(11):
        for cindy in range(11):
            con1 = (alyssa - ben == 2)
            con2 = (cindy == 2*alyssa)
            con3 = ((alyssa+cindy+ben) == 10)
            if (con2 and con1 and con3) == True:
                print(f"The no.of tickets sold by Alyssa {alyssa}")
                print(f"The no.of tickets sold by Ben {ben}")
                print(f"The no.of tickets sold by Cindy {cindy}")

#Decimal to Binary

num = 158
result = ''
if num ==0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num //=2
print(result)

#handling negative numbers

num = -167
if num < 0:
    neg = True
    num = abs(num)
else:
    neg = False
result = ''
if num ==0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num //=2
if neg:
    result = '-' + result
print(result)