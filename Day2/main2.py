class SequenceChecker:
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

    @staticmethod
    def is_safe_with_single_removal(numbers: list[int]) -> bool:
        for index in range(len(numbers)):
            # Create a new list without the element at the current index
            copy = numbers[:index] + numbers[index+1:]
            if SequenceChecker.all_increasing(copy) or SequenceChecker.all_decreasing(copy):
                return True
        return False

if __name__ == '__main__':
    result = 0
    with open('input') as f:
        for line in f:
            numbers = list(map(int, line.split()))

            if SequenceChecker.all_increasing(numbers) or SequenceChecker.all_decreasing(numbers):
                result += 1
            else:
                if SequenceChecker.is_safe_with_single_removal(numbers):
                    result += 1
    print(result)