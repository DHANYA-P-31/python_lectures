#Strings are case sensitive characters enclosed in ' ' or " "

a = "Hello"
b = 'world'

#Concatenate Strings

c = a + " " + b # This would be equal to c = 'Hello world'

#Repeat strings * operator is used

d = a * 3 #This is equal to d = 'HelloHelloHello'

len(d) #This function returns length of string d(i.e. 15)

#Slicing

s = "abc"
s[0] # a
s[1] # b
s[2] # c
#s[3] # Index out of bounds

s[-1] # c
s[-2] # b

#substrings

g="abcdef"
g[1:4:2] # It gives a substring 'bd'

s = "abcdefgh"

s[3:6] # def
s[3:6:2] # df
s[:] # abcdefgh
s[4:1:-2] #ec

#Printing and getting input

print("helloWorld")#displays helloWorld
word = input("Enter a word")# Gets the input from user and stores in word

num = input("Type a number") #Consider the input as 3
print(5*num) # displays 33333
num = int(input("Type a number:"))#Consider the input as 3
print(5*num) # displays 15

#Newton's method to find roots (g^3-x=0)

x = int(input("Enter a number to find cube root:"))
g = int(input("Enter a guess to start with:"))
print("The cube of current guess is:",g**3)
next_g = g - ((g**3-x)/(3*g**2))
print("The next guess is", next_g)

#F string

n = 3
m = 4

print(f"The result is {n*m}") #here the n*m is evaluated and type casted to string and then concatenated

#Branching

#equality
number = 3
guess = int(input("enter a number"))
print(number == guess)

num = 5
guess= int(input("Guess a number"))#Get the number from user
if num == guess:
    print("Both numbers are same") #If the numbers are same This block get performed
elif num>guess:
    print("Too low") #If the guess is less than num This block get performed
else:
    print("Too high") # if both the above conditions becomes false(i.eIf the guess is greater than num )This block get performed