from hwpl import plates_list


def uniq_numb():
    uniq_numb = len(set(plates_list))
    print(uniq_numb)

uniq_numb()

search = input("please input namber : ")

nam_plates = search

def in_plates(nam_plates):
    if len(nam_plates) != 8:
        return False
    else:
        if nam_plates in plates_list:
            nam_plates = nam_plates[:2], nam_plates[2], nam_plates[3], nam_plates[5], nam_plates[6:]
            return nam_plates

print(in_plates(nam_plates))

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
