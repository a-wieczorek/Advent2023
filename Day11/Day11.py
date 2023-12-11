with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]


def transpose(aList: list[str]) -> list[str]:
    return [''.join(x) for x in zip(*aList)]


def calculate_distance(startCoords: tuple[int, int], endCoords: tuple[int, int]) -> tuple[int, int]:
    endRow, endCol = endCoords
    startRow, startCol = startCoords
    distance = abs(endRow - startRow) + abs(endCol - startCol)
    crossedExpandedRows = len([expandedRow for expandedRow in expandedRows
                               if startRow < expandedRow < endRow or endRow < expandedRow < startRow])
    crossedExpandedCols = len([expandedCol for expandedCol in expandedColumns
                               if startCol < expandedCol < endCol or endCol < expandedCol < startCol])
    distanceExpanded = distance + crossedExpandedRows + crossedExpandedCols
    distanceExpandedPartTwo = distance - crossedExpandedRows - crossedExpandedCols + \
                              1_000_000 * (crossedExpandedRows + crossedExpandedCols)

    return distanceExpanded, distanceExpandedPartTwo


galaxiesCoords, expandedRows, expandedColumns = set(), set(), set()
for i, line in enumerate(lines):
    if '#' not in line:
        expandedRows.add(i)
        continue
    for j, symbol in enumerate(line):
        if symbol == '#':
            galaxiesCoords.add((i, j))

for i, line in enumerate(transpose(lines)):
    if '#' not in line:
        expandedColumns.add(i)

distances = []
while len(galaxiesCoords) > 1:
    galaxyOne = galaxiesCoords.pop()
    for galaxyTwo in galaxiesCoords:
        distances.append(calculate_distance(galaxyOne, galaxyTwo))

# Part 1
print(sum(distance[0] for distance in distances))
# Part 2
print(sum(distance[1] for distance in distances))
