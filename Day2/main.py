@staticmethod
def all_increasing(numbers: list[int]) -> bool:
    currentValue = numbers[0] - 1
    for number in numbers:
        if number > currentValue and abs(number - currentValue) <= 3:
            currentValue = number
        else:
            return False
    return True

@staticmethod
def all_decreasing(numbers: list[int]) -> bool:
    currentValue = numbers[0] + 1
    for number in numbers:
        if number < currentValue and abs(number - currentValue) <= 3:
            currentValue = number
        else:
            return False
    return True

if __name__ == '__main__':
    result = 0
    with open('input') as f:
        for line in f:
            # Split the line into a list of numbers
            numbers = list(map(int, line.split()))
            # Check if the numbers are all increasing or decreasing
            if all_increasing(numbers) or all_decreasing(numbers):
                result += 1
    print(result)