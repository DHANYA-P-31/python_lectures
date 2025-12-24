def find_grades(grades, student):
    """
    :param grades: dict mapping student name to grades
    :param student: List of student name
    :return: A list containing the grades in same order as student
    """
    grade_list = []
    for s in student:
        grade_list.append(grades[s])
    return grade_list

d = {"Dhan":'A',"John":"B","Doe":"B"}
print(find_grades(d,["Dhan","Doe"]))

def find_in_L(Ld, k):
    """

    :param Ld: list of dicts
    :param k: int
    :return: True if k is a key in any dicts of Ld and False otherwise
    """
    for d in Ld:
        if k in d:
            return True
    return False

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
print(find_in_L([d1, d2, d3], 2))
print(find_in_L([d1, d2, d3], 25))

def count_matches(d):
    """

    :param d: dict
    :return: how many entries in d have the key equal to its values
    """
    count = 0
    for k,v in dict.items(d):
        if k == v:
            count += 1
    return count

print(count_matches(d1))
d = {1:2, 'a':'a', 5:5}
print(count_matches(d))

my_d = {'Ana':{'mq':[10], 'ps':[10,10]},
        'Bob':{'ps':[7,8], 'mq':[8]},
        'Eric':{'mq':[3], 'ps':[0]}
        }

def get_average(data, what):
    all_data = []
    for stud in data.keys():
        all_data+=data[stud][what]
    return sum(all_data)/len(all_data)

print(get_average(my_d, 'mq'))

