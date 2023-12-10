from math import lcm

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]


class Node:
    def __init__(self, val: str, children: tuple[str]):
        self.val = val
        self.children = children

    @property
    def isPartOneLast(self) -> bool:
        return self.val == 'ZZZ'

    @property
    def isPartTwoFirst(self) -> bool:
        return self.val.endswith('A')

    @property
    def isPartTwoLast(self) -> bool:
        return self.val.endswith('Z')

    def get_side(self, side: str) -> str:
        if side == 'L':
            return self.children[0]
        return self.children[1]


directions = lines.pop(0)

nodes = {}
for node in lines:
    aKey, aValue = node.split(' = ')[0],  tuple(node.split(' = ')[1].replace('(', '').replace(')', '').split(', '))
    nodes[aKey] = Node(aKey, aValue)

# Part 1
counter = 0
node = nodes.get('AAA')
while not node.isPartOneLast:
    for side in directions:
        counter += 1
        node = nodes.get(node.get_side(side))
        if node.isPartOneLast:
            break
print(counter)

# Part 2
counter = 0
startNodes = [node for node in nodes.values() if node.isPartTwoFirst]
currentNodes = [node for node in nodes.values() if node.isPartTwoFirst]
counters = ['']*len(currentNodes)
test = ['']*len(currentNodes)
while not all(counters):
    for side in directions:
        counter += 1
        currentNodes = [nodes.get(node.get_side(side)) for node in currentNodes]
        for node in [aNode for aNode in currentNodes if aNode.isPartTwoLast]:
            anIndex = currentNodes.index(node)
            counters[anIndex] = counter if not counters[anIndex] else counters[anIndex]
            test[anIndex] = node if not test[anIndex] else test[anIndex]
        if all(counters):
            break
print(lcm(*counters))
