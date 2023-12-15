with open('input.txt', 'r') as f:
    steps = f.read().split(',')


def hash_string(aString: str) -> int:
    current = 0
    for char in aString:
        current += ord(char)
        current = (current * 17) % 256
    return current


class Lens:
    def __init__(self, lensLabel: str, lensFocalLen: int):
        self.lensLabel = lensLabel
        self.lensFocalLen = lensFocalLen


class Box:
    def __init__(self, ID: int):
        self.ID = ID
        self.lenses: list[Lens] = []

    def remove_lens(self, lensLabel: str) -> None:
        allLabels = [lens.lensLabel for lens in self.lenses]
        if lensLabel in allLabels:
            self.lenses.pop(allLabels.index(lensLabel))

    def add_lens(self, lensLabel: str, lensFocalLen: int) -> None:
        allLabels = [lens.lensLabel for lens in self.lenses]
        if lensLabel in allLabels:
            self.lenses[allLabels.index(lensLabel)].lensFocalLen = lensFocalLen
            return
        self.lenses.append(Lens(lensLabel, lensFocalLen))

    @property
    def focusingPower(self) -> int:
        return sum([(self.ID + 1) * (i + 1) * lens.lensFocalLen for i, lens in enumerate(self.lenses)]) if self.lenses else 0


partOneValues = []
boxes = {i: Box(i) for i in range(256)}

for step in steps:
    partOneValues.append(hash_string(step))
    if len(x := step.split('-')) > 1:
        label = x[0]
        boxes.get(hash_string(label)).remove_lens(label)
    else:
        label, focalLen = step.split('=')
        boxes.get(hash_string(label)).add_lens(label, int(focalLen))

print(sum(partOneValues))
print(sum(boxes[i].focusingPower for i in range(256)))




