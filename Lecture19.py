class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return f'Animal {self.name if self.name is not None else ""} is {self.age} years old'

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name = ""):
        self.name = name

myanimal = Animal(2)
print(myanimal)

myanimal.set_name("Billy")
print(myanimal)

def animal_dict(L):
    d = {}
    for a in L:
        if type(a) == int and a>=0:
            d[a] = Animal(a)
    return d

def make_animal(L1, L2):
    L = []
    for i in range(len(L1)):
        age = L1[i]
        name = L2[i]
        a = Animal(age)
        a.set_name(name)
        L.append(a)
    return L

L = [2, 5, 'a', -5, 0]
d = animal_dict(L)
for k, v in d.items():
    print(k, v)

L1 = [2, 3, 4, 6, 9]
L2 = ['Tom', 'Billy', 'Rocky', 'Sky', 'Lucky']

L = make_animal(L1, L2)
for a in L:
    print(a)

class Cat(Animal):
    def speak(self):
        print("Meow")

    #Overidding methods
    def __str__(self):
        return f"Cat {self.name}: {self.age} years old"

c = Cat(5)
c.speak()
c.set_name("Fluffy")
print(c)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends.copy()

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def speak(self):
        print("Hello, my name is %s" % self.name)

    def age_difference(self, other):
        print(f"Age gap is: {abs(self.age - other.age)}")

    def __str__(self):
        return f"Person {self.name} is {self.age} years old"

p1 = Person("John", 20)
p2 = Person("Doe", 30)
print(p1)
print(p2)
p1.add_friend('Anna')
p1.add_friend('Bobby')
print(p1.get_friends())
p1.age_difference(p2)

def make_pets(d):
    for k, v in d.items():
        print(k.get_name()+ ":" + v.get_name())

d = {p1:c, p2:myanimal}
make_pets(d)

import random

class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("Hello, my name is %s" % self.name)
        elif 0.25 <= r < 0.5:
            print("I have homework")
        elif 0.5 <= r < 0.75:
            print("I am busy")
        else:
            print("I am not at home")

s1 = Student("John", 22, "CS")
for i in range(5):
    s1.speak()

class Rabbit(Animal):
    tag = 1
    def __init__(self, age,parent1= None, parent2= None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return self.rid

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __eq__(self, other):
        parents_same = (self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid)
        parent_opp = (self.parent1.rid == other.parent2.rid and self.parent2.rid == other.parent1.rid)
        return parents_same or parent_opp

r1 = Rabbit(20)
r2 = Rabbit(25)
r3 = Rabbit(5,r1,r2)
r4 = Rabbit(7,r2,r1)
print(r3==r4)