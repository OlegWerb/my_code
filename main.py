from hwpl import plates_list

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
        # else:

    # search = input("please input namber : ")



