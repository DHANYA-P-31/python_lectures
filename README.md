# python_lectures
 Notes from Introduction to programming using Python by Ana Bell.

## Lecture_1 notes
   ### Objects 

   Objects have a type and defines the kinds of things programs can do to them.
   Syntax to know the datatype of objects type(Object) .

   #### Scalar Objects:

   These are the primitive data objects.

      1. int - represent integers (1,2,3,-1)
      2. float - represent real numbers (1.2, 3.6)
      3. bool - represent Boolean ( True or False)
      4. NoneType - has only one value None

   #### Non-scalar objects:

   Have Internal structures that can be accessed.

      1. Lists
      2. Dictionary
      3. Sequence of Characters

   ### Type Casting

   Conversion of one datatype to another.

      1. float() - converts to float
      2. int() - converts to int
      3. round() - implicit function to convert to int by rounding off

   ### Expression

   Objects and operators combined to form expression.
      Expression has a value and type .

         1. 5+2 , has value 7 and type int
         2. 5/2 , has value 2.5 and type float

   In expression if one object is float then the value will have type float.

   ### Variables 

   In computer science the variable is bound to single value at a time whereas in maths it could have multiple values.
   By assigning variables to values we could reuse it, and it improves the readability of program.
   The value of variable can also be rebounded.
   
## Lecture_2 Notes

### Strings

Sequence of case-sensitive characters(Letters, Special characters, spaces, digits).
Enclose in quotation marks or single quotes.

    a = "Hello" 
    b = 'Hello'

**Concatenation** refers to joining two or more string objects together to form new object.
It can be done using '+' operator.

**Repeating Strings** is done using '*' operators .
It works only between String and number.

    c = a+b
    d = a*3

here c is HelloHello, and d is HelloHelloHello.

len() function is used to retrieve the length of String inside the parentheses.

### Slicing and Substrings

Grabbing of individual characters at different position.
We use square brackets to do this python.

    s = "abc"
    s[0] is "a"
    s[1] is "b"

Indexing starts from 0 in python.
Python also has negative indexing.

    s[-1] = "c"
    s[-2] = "b"

Slicing can be done to get **SubStrings**

Syntax: *String[start:stop:step]*

It gets characters from start to stop - 1 taking every step characters.
If step is not given the default step is 1.
Positive steps means go left to right whereas negative step means go right to left.

**Strings are immutable Objects**.
We could only create the objects which are the versions of original one.

### Printing

Command to display is *print()*.
By separating the objects using , we could print multiple objects.
Concatenation is done for same objects only.

    print("hello")
    print(a,b,c)

### Getting input

Command is *input()*.
Inside the parentheses the prompt is given.
We usually need to store the input in variable and the input is saved as string.

    a = input("Enter Something")

Numbers are also stored as strings thus TypeCasting is required

### Newton's Algorithm

It is used to find roots of the polynomial .
Algorithm uses Successive approximation .
    next_guess = guess - f(guess)/ f'(guess).

### F string

F string is the formatted string referral Expressions are bracketed using curly braces {}.
Expressions in {} are calculated during run time and automatically converts to string and then concatenate.

    n = 3
    m = 4
    print(f"The result is {n*m}")

### Branching 

In Cs there are two notions '='  
    a = b assigning
    a == b checking equality and return bool

Certain comparisons to return bool

    i>j     i<j
    i>=j    i<=j
    i==j    i!=j

Logical Operators

    not a (negation)
    a and b (True only when both are True)
    a or b (False only when both are False)

**If-Else**

Check condition and performs the block only if condition is true

    if <condition>:
        <code>
        <code>
    elif <condition>:
        <code>
        <code>
    else:
        <code>
        <code>

First block where the condition is true is performed, when all conditions in if block is false else block performed

***Indentation matters in python***

## Lecture 3 notes

### Iteration
**While Loop**
loops as long as condition is true

    while <condition>:
        <code>
        <code>

The while loop repeats all the statements inside the block until the condition becomes False. While loop can repeat the blocks of code indefinitely

**For Loop**

For loop is used to iterate through a number in sequence, element of string
    
    for <variable> in <sequence>:
        <code>

**Range**

start:First int generated,
stop : goes upto but not including,
step : generates in the steps of.

    range(start,stop,step)

## Lecture 4 Notes

**break Statement**

Immediately exits the innermost loop it is in, skips the remaining expressions in block of code.

### Guess and check 

The process is called exhaustive enumeration. 
This is applied to a problem where we were able to guess a solution to the problem
and to check whether the solution is correct.
We could keep guessing until a solution is found or guessed all values.

### Floating point implementation:

Operations on some floats can have a small error and 
the small error will have big effect if operations are done many times.
The implementation of float depends on computer hardware and not on the programming language.
The hardware is implemented using binary.
We enter the inputs in decimal and computer converts it to binary

## Lecture 5 Notes

### Fraction

Real numbers are converted to int by multiplying real number with 
 multiple of 2 , Sometimes when there is no such power of 2 approximation is done.

Floating point digits are represented by pair of integers .(significant digit and base 2 exponent)

    (1,1) = 1*2^1
    (1,-1) = 1*2^-1

Never use == to check float.
Instead, use approximation method.

### Approximation method

By approximation method the answer is close enough to the ideal answer.
Approximation algorithms have 2 parameters

    epsilon - how close we are to answer
    increment - how much to increase guess

Increasing epsilon - less accurate and faster program
Decreasing increment = more accurate and slower program