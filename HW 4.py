from hwpl import plates_list


def uniq_numb():
    uniq_numb = len(set(plates_list))
    print(uniq_numb, "the sum of unique numbers in the list")

uniq_numb()

search = input("please input number : ")

num_plates = search

def in_plates(num_plates):
    if len(num_plates) != 8:
        return False
    else:
        if num_plates in plates_list:
            num_plates = num_plates[:2], num_plates[2], num_plates[3], num_plates[4], num_plates[5], num_plates[6:]
            print("This number in plates_list")
            return num_plates
        else:
            print("This number is not in plates_list")
            num_plates = num_plates[:2], num_plates[2], num_plates[3], num_plates[4], num_plates[5], num_plates[6:]
            return num_plates




print(in_plates(num_plates), "returns number")

# def search_plates():
#     # search = input("please input number : ")
#
#     x = search.upper()
#
#     if x in plates_list:
#         print("this number is in the list of license plates")
#     else:
#         print("this number is not in the list of license plates")
#
# search_plates()


def su_num():


    x = search.upper()

    x = x[2:6]

    e = 0
    for i in range(0, 4):
        e = e + int(x[i])

    print((e), 'this is sum of your number')

su_num()

exit()
