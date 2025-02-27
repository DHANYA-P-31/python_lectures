import copy


def remove_all(L,e):
    """
    mutates list L so that it removes all occurrences of e
    :param L: L is a list
    :param e: an element in list
    :return: None
    """
    l_copy=L[:]
    L.clear()
    for i in l_copy:
        if i != e:
            L.append(i)

L = [1,2,2,6,3,7]
remove_all(L,2)
print(L)

def remove_all2(L,e):
    """
    mutates list L so that it removes all occurrences of e
    :param L: L is a list
    :param e: an element in list
    :return: None
    """
    while e in L:
        L.remove(e)
        
L = [1,2,2,6,3,7]
remove_all(L,2)
print(L)

#tricky example - 4

def remove_dups(L1,L2):
    """
    Removes element from list 1 if the same element is present in list2
    :param L1:A list in which the elements to be removed
    :param L2: A list from which duplicates are checked
    :return:  None
    """
    l1_copy = L1[:]
    for e in l1_copy:
        if e in L2:
            L1.remove(e)

L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
remove_dups(L1,L2)
print("After removing duplicates")
print("L1=",L1)
print("L2=",L2)

old_list = [[1,2],[3,4],[5,'foo']]
new_list = old_list

new_list[1][1] = 6

print("New list ",new_list)
print("Old list ",old_list)

#changing the copy is also changing the original lis

old_list = [[1,2],[3,4],[5,6]]
new_list = copy.copy(old_list)
# shallow copy the list

old_list.append([7,8])
old_list[1][1] = 9
print("New list ",new_list)
print("Old list ",old_list)

old_list = [[1,2],[3,4],[5,6]]
new_list = copy.deepcopy(old_list)
# deep copy the list
# Creates new object

old_list.append([7,8])
old_list[1][1] = 9
print("New list ",new_list)
print("Old list ",old_list)
