if __name__ == '__main__':
    result = 0
    leftSide = []
    rightSide = []
    with open('input') as f:
        for line in f:
            words = line.split()
            leftSide.append(int(words[0]))
            rightSide.append(int(words[1]))
    leftSide.sort()
    rightSide.sort()
    for i in range(len(leftSide)):
        print("a={0} and b={1}".format(leftSide[i], rightSide[i]))
        result += abs(leftSide[i] - rightSide[i])
    print("RESULT IS: {0}".format(result))

    result2 = 0
    for num in leftSide:
        for num2 in rightSide:
            if (num == num2):
                result2 += num
    print("RESULT2 IS: {0}".format(result2))