from collections import Counter

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().split('\n') if line]

cardValues = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
}


class Hand:
    def __init__(self, cards: str, bid: str, part2: bool = False):
        self.cards = cards
        self.bid = int(bid)
        self.part2 = part2

    def __lt__(self, other):
        def swap_jokers(cards: str):
            jokerCount = cards.count('J')
            if jokerCount == 5:
                return 'AAAAA'
            cardsLeftCounter = Counter(cards.replace('J', ''))
            biggestComboCard = cardsLeftCounter.most_common(1)[0][0]
            return cards.replace('J', '') + biggestComboCard * jokerCount

        selfCounter = Counter(self.cards) if not self.part2 else Counter(swap_jokers(self.cards))
        otherCounter = Counter(other.cards) if not self.part2 else Counter(swap_jokers(other.cards))
        # less unique cards == better type
        if len(selfCounter) > len(otherCounter):
            return True
        if len(otherCounter) > len(selfCounter):
            return False
        # equal amount of same cards
        # more of the same card in hand == better type
        if max(selfCounter.values()) > max(otherCounter.values()):
            return False
        if max(otherCounter.values()) > max(selfCounter.values()):
            return True
        # same hand, checking card value
        for selfCard, otherCard in zip(self.cards, other.cards):
            if int(cardValues.get(selfCard, selfCard)) < int(cardValues.get(otherCard, otherCard)):
                return True
            if int(cardValues.get(otherCard, otherCard)) < int(cardValues.get(selfCard, selfCard)):
                return False


# Part 1
hands = set(Hand(line.split()[0], line.split()[1]) for line in lines)
print(sum([(i+1) * hand.bid for i, hand in enumerate(sorted(hands))]))

# Part 2
cardValues['J'] = 1
hands = set(Hand(line.split()[0], line.split()[1], part2=True) for line in lines)
print(sum([(i+1) * hand.bid for i, hand in enumerate(sorted(hands))]))

