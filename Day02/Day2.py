from math import prod

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]

# Part 1
cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
goodGamesIDs = []
for game in lines:
    goodGame = True
    gameID = int(game.split(': ')[0].replace('Game ', ''))
    game = game.split(': ')[1]
    for aSet in game.split('; '):
        for subset in aSet.split(', '):
            amount, color = int(subset.split(' ')[0]), subset.split(' ')[1]
            if cubes[color] < amount:
                goodGame = False
                break
        if not goodGame:
            break
    if goodGame:
        goodGamesIDs.append(gameID)
print(sum(goodGamesIDs))

# Part 2
powers = []
for game in lines:
    game = game.split(': ')[1]
    amounts = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for aSet in game.split('; '):
        for subset in aSet.split(', '):
            amount, color = int(subset.split(' ')[0]), subset.split(' ')[1]
            amounts[color] = amount if amount > amounts[color] else amounts[color]
    powers.append(prod(amounts.values()))
print(sum(powers))
