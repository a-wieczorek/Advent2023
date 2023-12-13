from typing import Optional

patterns = []
with open('input.txt', 'r') as f:
    pattern = []
    for line in f.read().split('\n'):
        if not line:
            patterns.append(pattern)
            pattern = []
            continue
        pattern.append(line)


def transpose(aList: list[str]) -> list[str]:
    return [''.join(x) for x in zip(*aList)]


def find_reflection_line(aList: list[str], part2: bool = False) -> Optional[int]:
    def compare_rows(duplicateIndex: int, checkRange: int, imperfect: bool = False) -> bool:
        top = aList[duplicateIndex - checkRange: duplicateIndex + 1]
        bottom = aList[duplicateIndex + 1: duplicateIndex + 2 + checkRange][::-1]
        if not imperfect:
            return top == bottom
        # exactly 1 difference between all rows
        return sum(sum(letter1 != letter2 for letter1, letter2 in zip(row1, row2)) for row1, row2 in zip(top, bottom)) == 1

    duplicates = []
    for i in range(1, len(aList)):
        if aList[i - 1] == aList[i] or (part2 and sum(x != y for x, y in zip(aList[i - 1], aList[i])) == 1):
            duplicates.append(i-1)

    for duplicate in duplicates:
        distanceToEnd = min(len(aList[:duplicate]), len(aList[duplicate + 2:]))
        if compare_rows(duplicate, distanceToEnd, part2):
            return duplicate
    
    return None


amounts = []
amountsPartTwo = []
for pattern in patterns:
    rowID = find_reflection_line(pattern)
    rowIDPartTwo = find_reflection_line(pattern, True)

    if rowID is None:
        rowID = find_reflection_line(transpose(pattern))
        amounts.append(rowID + 1)
    else:
        amounts.append((rowID + 1) * 100)

    if rowIDPartTwo is None:
        rowIDPartTwo = find_reflection_line(transpose(pattern), True)
        amountsPartTwo.append(rowIDPartTwo + 1)
    else:
        amountsPartTwo.append((rowIDPartTwo + 1) * 100)

print(sum(amounts))
print(sum(amountsPartTwo))
