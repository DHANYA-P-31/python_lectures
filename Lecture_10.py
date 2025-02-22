L = [2,4,8]
print(L)
L.append(9)
print(L)

L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1+L2  #L4 = ['re','mi']
L3.append(L4)  #L3 =['do',['re','mi']]
L = L1.append(L3) #L1 = ['re',['do',['re','mi']]], L = None

def make_ordered_list(n):
    """
    :param n: positive integer
    :return: List containing ordered elements from 0 to n
    """
    L = []
    for i in range(0,n+1):
        L.append(i)
    return L

print("ordered list")
L1 = make_ordered_list(5)
print(L1)

def remove_elem(L, e):
    """
    Removes element e from list
    :param L: L is a list
    :param e: An element in list
    :return: new list without e
    """
    L1 = []
    for i in L:
        if i != e:
            L1.append(i)
    return L1

print("removing element from list")
L = [1,2,2,2,3]
print(remove_elem(L,2))

print("splitting sentence to list of words")
s = "Hello World "
List = s.split()
print(List)

print("List to string")
str = " ".join(List)
print(str)

def count_words(sen):
    """
    Count the number of words in a sentence
    :param sen: string representing a sentence
    :return: No. of words in the sentence
    """
    word_list = sen.split()
    return len(word_list)

print("counting words in sentence:'Hello there How are you?'")
print(count_words("Hello there How are you?"))

def sort_words(sen):
    """
    Sort the words in sentence in alphabetical order
    :param sen: A string that is a sentence
    :return: List containing of sorted elements
    """
    words_list = sen.split()
    words_list.sort()
    return words_list

print("sentence:'look at this photograph' to list ofv sorted words")
print(sort_words("look at this photograph"))

def square_list(L):
    """
    Square each element in the list
    :param L: A list of integers
    :return: A mutated lists which contains square of each element in the list
    """
    for i in range(len(L)):
        L[i] = L[i]**2
    return L

print("squaring each element in list:[1,3,5,9]")
print(square_list([1,3,5,9]))

L = [1,2,3,4]
print("tricky example 1")
for i in range(len(L)):
    L.append(i)
    print(L)

#infinite loop
# print("tricky example 2")
# L = [1,2,3,4]
# i = 0
# for e in L:
#     L.append(i)
#     i+=1
#     print(L)

#extend is used to add more than one element at the end of the list

print("tricky example 3")
L1 = [1,6,9]
L1.extend([0,7])
print(L1)

L = [1,2,3,4]
print("tricky example 4")
for e in L:
    L = L+L
    print(L)

print("After clearing")
L.clear()
print(L)