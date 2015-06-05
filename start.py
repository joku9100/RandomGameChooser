import random
import os
import pickle

def randomizegame():
    amount_games = len(list_games)
    print (list_games[random.randrange(0,amount_games,1)])

if not os.path.isfile('gamedata.txt'):
    open('gamedata.txt','w')


list_games = []
f = open('gamedata.txt','rb')
while 1:
    try:
        list_games.append(pickle.load(f))
    except EOFError:
        break



answer  = input( "Do you want to add more games? Yes or No ")
gameinput = 'what'
if answer == 'Yes':
    while gameinput != "0":
        print("Enter 0 to exit")
        gameinput = input("Input additional games: ")
        
        while
        if gameinput == list_games[len(list_games-1)]
        list_games.append(gameinput)




answer  = input( "Do you want to pick a game? Yes or No")

if answer == 'Yes':
    randomizegame()


