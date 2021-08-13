#Single player in console XO game
#Written by dDaiver
import random
Pole = [0,1,2,
        3,4,5,
        6,7,8]
Pole2 = [0,1,2,
         3,4,5,
         6,7,8]

game = True
schet = 0
players = ('X','O')
player = (random.choice(players))


def changeWin():
    global game
    if Pole[0] == player:
        if Pole[1] == player:
             if Pole[2] == player:
                print('You Win '+ player)
                game = False
    
    if Pole[3] == player:
        if Pole[4] == player:
             if Pole[5] == player:
                print('You Win '+ player)
                game = False
    
    if Pole[6] == player:
        if Pole[7] == player:
             if Pole[8] == player:
                print('You Win '+ player)
                game = False

    if Pole[0] == player:
        if Pole[3] == player:
             if Pole[6] == player:
                print('You Win '+ player)
                game = False
    if Pole[1] == player:
        if Pole[4] == player:
             if Pole[7] == player:
                print('You Win '+ player)
                game = False
    if Pole[2] == player:
        if Pole[5] == player:
             if Pole[8] == player:
                print('You Win '+ player)
                game = False
    
    if Pole[0] == player:
        if Pole[4] == player:
             if Pole[8] == player:
                print('You Win '+ player)
                game = False

    if Pole[2] == player:
        if Pole[4] == player:
             if Pole[6] == player:
                print('You Win '+ player)
                game = False

def schetchik():
    global schet
    global game
    schet = schet + 1
    if schet == 9:
        print ('Ни кто не выиграл')
        game = False


    
def printPole():
    print ("|{},{},{}|\n|{},{},{}|\n|{},{},{}|\n".format(*Pole))

def userChange():
    global player 
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    print ('Ходит игрок ' + player)

def changePole():
    change = True
    global Pole
    global Pole2
    while change == True:
        print ('Вы играете за ' + player)
        x = int(input('Выберите куда будете ходить = '))
        if Pole[x] in Pole2:
            Pole[x] = player
            change = False
          
        else:
            continue
    



while game == True:
    #проверка игрока
    userChange()
    printPole()
    changePole()
    changeWin()
    schetchik()

    #game = False



print ('-----------Конец игры----------')