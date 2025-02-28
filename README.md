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

## Lecture_10

### List

Lists are indexable ordered sequence of objects, they are usually homogenous(i.e. consists of elements of similar data type).
Denoted by Square brackets, Lists are mutable(we can change the element values in list).

### Operations on list

**append** - Adds an element to the end of the list L.append(element), It returns None

**Concatenation** - concatenation is done by + operator 
        
     L1 = [1,2]
     L2 = [6,3]
     L3 = L1+L2 # L3 = [1,2,6,3]

**split** - Every word in string s can be converted into List of words by using a function split()

**join** - Converts list to string (Syntax ''.join(L)), inside '' we could give the separator.

**sort** - Sort the elements in the list l.sort(), it mutates the list

**reverse** - Reverse the elements in list l.reverse(), it mutates the list

**sorted** - returns a sorted version of the list New_list = sorted(list), Here no mutation takes place

**extend** - add elements to end of the list

**clear** - clear is used to remove all elements from list

## Lecture_11

**Copying the list** L_copy = L[:]

**remove** 

1. Delete element at specific index - del(L[index])
2. Remove element at the end of the list L.pop()
3. Remove a specific element L.remove(element), If the element has multiple occurrence removes the first occurrence, if it s not in list gives error

**Aliasing**

Pointing the same object using various names.

**Shallow copy**

Syntax : new_list = copy.copy(old_list)

In shallow copy mutating the old list will also mutate the new list,
 but appending a new element to the list will not affect the copied list.

    old_list = [[1,2],[3,4],[5,6]]
    new_list = copy.copy(old_list)
    old_list.append([7,8])
    old_list[1][1] = 9

Now, New list  [[1, 2], [3, 9], [5, 6]] Old list  [[1, 2], [3, 9], [5, 6], [7, 8]]

**Deep copy**

Syntax : new_list = copy.deepcopy(old_list)

It creates a new object which is the copy of now existing object, 
then after the changes in old list will not affect the new list.

    old_list = [[1,2],[3,4],[5,6]]
    new_list = copy.deepcopy(old_list)
    old_list.append([7,8])
    old_list[1][1] = 9

Now, New list  [[1, 2], [3, 4], [5, 6]], Old list  [[1, 2], [3, 9], [5, 6], [7, 8]]

## Lecture 11

### List comprehension

Creates a new list, Applies a function to every element of another iterable that satisfies the condition.

    Syntax : [expression for element in iterable if test]

### Keyword parameters

It is also known as default parameter. In a function the parameter can be set to a default value.
When the function is called without the parameter it would set that to default value and if the parameter is given
to the function the value changes. Default parameter must go at the end in function call.

### Testing

#### Classes of Tests

**Unit Testing**

Validate each piece of program, testing each function separately

**Regression Testing**

Add tests for bugs as you find them, Catch introduced errors that were previously fixed

**Integration Testing**

Does overall program works.

### Black box technique

Designed without looking at the code.
Testing can be reused if the implementation changes.
Build test case in natural space partitions.
Also consider the boundary conditions.

### Glass box testing

Use code directly to guide design of test case.
Called path complete if every potential path through code is tested at least once.
It has some drawbacks like can go through the loops arbitrarily many times, missing paths.

### Debugging

Once we have discovered the code doesn't run properly then we want to

1. Isolate the bug
2. Eradicate the bug
3. Retest until all the test cases run correctly
4. Steep learning curve

### Certain error messages

IndexError - trying to access beyond the limits of list

TypeError - Trying to convert an inappropriate time

NameError - Referencing a non existent variable

SyntaxError - error in the syntax of the code

#### Using print statements

Use print statement at Enter function, Parameters, Return result of functions.
Print at the halfway in code and based on values decide where bug may be present.