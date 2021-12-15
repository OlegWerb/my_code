from hwpl import plates_list

unique_numbers = set(plates_list)
print(len(unique_numbers))



search = input("please input namber : ")

x = search.upper()

if x in plates_list:
    print("true")
else:
    print("false")

# a = int(search[2])
# b = int(search[3])
# c = int(search[4])
# d = int(search[5])
#
# print(a+b+c+d)

x = x[2:6]

e = 0
for i in range(2, 6):
    e = e + int(x[i])

#print(x)

exit()
