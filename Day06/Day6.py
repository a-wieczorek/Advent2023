from math import prod

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]

times = [int(ms.strip()) for ms in lines[0].split(' ')[1:] if ms]
distances = [int(mm.strip()) for mm in lines[1].split(' ')[1:] if mm]

racesWon = []
for milliSec, milliMet in zip(times, distances):
    counter = 0
    for i in range(1, milliSec):
        if milliMet < i * (milliSec-i):
            counter += 1
    racesWon.append(counter)
print(prod(racesWon))

milliSec = int(''.join([str(ms) for ms in times]))
milliMet = int(''.join([str(mm) for mm in times]))
counter = 0
for i in range(1, milliSec):
    if milliMet < i * (milliSec-i):
        counter += 1
print(counter)
