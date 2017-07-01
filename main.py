import time

import pyautogui
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

HOME_BUTTON = {'x': 1300, 'y': 670}
GO_ICON = {'x': 650, 'y': 380}
TERM_ICON = {'x': 420, 'y': 380}
SKIP_BUTTON = {'x': 1200, 'y': 70}
CONFIRM = {'x': 830, 'y': 600}
ATTACK = {'x': 1125, 'y': 630}
EXCAL = {'x': 400, 'y': 250}
NAME_FIELD = {'x': 900, 'y': 400}
NAME_CONFIRM = {'x': 900, 'y': 500}
NAME_CONFIRM_2 = {'x': 850, 'y': 600}
NEXT = {'x': 1100, 'y': 700}
CLOSE = {'x': 640, 'y': 590}

def press_home():
    pyautogui.click(**HOME_BUTTON)

def skip_scene():
    pyautogui.click(**SKIP_BUTTON)
    pyautogui.click(**CONFIRM)

def select_card(card_no):
    if card_no == 1:
        x = 140
    elif card_no == 2:
        x = 390
    elif card_no == 3:
        x = 650
    elif card_no == 4:
        x = 900
    else:
        x = 1160

    pyautogui.click(x=x, y=530)

def wait_until(image):
    while True:
        if pyautogui.locateCenterOnScreen(image):
            return 

if __name__ == '__main__':

    # First Launch
    press_home()
    pyautogui.click(**GO_ICON)      # Game Icon   
    wait_until('tm.png')

    # Intro
    pyautogui.click(**GO_ICON)       # Title Screen
    pyautogui.click(**CONFIRM)       # Accept ToS
    time.sleep(5)
    skip_scene()
    time.sleep(20)


    # First Battle

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(28)

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(28)

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(28)

    pyautogui.click(**ATTACK)
    time.sleep(2)
    pyautogui.click(**CONFIRM)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(28)

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    pyautogui.click(**EXCAL)
    time.sleep(45)

    # Story

    skip_scene()
    time.sleep(8)
    pyautogui.click(**NAME_FIELD)
    pyautogui.typewrite('Mal', interval = 0.25)   
    pyautogui.click(**NAME_CONFIRM)
    pyautogui.click(**NAME_CONFIRM)

    pyautogui.click(**NAME_CONFIRM_2)

    time.sleep(3)
    skip_scene()
    time.sleep(20)

    pyautogui.click(x=650, y=390)   # Mission Select 1
    pyautogui.click(x=1000, y=200)  # Mission Select 2
    time.sleep(5)
    skip_scene()
    time.sleep(20)

    # Second Battle

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(20)

    pyautogui.click(x=166, y=607) # Mash Ability
    pyautogui.click(x=850, y=460) # Confirm
    pyautogui.click(x=644, y=455) # Select Target
    time.sleep(4)

    pyautogui.click(**ATTACK)
    time.sleep(2)
    pyautogui.click(x=1140, y=90) # Battle Speed
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(20)

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(20)    

    pyautogui.click(**CONFIRM)
    time.sleep(2)
    pyautogui.click(**CONFIRM)
    time.sleep(2)
    pyautogui.click(**NEXT)
    time.sleep(8)
    skip_scene()
    time.sleep(8)
    pyautogui.click(**CONFIRM)
    time.sleep(2)

    # Story

    pyautogui.click(x=640, y=430)   # Mission Select 1
    pyautogui.click(x=1000, y=200)  # Mission Select 2
    time.sleep(8)
    skip_scene()
    time.sleep(20)

    # Third Battle

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(20)   

    pyautogui.click(x=300, y=330) # Change Target00
    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(15)

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(20)    

    pyautogui.click(**CONFIRM)
    time.sleep(2)
    pyautogui.click(**CONFIRM)
    time.sleep(2)
    pyautogui.click(**NEXT)
    time.sleep(8)
    skip_scene()
    time.sleep(8)
    pyautogui.click(**CONFIRM)
    time.sleep(2)

    # Summon

    pyautogui.click(x=1190, y=715)  # Menu Button
    time.sleep(1)
    pyautogui.click(x=540, y=680)   # Summon Button
    time.sleep(1)
    pyautogui.click(x=640, y=600)   # Select 10x Summon   
    time.sleep(1) 
    pyautogui.click(x=830, y=600)   # Confirm Summon

    while True:
        pyautogui.click(x=1070, y=700)
        pyautogui.click(x=1070, y=700)
        pyautogui.click(x=1070, y=700)
        if pyautogui.locateCenterOnScreen('summon.png'):
            break

    # Finish Tutorial

    pyautogui.click(x=760, y=700)   # Summon Button
    pyautogui.click(x=1190, y=715)  # Menu Button
    pyautogui.click(x=170, y=680)   # Formation Button
    pyautogui.click(x=980, y=200)   # Party Setup
    pyautogui.click(x=280, y=380)   # ??
    pyautogui.click(x=360, y=310)   # Clear Overlay
    pyautogui.click(x=360, y=310)   # Select Servant
    pyautogui.click(x=1190, y=715)  # OK Button
    time.sleep(1)
    pyautogui.click(x=100, y=75)    # Close Button
    time.sleep(1)
    pyautogui.click(x=100, y=75)    # Close Button

    time.sleep(1)

    pyautogui.click(x=640, y=430)   # Mission Select 1
    pyautogui.click(x=1000, y=200)  # Mission Select 2
    pyautogui.click(x=1000, y=200)  
    pyautogui.click(x=500, y=300)   # Select Support 
    pyautogui.click(x=1190, y=715)  # Start Button

    time.sleep(4)
    skip_scene()
    time.sleep(20)

    # Final Battle    

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(28)   

    pyautogui.click(**ATTACK)
    select_card(1)
    select_card(2)
    select_card(3)
    time.sleep(28)   

    # Story

    pyautogui.click(x=830, y=600)  # Advance Game
    time.sleep(3)
    pyautogui.click(x=830, y=600)  # Advance Game
    pyautogui.click(x=830, y=600)  # Advance Game
    pyautogui.click(**NEXT)
    time.sleep(1)
    pyautogui.click(x=320, y=650)  # Do Not Request
    time.sleep(5)
    skip_scene()
    time.sleep(5)
    pyautogui.click(**CLOSE)
    pyautogui.click(**CLOSE)
    pyautogui.click(**CLOSE)

    pyautogui.click(x=440, y=700)   # Gift Box
    time.sleep(1)
    pyautogui.click(x=1125, y=330)  # Recieved Non-Cards
    time.sleep(1)
    pyautogui.click(x=100, y=75)    # Close Button

    # Summon

    pyautogui.click(x=1190, y=715)  # Menu Button
    time.sleep(1)
    pyautogui.click(x=540, y=680)   # Summon Button
    time.sleep(1)
    pyautogui.click(x=1250, y=65)   # Close Prompt
    time.sleep(1)
    pyautogui.click(x=840, y=600)   # Select 10x Summon   
    time.sleep(1) 
    pyautogui.click(x=830, y=600)   # Confirm Summon


    while True:
        pyautogui.click(x=1070, y=700)
        pyautogui.click(x=1070, y=700)
        pyautogui.click(x=1070, y=700)
        if pyautogui.locateCenterOnScreen('craft.png'):
            break

    pyautogui.click(x=1250, y=65)   # Close Prompt
    pyautogui.click(x=1070, y=700)  # Click Next

    print("Done")