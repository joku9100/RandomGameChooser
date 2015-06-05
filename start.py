import random
import os
import pickle

def randomizegame():
   # print (list_games)
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
        f.close()
        break



answer  = input( "Do you want to add more games? Yes or No ")
gameinput = 'what'
if answer == 'Yes':
    while gameinput != "0":
        gameindata = True
        print("Enter 0 to exit")
        gameinput = input("Input additional games: ")
        #list_games.append(gameinput)
        a = 0
        if gameinput!='0':
            while a +1 < len(list_games):
                if gameinput == list_games[a]:
                    gameindata = False
                    
                a = a +1
            if gameindata:
                list_games.append(gameinput)
                




answer  = input( "Do you want to pick a game? Yes or No ")

if answer == 'Yes':
    randomizegame()


f = open('gamedata.txt','wb')
games=len(list_games)
a = 0
while a   <games:
    pickle.dump(list_games[games-1],f)
    list_games.pop()
    games = len(list_games)
    


