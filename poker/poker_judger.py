from poker_hand import PokerHand


class PokerJudger:
    """
       PokerJudger determines the winner from all of the players hands
    """

    def __init__(self, players):
        """
        Initializes the PokerJudger Class.

        :param players: list of players
        """
        self.players = players

    def get_winner(self):
        """
        Determine the highest rank from all of the poker hands.

        :return: the player's id of the winner
        """
        if not self.players or len(self.players) == 0:
            raise Exception("There's no player in the game!")
        poker_players = [PokerHand(k, v) for k, v in self.players.items()]
        for i in range(len(poker_players[0].ranks)):
            highest_rank = max([player.ranks[i] for player in poker_players])
            poker_players = [
                player for player in poker_players if player.ranks[i] == highest_rank]
            if len(poker_players) == 1:
                return poker_players[0].id
        return " ".join([player.id for player in poker_players])
