import random

import game_data

score = 0


#  Pick two random artists and append them to a list
def pick_two_artists(running):
    artists = []
    while len(artists) < 2:
        artist = []
        r = random.randint(0, len(game_data.data) - 1)
        artist.append(game_data.data[r]['name'])
        artist.append(game_data.data[r]['description'])
        artist.append(game_data.data[r]['country'])
        artist.append(game_data.data[r]['follower_count'])
        artists.append(artist)
    return artists




#  Print to the user
def welcome(artists):
    player_guess = input(f"Who is higher? A: {artists[0][0]}, a {artists[0][1]} from {artists[0][2]}"
              f" or B: {artists[1][0]}, a {artists[1][1]} from {artists[1][2]}\n"
              f"Enter 'A', 'B' or 'E': ")
    return player_guess



#  Comparison: a[-1] to b[-1]
def comparison(artists, players_guess):
    if int(artists[0][3]) > int(artists[1][3]):
        result = "A"
    elif int(artists[0][3]) < int(artists[1][3]):
        result = "B"
    else:
        result = "U"
    running = players_guess == result
    print(running)
    return running




def game_loop(running, score):
    round = 0
    artists = [b]
    while running:
        if round != 0:
            print(f"You won this round. Score {score}")
            artists.pop()
        artists = pick_two_artists(running)
        player_guess = welcome(artists)
        running = comparison(artists, player_guess)
        score += 1
        round += 1

    print(f"You lost. This is you´re score: {score}")








game_loop(True, 0)
