from sys import argv
from collections import OrderedDict
from poker_judger import PokerJudger


def main():
    players = OrderedDict()
    n, players_inp = int(argv[1]), argv[2:]
    if n != len(players_inp):
        raise Exception("Number of players does not match!")
    for player in players_inp:
        players[player[0]] = player[1:]
    judge = PokerJudger(players)
    print(judge.get_winner())


if __name__ == '__main__':
    main()
