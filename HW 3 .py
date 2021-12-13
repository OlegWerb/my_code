from hwpl import plates_list



unique_numbers = set(plates_list)
print(len(unique_numbers))


search = input("please input namber : ")

#suma = 0


#while search > 0:
 #   digit = search % 10
  #  suma = suma + digit
   # search = search // 10

#print(suma)


#search = str(input("please input namber : "))

x = search



if x in plates_list:
    print("true")
else:
    print("false")
#    print("Yes")
#else:
#    print("No")



exit()
