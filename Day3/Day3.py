from math import prod

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]


def check_index(indexToCheck: list[int], aList: list[list[str]]):
    rowIndex, colIndex = indexToCheck
    val = aList[rowIndex][colIndex]
    if not val.isdigit() and val != '.':
        if val == '*':
            for asterisk in allAsterisks:
                if asterisk.location == [rowIndex, colIndex]:
                    return True
            allAsterisks.append(AsteriskSymbol(rowIndex, colIndex))
        return True
    return False


def get_neighbouring_indices(rowIndex, colIndex):
    return [
        [rowIndex - 1, colIndex - 1], [rowIndex - 1, colIndex], [rowIndex - 1, colIndex + 1],
        [rowIndex, colIndex - 1], [rowIndex, colIndex + 1],
        [rowIndex + 1, colIndex - 1], [rowIndex + 1, colIndex], [rowIndex + 1, colIndex + 1]
    ]


class NumberData:
    def __init__(self):
        self.number = ''
        self.numberIndices = []
    number: str
    numberIndices: list
    isFinal: bool = False


class AsteriskSymbol:
    def __init__(self, rowIndex: int, colIndex: int):
        self.location = [rowIndex, colIndex]
        self.neighbours = get_neighbouring_indices(rowIndex, colIndex)
    location: list[int]
    neighbours: list[list[str]]


lines = [[y for y in x] for x in lines]

allNumbersData = []
allAsterisks = []
numberData = NumberData()
for rowIndex, row in enumerate(lines):
    if numberData.number:
        allNumbersData.append(numberData)
    numberData = NumberData()
    for colIndex, col in enumerate(row):
        if not col.isdigit():
            if numberData.number:
                allNumbersData.append(numberData)
                numberData = NumberData()
            continue
        numberData.number += col
        numberData.numberIndices.append([rowIndex, colIndex])

        indicesToCheck = get_neighbouring_indices(rowIndex, colIndex)
        indicesToCheck = [indexToCheck for indexToCheck in indicesToCheck if
                          0 <= indexToCheck[0] <= len(lines) - 1 and  # row index condition
                          0 <= indexToCheck[1] <= len(lines[0]) - 1]  # column index condition
        if any([check_index(indexToCheck, lines) for indexToCheck in indicesToCheck]):
            numberData.isFinal = True

# Part 1
finalNumbers = [numberData for numberData in allNumbersData if numberData.isFinal]
print(sum([int(num.number) for num in finalNumbers]))

# Part 2
finalNeighbouringNumbers = []
for asterisk in allAsterisks:
    neighbouringNumbers = []
    for finalNumber in finalNumbers:
        if any(index in asterisk.neighbours for index in finalNumber.numberIndices):
            neighbouringNumbers.append(int(finalNumber.number))
    if len(neighbouringNumbers) == 2:
        finalNeighbouringNumbers.append(prod(neighbouringNumbers))
print(sum(finalNeighbouringNumbers))
