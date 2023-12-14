with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]


def rotate_left(aList: list[str]) -> list[str]:  # anti-clockwise
    return [''.join(x) for x in zip(*[x[::-1] for x in aList])]


def rotate(aList: list[str]) -> list[str]:  # clockwise
    return [''.join(x[::-1]) for x in zip(*aList)]


class Reflector:
    def __init__(self, rockMap: list[str]):
        self.rockMap = rockMap

    def __str__(self):
        return '\n'.join(self.rockMap)

    @property
    def totalLoad(self) -> int:
        return sum([line.count('O') * (len(self.rockMap) - i) for i, line in enumerate(self.rockMap)])

    @staticmethod
    def slide(rockMap: list[str]) -> list[str]:
        rockMap = [list(line) for line in rockMap]
        lastEmpty = 0
        for i, row in enumerate(rockMap):
            continuing = False
            for j, symbol in enumerate(row):
                if symbol == '.':
                    if continuing:
                        continue
                    lastEmpty = j
                    continuing = True
                elif symbol == '#':
                    lastEmpty = j + 1
                    continuing = False
                elif symbol == 'O' and continuing:
                    rockMap[i][lastEmpty] = 'O'
                    rockMap[i][j] = '.'
                    lastEmpty = lastEmpty + 1
        return [''.join(line) for line in rockMap]

    def cycle(self) -> None:
        adjustedMap = rotate_left(self.rockMap)
        for _ in range(4):
            adjustedMap = self.slide(adjustedMap)
            adjustedMap = rotate(adjustedMap)
        self.rockMap = rotate(adjustedMap)

    def tilt_north(self) -> None:
        self.rockMap = rotate(self.slide(rotate_left(self.rockMap)))


# Part 1
reflector = Reflector(lines)
reflector.tilt_north()
print(reflector.totalLoad)

# Part 2
reflector = Reflector(lines)
cycled = [reflector.rockMap]
i = 0
while True:
    reflector.cycle()
    if reflector.rockMap in cycled:
        break
    i += 1
    cycled.append(reflector.rockMap)
cycle = cycled[cycled.index(reflector.rockMap):]
finalMap = cycle[(1000000000-len(cycled)) % len(cycle)]
finalReflector = Reflector(finalMap)
print(finalReflector.totalLoad)

