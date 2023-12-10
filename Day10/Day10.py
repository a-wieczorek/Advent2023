with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]

pipes = {
    '|': {
        'N': 'N',
        'S': 'S'
    },
    '-': {
        'E': 'E',
        'W': 'W'
    },
    'L': {
        'S': 'E',
        'W': 'N'
    },
    'J': {
        'S': 'W',
        'E': 'N'
    },
    '7': {
        'N': 'W',
        'E': 'S'
    },
    'F': {
        'N': 'E',
        'W': 'S'
    },
}


class Pipe:
    def __init__(self, symbol: str, coords: tuple[int, int], direction: str):
        self.symbol = symbol
        self.coords = coords
        self.direction = direction  # the direction I'm going when entering the pipe
    symbol: str
    coords: tuple[int, int]
    direction: str

    @property
    def row(self) -> int:
        return self.coords[0]

    @property
    def col(self) -> int:
        return self.coords[1]

    def move(self) -> None:
        self.direction = pipes[self.symbol][self.direction]  # new direction the pipe is pointing to
        if self.direction == 'N':
            coordChange = (-1, 0)
        elif self.direction == 'S':
            coordChange = (1, 0)
        elif self.direction == 'E':
            coordChange = (0, 1)
        else:
            coordChange = (0, -1)
        self.coords = (self.row + coordChange[0], self.col + coordChange[1])
        self.symbol = maze[self.row][self.col]


maze = []
start = (0, 0)
for i, line in enumerate(lines):
    maze.append([elem for elem in line])
    if 'S' in line:
        start = (i, line.index('S'))

if (elem := maze[start[0] - 1][start[1]]) in ['|', '7', 'F']:  # north
    symbol = elem
    coords = (start[0] - 1, start[1])
    direction = 'N'
elif (elem := maze[start[0] + 1][start[1]]) in ['|', 'L', 'J']:  # south
    symbol = elem
    coords = (start[0] + 1, start[1])
    direction = 'S'
elif (elem := maze[start[0]][start[1] + 1]) in ['-', 'J', '7']:  # east
    symbol = elem
    coords = (start[0], start[1] + 1)
    direction = 'E'
else:
    symbol = maze[start[0]][start[1] - 1]
    coords = (start[0], start[1] - 1)
    direction = 'W'

# Part 1
currentPipe = Pipe(symbol, coords, direction)
path = currentPipe.symbol
cleanMap = [['0']*len(maze[0]) for _ in range(len(maze))]
while True:
    cleanMap[currentPipe.row][currentPipe.col] = currentPipe.symbol
    currentPipe.move()
    if currentPipe.symbol == 'S':
        cleanMap[currentPipe.row][currentPipe.col] = currentPipe.symbol
        break
    path += currentPipe.symbol
print(int((len(path)+1) / 2))

# Part 2
cleanMap[start[0]][start[1]] = '|'
counter = 0
inside = False
for i, row in enumerate(cleanMap):
    inside = False
    prevChanger = ''
    for j, symbol in enumerate(row):
        if inside:
            if symbol == '0':
                #cleanMap[i][j] = '1'
                counter += 1
                continue
            if symbol == '7' and prevChanger == 'F' or symbol == 'J' and prevChanger == 'L':
                inside = False
                continue
            if symbol == '7' and prevChanger == 'L' or symbol == 'J' and prevChanger == 'F':
                continue
            if symbol in ['|', 'L', 'F', 'J', '7']:
                inside = False
                prevChanger = symbol
                continue
        if not inside:
            if symbol == '7' and prevChanger == 'F' or symbol == 'J' and prevChanger == 'L':
                inside = True
                continue
            if symbol == '7' and prevChanger == 'L' or symbol == 'J' and prevChanger == 'F':
                continue
            if symbol in ['|', 'J', '7', 'L', 'F']:
                inside = True
                prevChanger = symbol
                continue

print(counter)
#for row in cleanMap:
#    print(''.join(([elem for elem in row])))

