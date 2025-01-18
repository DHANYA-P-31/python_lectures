# type() is the keyword which returns type of the object

print(type(4))#int
print(type(3.0))#Float
print(type(False))#Bool

#Conversion of one type to another is called casting

print(type(float(3)))#convert int to float
print(type(int(3.9)))#convert float to int
print(type(round(3.9)))#convert float to int by rounding off

#Expression has value and type

print(5/2) # The value of expression is 2.5
print(type(5/2)) # the type of expression is float

#In expression if one object is float then the value will have type float

#Variable is bound to one value at a time

a=5

#By assigning variables to values we could reuse it and it improves the readability of program
#We can also rebind variable

print(a)#Now the value is 5

a=10

print(a) #  Now the value becomes 10

meters = 100 #Here value of meters is 100
feet = 3.2808*meters # here the value of meters is 100 and that of feet is 328.08
meters = 200 # here the meters is rebound to value 200

#Program to swap values of variables

a=5
b=10
print(a,b)
#The initial values of a and b are 5 and 10 respectively
temp = a
a = b
b = temp
print(a,b)
#Now the values of a and b are interchanged and a = 10 and b = 5