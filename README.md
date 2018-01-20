# Three Card Poker Judger

Accepts as its input a collection of hands of cards (3 Card Poker), and selects the winner from among those hands.

## Getting Started

### Prerequisites

Python 3

### How to run

* `cd poker/`
* `./run_tests3 "python main.py"`

### How to Add Tests

* add test files in `poker/tests/`

### Bugs and Limitations

I modified the test runner from
`output = subprocess.check_output(sys.argv[1].split(), universal_newlines=True, input=inp).strip()`
to
`output = subprocess.check_output(sys.argv[1].split() + inp.split('\n') , universal_newlines=True).strip()`

I was not able to get the input in the original test runner in my program from `stdin` or `sys.argv`. Instead, I modified to pass it as the input parameter.

### Testing

I created a `deck_of_cards.py` module that has a Card, Deck and Player class which simulate a deck of cards (shuffled) and each player will draw 3 cards from the deck. Then I used my `poker_judger.py` and `poker_hand.py` modules to determine the winner from those players. Below is a code snippet:

```
# deck_of_cards.py

# init deck of cards
deck = Deck()
# shuffle deck
deck.shuffle()
deck.show()

# create 10 players
players = [Player("player{}".format(i)) for i in range(0, 10)]
ret = []
# each player draw 3 cards
for player in players:
    player.draw(deck).draw(deck).draw(deck)
    ret.append(" ".join(player.showHand()))

# determine the winner
print(ret, PokerJudger.get_winner(ret))
```

## Design decisions

* `main.py`
  * The main access point to the application
* `poker_hand.py`
  * This class keeps tracks of the face values and suits count. It has a methods `determine_rank` to evaluate or score the player’s hand (Taking into account ties). It has a couple of helper methods such as `sort_hand` to sort the cards from highest to lowest. `check_for_straight` and check for flush which will ultimately be used by the `determine_rank` method to return a score or ranking. The way the `determine_rank` is it looks at the face values cards and check for specific criteria, i.e., Straight Flush, Three Of a Kind, Straight, etc. If it finds one of the criteria, it will append the score to the hand (list of face values cards).
* `poker_judger.py`
  * This class sets the up the 3 card poker game accepts all of the players with their respective poker hands and determine the winner. The `get_winner` method iterates through all of the players and tries to find the highest ranks/points and return the player’s id. In the case of a tie, it will return those players’ ids.
* `deck_of_cards.py`
  * This is for testing purpose only and is not part of the program. I created a Card and Deck classes to simulate a deck of cards (52 cards) and using the Fisher-Yates shuffle [Fisher–Yates shuffle - Wikipedia](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) to ensure every card has an equal likelihood of being a draw. I also created a Player class which will have 3 random cards and uses it to tests my `poker_hand.py` and `poker_judge.py` modules.
