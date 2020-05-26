for waiting_no in range(5): #0,1,2,3,4
    print("waiting number: {0}".format(waiting_no))

for waiting_no in range(1,6): #0,1,2,3,4
    print("waiting number: {0}".format(waiting_no))


absent = [2,5] #absent
for student in range(1,11):
    if student in absent:
        continue
    print("{0}, read the book".format(student))


#출석번호가 1,2,3,4 앞에 100을 붙이기로 함
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)
print(students)

#length of student name
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

#Capitalize
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

#quiz
from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if(5<=time<=15):
        print("{0} cusotmer time {1}minutes".format(i, time))
        cnt+=1
    else:
        print("{0} cusotmer time {1}minutes".format(i, time))


def profile(name, age=27, main_lang="Python"):
    print("name: {0}\t age: {1}\t language {2}".format(name, age, main_lang))

profile("injun")
profile("changwha")

#위치, 키워드 인자의 개수가 많아지거나 인자의 수가 미정일 경우 가변인자를 사용합니다.
#가변 위치인자(*args)는 임의개수의 위치인자를 tuple형태의 변수로 저장합니다.'
#가변 키워드인자(**kwargs)는 임의개수의 키워드인자를 dictionary형태로 저장합니다.


def profile(name, age, *language):
    print("name: {0}\t age : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("injun", 27, "Python", "Java", "C", "C++", "Android", "Javascript")
profile("Kim", 25)

#Local variable, global variable

gun = 10

def checkpoint(soldiers):
    global gun #global gun
    gun = gun - soldiers
    print("left gun: {0}".format(gun))

print("gun: {0}".format(gun))
checkpoint(2)
print("gun: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("left gun: {0}".format(gun))
    return gun


print("gun: {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("gun: {0}".format(gun))


#quiz
def std_weight(height, gender):
    if gender=="male":
        return height*height*22
    else:
        return height*height*21

height = 188
gender ="male"
weight = round(std_weight(height/100, gender), 2)
print(weight)

#end means change the last character of line
#from '\n' to '?'
print("Python", "Java", sep=",", end="?")
print("what?")

import sys
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr)

scores = {"math":90, "Eng":80, "coding":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")


#bank
for num in range(1, 21):
    print("wait number: "+ str(num).zfill(3))


#left empty space empty, right side sorting, total space will be 10
print("{0: >10}".format(123456789))

#positive +, negative -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#left sorting, fill empty space with _
print("{0:_<+10}".format(500))
