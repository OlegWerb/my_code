from hwpl import plates_list



unique_numbers = list(set(plates_list))
print(len(unique_numbers))


search = int(input("please input namber : "))

suma = 0


while search > 0:
    digit = search % 10
    suma = suma + digit
    search = search // 10

print(suma)

#Надо узнать есть ли введенный с клавиатуры номер в списке (без учета регистра букв) -> не получаеться =(
#n = plates_list

#x = n.count(search)


exit()
