import random


class PokerHand:
    """
       Represents poker hands
    """
    CARD_RANK = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
                 "A": 14}

    def __init__(self, id, cards):
        """
        Initializes the PokerHand Class.

        :param id: player_id
        :param cards: player hands
        """
        self.id = id
        self.suits = {"s": 0, "h": 0, "d": 0, "c": 0}
        self.values = {}
        self.is_flush = False
        for card in cards.split():
            card_val = self.CARD_RANK.get(card[0])
            self.values[card_val] = self.values.get(card_val, 0) + 1
            self.suits[card[1]] += 1
            if self.suits[card[1]] == 3:
                self.is_flush = True
        self.hand = self.sort_hand()
        self.is_straight = self.check_for_straight()
        self.ranks = [self.determine_rank()] + self.hand[:]

    def sort_hand(self):
        """
        Sort the card values in descending (highest to lowest) order give precedence to values that appears more times

        :return: a list with all the words in the file
        """
        hands = []
        for i in range(1, 4):
            hands += sorted([k for k, v in self.values.items() if v == i])
        return hands[::-1]

    def check_for_straight(self):
        """
        Check if hand has a straight

        :return: Boolean
        """
        val_array = self.hand[:]
        if 14 in val_array:
            val_array[val_array.index(14)] = 1 if 2 in val_array else 14
        return val_array == list(range(val_array[0], val_array[0] - 3, -1))

    def determine_rank(self):
        """
        Identify the rank of the hand based off the criteria for comparison

        :return: int
        Straight Flush - 6
        Three Of A Kind - 5
        Straight - 4
        Flush - 3
        Pair - 2
        High Card - 1
        """
        num_vals = list(self.values.values())
        # check for flush or straight flush
        if self.is_flush:
            return 6 if self.is_straight else 3
        # check for three of a kind
        if num_vals.count(3) == 1:
            return 5
        # check for straight
        if self.is_straight:
            return 4
        # check for pairs
        if num_vals.count(2) == 1:
            return 2
        # check for high card
        return 1
