print(5//3)


from math import *
print(floor(4.99))

from random import *
print(random()) #0.0 ~1.0 미만의 임의이 값 생성
print(random()*10) #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) #0~10 미만
print(int(random()*10)+1) #1~10 이하의 임의의 값 생성

print(randrange(1,46)) #1~46미만의 값 생성

####
sentence3 = """
    i am  a man
    and python is easy
"""
print(sentence3)

#####
jumin ="940812-789012"
print("sex: "+jumin[7])
print("year : "+jumin[0:2])

##
python = "Python is Amazing"
print(python.replace("Python", "Java"))
index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java"))

print(python.count("n"))


#String format

#1
print("I am %d years old" %20)
print("I like %s" %"Python")
print("Apple starts with %c" %"A")

#2
print("I am {} years old".format(20))
print("I like {}color and {}color".format("blue", "red"))
print("I like {0}color and {1}color".format("blue", "red"))


#3
print("I am {age}years old, and I like {color}color".format(age=20, color="red"))

#4. Python3.6 above
age = 20
color ="red"
print(f"I am {age}years old, and like {color}color")

#quiz
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3]+ str(len(my_str))+ str(my_str.count("e"))+"!"
print(password)


#List

subway = ["a", "b", "c"]
print(subway.index("b"))

subway.append("d")
print(subway)

subway.insert(1, "aa")
print(subway)

print(subway.pop())

#Sorting
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

#num_list.clear()
num_list = [5,4,3,2,1]
mix_list = ["a", "b"]

num_list.extend(mix_list)
print(num_list)

#Dictionary
cabinet = {3:"a", 100:"bb"}
print(cabinet[3])
print(cabinet.get(3))
print(cabinet.get(5, "there is no"))

print(3 in cabinet)
print("a" in cabinet)

#new
cabinet["c-20"] ="new"
print(cabinet)

#delete
del cabinet["c-20"]
print(cabinet)

#print keys
print(cabinet.keys())

#print values
print(cabinet.values())

#key, value pairs
print(cabinet.items())

#Delete all
cabinet.clear()
print(cabinet)


#Tuple
menu = ("donkkas", "cheesekas")
print(menu[0])
print(menu[1])

# menu.add("fishkas") error

name, age, hobby = "kim", 20, "coding"

#SET
#No duplicaetion, no order
my_set = {1,2,3,3,3}
print(my_set)
java = {"a", "b", "c"}
python = set(["a", "b"])

#Intersection
print(java & python)
print(java.intersection(python))

#Union
print(java | python)
print(java.union(python))

#Difference
print(java-python)
print(java.difference(python))


python.add("c")
print(python)

python.remove("c")
print(python)

#Change data sructures
menu = {"coffee", "milk", "Juice"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#quiz
from random import *
users = range(1,21)
users = list(users)
shuffle(users)

winners = sample(users, 4)

print("--Winner---")
print("chicken: {0}".format(winners[0]))
print("chicken: {0}".format(winenrs[1:]))
