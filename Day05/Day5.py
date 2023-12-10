with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]


class Map:
    def __init__(self):
        self.sourceRanges = []
        self.destinationRanges = []
    sourceRanges: list[range]
    destinationRanges: list[range]

    def expand(self, sourceRange: range, destinationRange: range) -> None:
        self.sourceRanges.append(sourceRange)
        self.destinationRanges.append(destinationRange)
        return

    def check_val(self, seed: int) -> int:
        for i, sourceRange in enumerate(self.sourceRanges):
            if seed in sourceRange:
                return self.destinationRanges[i][sourceRange.index(seed)]
        return seed

    def check_val_ranges(self, valRanges: list[range]) -> list[range]:
        output = []
        while valRanges:
            valRange = valRanges.pop(0)
            for destRange, sourceRange in zip(self.destinationRanges, self.sourceRanges):
                if valRange[0] <= sourceRange[0] <= valRange[-1] <= sourceRange[-1]: # left overlap
                    output.append(range(destRange[0], destRange[sourceRange.index(valRange[-1])] + 1))
                    valRange = range(valRange[0], sourceRange[0] + 1)
                elif sourceRange[0] <= valRange[0] <= sourceRange[-1] <= valRange[-1]: # right overlap
                    output.append(range(destRange[sourceRange.index(valRange[0])], destRange[-1] + 1))
                    valRange = range(sourceRange[-1], valRange[-1] + 1)
                elif sourceRange[0] <= valRange[0] and valRange[-1] <= sourceRange[-1]: # valRange inside sourceRange
                    output.append(range(destRange[sourceRange.index(valRange[0])], destRange[sourceRange.index(valRange[-1])] + 1))
                    valRange = None
                    break
                elif valRange[0] <= sourceRange[0] and sourceRange[-1] <= valRange[-1]: # sourceRange inside valRange
                    output.append(destRange)
                    newRange = range(valRange[0], sourceRange[0] + 1)
                    if newRange:
                        valRanges.append(newRange)
                    valRange = range(sourceRange[-1], valRange[-1] + 1)
                if not valRange:
                    break
            if valRange:
                output.append(valRange)
        return output


seeds = [int(num) for num in lines.pop(0).replace('seeds: ', '').split(' ')]
mapOrder = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location',
]

maps = {
    aMap: Map() for aMap in mapOrder
}

mapName = ''
for line in lines:
    if 'map' in line:
        mapName = line.split(' ')[0]
        continue
    destinationStart, sourceStart, rangeLength = [int(num) for num in line.split(' ')]
    maps[mapName].expand(range(sourceStart, sourceStart + rangeLength),
                         range(destinationStart, destinationStart + rangeLength))

# Part 1
finalLocations = set()
for val in seeds:
    for mapName in mapOrder:
        val = maps[mapName].check_val(val)
    finalLocations.add(val)
print(min(finalLocations))

# Part 2
valRanges = [range(start, start+length) for start, length in zip(seeds[::2], seeds[1::2])]
for mapName in mapOrder:
    valRanges = maps[mapName].check_val_ranges(valRanges)

print(min([valRange[0] for valRange in valRanges]))
