from hwpl import plates_list

unique_numbers = list(set(plates_list))
print(len(unique_numbers))


search = int(input("please input namber : "))

if search == plates_list:
    print("yes")
else:
    print("no")


exit()
