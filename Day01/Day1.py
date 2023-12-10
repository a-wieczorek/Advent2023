FILTERS = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]

# Part 1
numbers = [''.join(filter(str.isdigit, line)) for line in lines]
print(sum([int(number[0]+number[-1]) for number in numbers if number]))

# Part 2
numbers = []
for line in lines:
    startDigits = ''.join(filter(str.isdigit, line))
    firstDigit = startDigits[0]
    firstDigitIndex = line.index(startDigits[0])
    reversedLine = line[::-1]
    lastDigit = startDigits[-1]
    lastDigitIndex = reversedLine.index(startDigits[-1])
    for key in FILTERS:
        newLine = line.replace(key, FILTERS[key])
        digits = ''.join(filter(str.isdigit, newLine))
        if int(newLine.index(digits[0])) < firstDigitIndex:
            firstDigit = digits[0]
            firstDigitIndex = newLine.index(digits[0])
        reversedNewLine = newLine[::-1]
        if int(reversedNewLine.index(digits[-1])) < lastDigitIndex:
            lastDigit = digits[-1]
            lastDigitIndex = reversedNewLine.index(digits[-1])
    numbers.append(firstDigit + lastDigit)

print(sum([int(number) for number in numbers]))
