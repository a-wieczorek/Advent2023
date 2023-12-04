with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]


class LotteryCard:
    def __init__(self, cardData):
        cardID, cardData = cardData.split(': ')
        self.cardID = int(cardID.replace('Card ', ''))
        winningNumbers, lotteryNumbers = cardData.split(' | ')
        self.winningNumbers = set(num.strip() for num in winningNumbers.split(' ') if num.strip())
        self.lotteryNumbers = set(num.strip() for num in lotteryNumbers.split(' ') if num.strip())
    cardID: int
    winningNumbers: set[str]
    lotteryNumbers: set[str]
    points: int = 0


allCards = []
for line in lines:
    card = LotteryCard(line)
    if counter := len(card.winningNumbers & card.lotteryNumbers):
        card.points = int(2**(counter-1))
    allCards.append(card)

# Part 1
print(sum([card.points for card in allCards]))

# Part 2
maxCardID = len(allCards)
cardsCounter = dict.fromkeys(range(1, maxCardID +1), 1)
for card in allCards:
    if not card.points:
        continue
    cardAmount = cardsCounter[card.cardID]
    matches = len(card.winningNumbers & card.lotteryNumbers)
    for i in range(1, matches+1):
        ID = card.cardID + i
        if ID > maxCardID:
            break
        cardsCounter[ID] += cardAmount
print(sum(cardsCounter.values()))
