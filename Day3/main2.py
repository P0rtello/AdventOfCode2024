import re
if __name__ == '__main__':
    bigNumber = 0
    listOfListOfStrings: list[list[str]] = []
    with open('input') as f:
        for line in f:
            listOfListOfStrings.append((re.findall("mul[(]\d{1,3},\d{1,3}[)]|do\(\)|don't\(\)", str(line))))

    StopComputing: bool = False
    for ListOfStrings in listOfListOfStrings:
        for strings in ListOfStrings:
            if strings in "do()":
                StopComputing = False
            if strings in "don't()":
                StopComputing = True
            if not StopComputing and strings not in "don't()" and strings not in "do()":
                value = (re.findall("\d{1,3}", str(strings)))
                bigNumber += (int(value[0]) * int(value[1]))
    print(bigNumber)


#"mul[(]\d{1,3},\d{1,3}[)] |\bdo\(\)"