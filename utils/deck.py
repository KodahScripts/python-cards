import random

class Card:
    def __init__(self, card_char:str, suit:str) -> None:
        self._char = card_char
        self._suit = suit

    @property
    def value(self) -> int:
        if self._char == 'A':
            return 11
        elif self._char == 'K' or self._char == 'Q' or self._char == 'J':
            return 10
        else:
            return int(self._char)

    def __repr__(self) -> str:
        return f"{self._char}{self._suit}"


class Hand:
    def __init__(self) -> None:
        self._hand = []

    def add(self, cards:list[Card]):
        for card in cards:
            self._hand.append(card)

    def get_total(self) -> int:
        total = 0
        for card in self._hand:
            total += card.value
        return total

    def play_top(self) -> Card:
        return self._hand.pop()

    def play_by_count(self, count) -> list[Card]:
        played = []
        while len(played) < count:
            played.append(self._hand.pop())
        return played

    def __repr__(self) -> str:
        hand = []
        for card in self._hand:
            hand.append(str(card))
        return ", ".join(hand)


class Deck:
    def __init__(self) -> None:
        self._chars = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self._suits = "♣♦♥♠"
        self._deck:Hand = Hand()
        
        cards = []
        for suit in self._suits:
            for char in self._chars:
                card = Card(char, suit)
                cards.append(card)
        random.shuffle(cards)
        self._deck.add(cards)

    def burn(self) -> None:
        self._deck.play_top()

    def deal(self, count:int) -> list[Card]:
        return self._deck.play_by_count(count)

    def __repr__(self) -> str:
        return str(self._deck)


if __name__ == "__main__":
    d = Deck()
    print(d)
