from time import time

with open('input.txt', 'r') as f:
    layout = [line for line in f.read().split('\n') if line]

mirrors = {
    '|': {
        'N': 'N',
        'S': 'S',
        'E': 'NS',
        'W': 'NS',
    },
    '-': {
        'N': 'EW',
        'S': 'EW',
        'E': 'E',
        'W': 'W',
    },
    '/': {
        'N': 'E',
        'S': 'W',
        'E': 'N',
        'W': 'S',
    },
    '\\': {
        'N': 'W',
        'S': 'E',
        'E': 'S',
        'W': 'N',
    },
    '.': {
        'N': 'N',
        'S': 'S',
        'E': 'E',
        'W': 'W',
    },
}


class Beam:
    def __init__(self, currentCoords: tuple[int, int], direction: str):
        self.currentCoords = currentCoords
        self.direction = direction  # direction I'm going when entering a field
        self.active = True
        self.symbol = layout[currentCoords[0]][currentCoords[1]]
        self.path = set()
    symbol: str
    path: set[tuple[int, int, str]]
    currentCoords: tuple[int, int]
    direction: str

    @property
    def row(self):
        return self.currentCoords[0]

    @property
    def col(self):
        return self.currentCoords[1]

    def move(self):
        if (pathRecord := (self.currentCoords[0], self.currentCoords[1], self.direction)) in self.path:
            self.active = False
            return
        self.direction = mirrors[self.symbol][self.direction]  # new direction the pipe is pointing to
        if self.direction == 'NS':
            self.direction = 'N'
            newBeam = Beam(self.currentCoords, direction='S')
            newBeam.path = self.path
            activeBeams.append(newBeam)
        elif self.direction == 'EW':
            self.direction = 'E'
            newBeam = Beam(self.currentCoords, direction='W')
            newBeam.path = self.path
            activeBeams.append(newBeam)
        if self.direction == 'N':
            coordChange = (-1, 0)
        elif self.direction == 'S':
            coordChange = (1, 0)
        elif self.direction == 'E':
            coordChange = (0, 1)
        else:  # self.direction == 'W'
            coordChange = (0, -1)
        self.path.add(pathRecord)
        newCoords = (self.row + coordChange[0], self.col + coordChange[1])
        if newCoords[0] not in range(len(layout)) or newCoords[1] not in range(len(layout[0])):
            self.active = False
            return
        self.currentCoords = newCoords
        self.symbol = layout[self.row][self.col]


# Part 1
startingBeam = Beam((0, 0), 'E')
activeBeams = [startingBeam]
finishedBeams = []
while activeBeams:
    for i, beam in enumerate(activeBeams):
        beam.move()
        if not beam.active:
            finishedBeams.append(activeBeams.pop(i))

allWalked = set((coord[0], coord[1]) for coord in finishedBeams[0].path)
print(len(allWalked))

# Part 2
allStarting = set()
for i in range(len(layout)):
    allStarting.add(Beam((i, 0), 'E'))
    allStarting.add(Beam((i, len(layout)-1), 'W'))
for i in range(len(layout[0])):
    allStarting.add(Beam((0, i), 'S'))
    allStarting.add(Beam((len(layout)-1, i), 'N'))
    
finalValues = []
for startingBeam in allStarting:
    activeBeams = [startingBeam]
    finishedBeams = []
    while activeBeams:
        for i, beam in enumerate(activeBeams):
            beam.move()
            if not beam.active:
                finishedBeams.append(activeBeams.pop(i))
    allWalked = set((coord[0], coord[1]) for coord in finishedBeams[0].path)
    finalValues.append(len(allWalked))
print(max(finalValues))





