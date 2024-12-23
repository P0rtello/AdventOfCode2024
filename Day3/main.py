import re
if __name__ == '__main__':
    bigNumber = 0
    listOfListOfStrings: list[list[str]] = []
    with open('input') as f:
        for line in f:
            listOfListOfStrings.append((re.findall("mul[(]\d{1,3},\d{1,3}[)]", str(line))))


    for ListOfStrings in listOfListOfStrings:
        for strings in ListOfStrings:
            value = (re.findall("\d{1,3}", str(strings)))
            bigNumber += (int(value[0]) * int(value[1]))
    print(bigNumber)
