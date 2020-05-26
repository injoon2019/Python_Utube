# score_file = open("score.txt", "w", encoding="utf-8")
# print("math: 80", file=score_file)
# print("eng: 90", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("sci: 90")
# score_file.write("\ncoding: 100")
# score_file.close()

# score_file= open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# score_file= open("score.txt", "r", encoding="utf-8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end='')
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  #save in list
# for line in lines:
#     print(line, end='')
#
# score_file.close()

#######Pickle
import pickle
# profile_file = open("profile.pickle", "wb")
#
# profile = {"name": "kim", "age":30, "hobby":["A", "b", "C"]}
# print(profile)
#
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("I am studying python")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())
