from hwpl import plates_list


def uniq_numb():
    uniq_numb = len(set(plates_list))
    print(uniq_numb)

uniq_numb()

def search_plates():
    search = input("please input namber : ")

    x = search.upper()

    if x in plates_list:
        print("true")
    else:
        print("false")

search_plates()


def su_num():
    search = input("please input namber : ")

    x = search.upper()

    x = x[2:6]

    e = 0
    for i in range(0, 4):
        e = e + int(x[i])

    print(e)

su_num()

exit()
