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

## Lecture 6 Notes

### Bisection Search

It is applied to the problem with an inherent order to the range of possible answers.

1.Suppose we know that the answer is within certain interval, then guess the midpoint of the interval.

2.If not answer check if answer is greater than or less than midpoint.

3.Change Interval and then Repeat

Bisection Search is a logarithmic algorithm. Process cuts the set of things in half at each step.
Exhaustive algorithm is linear, and bisection search which is logarithmic is better than linear.

Search spaces gets smaller quickly at the beginning and then more slowly later.

### Newton Raphson algorithm

Algorithm to find roots of a polynomial.
If p(x) is a polynomial.
As of Newton Raphson Algorithm if g is an approximation to root, then g-p(g)/p'(g) is better approximation.

### Decomposition and abstraction

Decomposition - The program is divided into self containing parts and can be combined to solve the problem.

Abstraction - Ignore the unnecessary details, used to separate what something does and how does it do.

## Lecture 7

### Functions:

Defining the functions allocates memory for function. Function is only used when it is called.
Same function can be called numerous times.

### Function Characteristics

Name -  Variable bound to function argument

Parameters - The inputs

docstring - Provides the specification of function

body - set of instructions to execute when the function is called.

return value - Return the result of function

1. keyword for creating function - def
2. Keyword for returning output - return

As soon as function is called formal parameters in the function get replaced with the values from function call.
Python executes expression in the body of the function

The function call is replaced by return value. If there is no return value python returns None.

## Lecture_8

### return

1. return used inside function only 
2. Only one return value is executed for a function
3. Codes after return will not be executed in the function
4. Value associated with return is given to the function call

### print

1. print can be used inside and outside the function call
2. Multiple print statement can be executed
3. Line of codes after print statement will be executed
4. Values inside the print is outputted to the console

print is a function which returns None.

### Function Calls

1. It creates a new environment inside the function call
2. Like a mini program that it needs to complete
3. The mini program runs with assigning its parameters to some inputs
4. It executes the part of the body
5. It returns a value
6. The environment disappears after returning the value

### Environment

Global environment - where user interacts with python interpreter, where the program starts

Invoking a function creates new environment.

### Scope

Formal parameters get bound to the value of input parameters .
Scope is a mapping of name to object, defines context in which the value is evaluated.
Expressions in body of function evaluated with respect to this new scope

### Functions as Objects

Functions are also first class Objects
1. They have a type
2. They can be assigned to a value bound to name
3. They can be used as argument to another function
4. Function can be returned by other object

## Lecture_9

### Lambda function

Lambda function creates a procedure or function but simply does not bind a name to it.
Lambda function creates an anonymous function, and is useful when function is used only once .

### Tuples

Tuple is a compound data type and is immutable.
Tuples are indexable ordered sequence of object.
Syntax to create a tuple object is ().
Tuple elements can be of different datatypes.

    tuple_ex = (1,"Hello",6.5)

Square bracket is used to  grab element at a particular index.
Tuple is used to return more than one value from a function.

**Variable number of arguments**

Python allows a function to take variable  number of arguments using * notation. 
Numbers are stored a tuple.

### List

Lists are indexable ordered sequence of objects, they are usually homogenous(i.e. consists of elements of similar data type).
Denoted by Square brackets, Lists are mutable(we can change the element values in list).