import button
import keyboard as kb
import pyautogui as pg
import ctypes
import pygetwindow as gw

#x=869, y=439
#x=961, y=441
#x=1057, y=422
#=1053, y=532
#x=1051, y=619
#x=963, y=624
#x=873, y=620
#x=8727, y529 

#LOCALIZAR AS POSIÇÔES NA TELA
#while True:
    #print(pg.position())

#POKE_POSITION1 = 958, 628
#POKE_POSITION2 = 861, 631
#POKE_POSITION3 = 857, 533
#POKE_POSITION4 = 857, 438
#POKE_POSITION5 = 957, 437
#POKE_POSITION6 = 1056, 445
#POKE_POSITION7 = 1056, 536
#POKE_POSITION8 = 1056, 630


def check_battle():
    return pg.locateOnScreen('imgs/a.PNG')
    

#is_battle = check_battle()
#print(is_battle)

while True:
    attack = check_battle()
    print('a.PNG')