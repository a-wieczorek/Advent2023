with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]


def gen_children(sequence: list[int]) -> list[int]:
    return [nextVal - currentVal for currentVal, nextVal in zip(sequence, sequence[1:])]


def gen_tree(top: list[int]) -> list[list[int]]:
    treeLines = [top]
    while any(num != 0 for num in treeLines[-1]):
        treeLines.append(gen_children(treeLines[-1]))
    return treeLines


def extrapolate(tree: list[list[int]]) -> (int, int):
    if all(num == 0 for num in tree[0]):
        return 0, 0
    newLeft, newRight = extrapolate(tree[1:])
    return tree[0][0] - newLeft, tree[0][-1] + newRight


newValPartOne, newValPartTwo = 0, 0
for line in lines:
    history = [int(num.strip()) for num in line.split(' ') if num]
    tree = gen_tree(history)
    newLeft, newRight = extrapolate(tree)
    newValPartOne += newRight
    newValPartTwo += newLeft
print(newValPartOne)
print(newValPartTwo)
