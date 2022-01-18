import json

a = 10

# f = open( 'text.txt', 'w' ) #(w = write)
# f.write(a)
# f.close()

with open("text.json", "w") as f:
    json.dump(a, f)


# # li = [-10, 3, -55, 2,]
# #
# # maximum = li[0]
# # for i in li:
# #     if i > maximum:
# #         maximum = i
# # print(maximum)
# from random import randint
#
# lst = []
# slovar = dict()
#
#
#
# for i in range(100):
#     slovar[i] = randint(1,100) ** 3.5
#     lst.append(i**2) }\n")

# file = open("text.txt", "r")
#
# #
# # file.readline()
# #
# #
# # file.close()
#
# # with open("text.txt", "w") as file:
# #     file.write(str(slovar))
#
#  with open("text.txt", "r") as file:
#     file.write(str(slovar))
#
#
# #     print("do something")
# #
# # print("end")
#


# with open("test.json", "r") as f:
#     data = json.load(f)
# #
# print(value)
# # value = file.read(10)
# # print (value)


