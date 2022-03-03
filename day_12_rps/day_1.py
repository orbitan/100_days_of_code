import random

round = 0


class Player:
    player_id = None
    player_points = 0
    hand_cards = []
    

    def __init__(self, player_id, player_points):
        self.player = player_id
        self.player_points = player_points

    @classmethod
    def set_player_points(self, value):
        player_points = self.player_points + value
        return player_points, self.hand_cards

    @classmethod
    def add_handcards(self, card, player_id):
        self.hand_cards.append(card)
        value = card.value
        self.set_player_points(value, Player.player_id)


class PlayingCard:
    def __init__(self, value, card_id):
        self.value = value
        self.id = card_id


cards = [PlayingCard(i, f"{i}") for i in range(1, 10)]
cards.append(PlayingCard(1, "ace"))
_ = ["queen", "king", "boy"]
for el in _:
    PlayingCard(10, el)

players = [Player(1, 0), Player(-1, 0)]


#  game loop, true while sum of comp && player is less than 21
def game_loop(round, player):
    if round == 0:
        print(f"You're card: [{gen_cards(player)}] [{gen_cards(player)}]")
        player = player * (-1)
        print(f"You´re opponents: [{gen_cards(player)}]")
        round += 1


#  hand cards out (two to player, two to cmputer but only one is visible
def gen_cards(player):
    card = random.choice(cards)
    Player.add_handcards(card, player)
    Player.player_points += card.value
    print(f"Spieler {Player.player_id}:{Player.player_points} Punkte")
    return card.id, card.value


game_loop(0, 1)
