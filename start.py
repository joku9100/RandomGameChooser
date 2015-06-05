import random


def randomizegame():
    amount_games = len(list_games)
    print (list_games[random.randrange(0,amount_games,1)])


gameinput = input("Input game here: " )
list_games = [];
list_games.append(gameinput)
while gameinput != "0":
    print("Enter 0 to exit")
    gameinput = input("Input additional games")
    list_games.append(gameinput)


randomizegame()


