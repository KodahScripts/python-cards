# Blackjack
import utils.deck
import utils.entities


class Game:
    def __init__(self):
        self.player = Player()
        self.board = {
            "player": Hand(),
            "dealer": Hand()
        }
        self.deck = Deck()


if __name__ == "__main__":
    g = Game()
    print(g.deck)
