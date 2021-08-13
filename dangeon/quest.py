
from random import shuffle

pName = input('Здарова, как звать?')
print ('Привет ' + pName)
typeEnemys = [1, 2, 3]

HELP = """Доступные команды:
help = напечатать справку
c,ю,з,в = передвижение
inv = показать инвентарь
atac = атаковать кого либо
"""
INV = """Инвентарь:
-Пока у Вас ни чего нет 
"""




class Player():
    hp = 100
    mana = 100
    armor = 0
    damage = 1
    spas = 0
    
    def __init__(self):
        
        pass

class Monster():
    hp = 100
    mana = 100
    armor = 0
    damage = 1
    spas = 0

    def __init__(self):
        
        pass

class Room():
    rExit = True


    def __init__(self):
        
        pass




'''def x:
    return shuffle(typeEnemys)'''
    

    
    
print (HELP)


while True:
    command = input('Введите команду:')
    if command == 'help':
        print(HELP)
    elif command == 'inv':
        print(INV)
    
    elif command == 'exit':
        print('Спасибо за игру! До свидания!')
        break
    else:
        print('Неизвестная команда - ', command)
        


