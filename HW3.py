from hwpl import plates_list

uniq_numb = len(set(plates_list))
print(uniq_numb)

search = input("please input number : ")

x = search.upper()

if x in plates_list:
    print("true")
else:
    print("false")

x = x[2:6]

e = 0
for i in range(0, 4):
    e = e + int(x[i])

print(e)

exit()
