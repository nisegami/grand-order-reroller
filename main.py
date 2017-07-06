import time
import datetime
import os, os.path
from PIL import Image
from settings import PASSWORD, NAME

############
# Settings #
PAUSE_TIME = 1.5
TIMING_MULT = 1.5
############

import pyautogui
pyautogui.PAUSE = PAUSE_TIME
pyautogui.FAILSAFE = True

HOME_BUTTON = {'x': 1300, 'y': 670}
GO_ICON = {'x': 650, 'y': 380}
CLEAR_DATA_ICON = {'x': 420, 'y': 380}
SKIP_BUTTON = {'x': 1200, 'y': 70}
CONFIRM = {'x': 830, 'y': 600}
ATTACK = {'x': 1125, 'y': 630}
EXCAL = {'x': 400, 'y': 250}
NAME_FIELD = {'x': 900, 'y': 400}
NAME_CONFIRM = {'x': 900, 'y': 500}
NAME_CONFIRM_2 = {'x': 850, 'y': 600}
NEXT = {'x': 1110, 'y': 700}
CLOSE = {'x': 640, 'y': 590}
MENU = {'x': 1190, 'y': 715}
LEFT_EDGE = {'x': 10,'y': 400}

def skip_scene():
    pyautogui.click(**SKIP_BUTTON)
    pyautogui.click(**CONFIRM)

def close_app():
    pyautogui.click(**HOME_BUTTON)
    pyautogui.click(x=1300, y=700)                          # App Switcher
    pyautogui.moveTo(1150, 400)                             # Move Cursor Over GO
    pyautogui.dragTo(1150, 100, button='left')
    time.sleep(TIMING_MULT * 1)

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

def click_until(*images):
    return _roll_click_helper(images, extra_click = False)

def roll_until(*images):
    return _roll_click_helper(images, extra_click = True)

def _roll_click_helper(images, extra_click = False):
    pyautogui.PAUSE = 0.1 * PAUSE_TIME
    while True:
        for image in images:
            if pyautogui.locateCenterOnScreen(
                    os.path.join('screenshots', image + '.png')):
                pyautogui.PAUSE = PAUSE_TIME
                return images.index(image)

        for _ in range(10):
            pyautogui.click(**LEFT_EDGE)

        if extra_click:
            pyautogui.click(**NEXT)

def wait_until(*images):
    pyautogui.PAUSE = 0.1 * PAUSE_TIME
    while True:
        for image in images:
            if pyautogui.locateCenterOnScreen(
                    os.path.join('screenshots', image + '.png')):
                pyautogui.PAUSE = PAUSE_TIME
                return images.index(image)

if __name__ == '__main__':

    while True:

        # First Launch
        pyautogui.click(**HOME_BUTTON)
        pyautogui.click(**GO_ICON)                          # Game Icon

        result = wait_until('tm',
                            'ip_ban',
                            'go_icon',
                            'crash',
                            'relaunch_screen')

        if result == 0:                                     # Main Screen
            pass

        # Failed To Launch?
        elif result == 1:                                   # IP Ban
            close_app()
            time.sleep(600)
            continue

        elif result == 2:                                   # Launcher
            continue

        elif result == 3:                                   # Crash Message
            pyautogui.click(x=990, y=440)
            continue

        elif result == 4:                                   # Launching Again
            close_app()
            pyautogui.click(**CLEAR_DATA_ICON)
            time.sleep(TIMING_MULT * 1)
            continue


        # Setup This Run

        folder_name = os.path.join('rolls',
            datetime.datetime.now().strftime('%y_%m_%d_%H_%M'))

        try:
            os.mkdir(folder_name)
        except:                                             ### WindowsError?
            pass                                            # Anti-pattern justified
                                                            # folder already exists,
                                                            # no action needed.

        # Intro
        pyautogui.click(**CONFIRM)                          # Title Screen
        print(pyautogui.PAUSE)
        pyautogui.click(**CONFIRM)                          # Accept ToS
        wait_until('skip_1')
        skip_scene()
        wait_until('attack')

        # First Battle

        pyautogui.click(**ATTACK)
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('attack')

        pyautogui.click(**ATTACK)
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('attack')

        pyautogui.click(**ATTACK)
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('attack')

        pyautogui.click(**ATTACK)
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(**CONFIRM)
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('attack')

        pyautogui.click(**ATTACK)
        pyautogui.click(**EXCAL)
        select_card(1)
        select_card(2)

        # Story

        wait_until('skip_2')
        skip_scene()
        wait_until('name_prompt')
        pyautogui.click(**NAME_FIELD)
        pyautogui.typewrite(NAME, interval = 0.25)
        pyautogui.click(**NAME_CONFIRM)
        pyautogui.click(**NAME_CONFIRM)
        pyautogui.click(**NAME_CONFIRM_2)

        wait_until('skip_3')
        skip_scene()
        wait_until('mission_select')

        pyautogui.click(x=650, y=390)                       # Mission Select 1
        pyautogui.click(x=1000, y=200)                      # Mission Select 2
        wait_until('skip_4')
        skip_scene()
        wait_until('attack')

        # Second Battle

        pyautogui.click(**ATTACK)
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('attack_dimmed')

        pyautogui.click(x=166, y=607)                       # Mash Ability
        pyautogui.click(x=850, y=460)                       # Confirm
        pyautogui.click(x=644, y=455)                       # Select Target
        time.sleep(TIMING_MULT * 4)

        pyautogui.click(**ATTACK)
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(x=1140, y=90)                       # Battle Speed
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('attack')

        pyautogui.click(**ATTACK)
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('battle_end')
        click_until('next')
        pyautogui.click(**NEXT)

        wait_until('skip_5')
        skip_scene()
        wait_until('saint_quartz_reward')
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(**CONFIRM)
        wait_until('mission_select')

        # Story

        pyautogui.click(x=640, y=430)                       # Mission Select 1
        pyautogui.click(x=1000, y=200)                      # Mission Select 2
        wait_until('skip_6')
        skip_scene()
        wait_until('attack')

        # Third Battle

        pyautogui.click(**ATTACK)
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('attack_dimmed')

        pyautogui.click(x=300, y=330)                       # Change Target
        pyautogui.click(**ATTACK)
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('attack')

        pyautogui.click(**ATTACK)
        select_card(1)
        select_card(2)
        select_card(3)
        wait_until('battle_end')
        click_until('next')
        pyautogui.click(**NEXT)
        wait_until('skip_7')
        skip_scene()
        wait_until('saint_quartz_reward')
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(**CONFIRM)
        time.sleep(TIMING_MULT * 2)

        # Summon

        pyautogui.click(**MENU)                             # Menu Button
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=540, y=680)                       # Summon Button
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=640, y=600)                       # Select 10x Summon
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=830, y=600)                       # Confirm Summon
        roll_until('summon')

        # Finish Tutorial

        pyautogui.click(x=760, y=700)                       # Summon Button
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(**MENU)                             # Menu Button
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(x=170, y=680)                       # Formation Button
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(x=980, y=200)                       # Party Setup
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(x=280, y=380)
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(x=360, y=310)                       # Clear Overlay
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(x=360, y=310)                       # Select Servant
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(**MENU)                             # OK Button
        time.sleep(TIMING_MULT * 5)
        pyautogui.click(x=100, y=75)                        # Close Button
        time.sleep(TIMING_MULT * 5)
        pyautogui.click(x=100, y=75)                        # Close Button

        wait_until('mission_select')
        pyautogui.click(x=640, y=430)                       # Mission Select 1
        pyautogui.click(x=1000, y=200)                      # Mission Select 2
        pyautogui.click(x=1000, y=200)
        pyautogui.click(x=500, y=300)                       # Select Support
        pyautogui.click(**MENU)                             # Start Button

        wait_until('skip_8')
        skip_scene()

        # Final Battle - Non-deterministic

        while True:

            result = wait_until('attack',
                                'battle_end')

            if result == 0:
                pyautogui.click(**ATTACK)
                select_card(1)
                select_card(2)
                select_card(3)
            else:
                break

        # Story

        click_until('next_2')
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(**NEXT)
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=320, y=650)                       # Do Not Request
        wait_until('skip_9')
        skip_scene()
        wait_until('protag')
        pyautogui.click(**CLOSE)
        pyautogui.click(**CLOSE)
        pyautogui.click(**CLOSE)


        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=440, y=700)                       # Gift Box
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=1125, y=330)                      # Recieved Non-Cards
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=100, y=75)                        # Close Button
        time.sleep(TIMING_MULT * 1)

        # Summon

        pyautogui.click(**MENU)                             # Menu Button
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=540, y=680)                       # Summon Button
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=1250, y=65)                       # Close Prompt
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=840, y=600)                       # Select 10x Summon
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=830, y=600)                       # Confirm Summon

        click_until('first_10x_summon_end')
        pyautogui.click(x=1250, y=55)
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(**NEXT)
        roll_until('summon')

        # YOLO Summons

        while True:
            time.sleep(TIMING_MULT * 2)
            pyautogui.click(x=770, y=700)                   # Summon Button
            pyautogui.click(x=450, y=600)                   # 1x Summon

            result_1 = wait_until('not_enough_quartz',
                                'enough_quartz')

            if result_1 == 1:                                 # More Summons
                pyautogui.click(x=830, y=600)               # Confirm Summon
                result_2 = click_until('lock',
                                    'summon_screen_close')
                if result_2 == 0:
                    pyautogui.click(x=50, y=75)             # Close

            else:                                           # No More Summons
                pyautogui.click(x=440, y=600)
                break

        # Second 10x Roll - No Longer Available

        # pyautogui.click(x=770, y=700)                       # Summon Button
        # time.sleep(TIMING_MULT * 1)
        # pyautogui.click(x=840, y=600)                       # Select 10x Summon
        # time.sleep(TIMING_MULT * 1)
        # pyautogui.click(x=830, y=600)                       # Confirm Summon
        # roll_until('summon')

        # Collect Saber Lily

        pyautogui.click(x=110, y=90)                        # Close Prompt
        wait_until('protag')
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(x=440, y=700)                       # Gift Box
        time.sleep(TIMING_MULT * 2)
        pyautogui.click(x=1100, y=250)                      # Receive All
        click_until('lock')
        pyautogui.click(x=50, y=75)                         # Close
        click_until('lock')
        pyautogui.click(x=50, y=75)                         # Close
        pyautogui.click(x=110, y=90)                        # Close Prompt

        # Take Screenshots
        pyautogui.click(**MENU)
        pyautogui.click(x=175, y=675)                       # Formation
        wait_until('prompt_close')
        pyautogui.click(x=1250, y=70)                       # Close
        wait_until('party_setup')
        pyautogui.click(x=1000, y=200)                      # Party Setup
        time.sleep(TIMING_MULT * 1)
        pyautogui.click(x=330, y=330)                       # Open Servants

        for _ in range(6):
            pyautogui.click(x=1125, y=160)                  # Sort by Rarity

        servants = pyautogui.screenshot(
                region=(85, 200, 1130, 540))

        pyautogui.click(x=90, y=70)                         # Close
        pyautogui.click(x=335, y=510)                       # Craft Essences
        wait_until('ce_prompt')
        pyautogui.click(x=1075, y=710)                      # Next
        pyautogui.click(x=1250, y=70)                       # Close
        time.sleep(TIMING_MULT * 1)

        for _ in range(4):
            pyautogui.click(x=1125, y=160)                  # Sort by Rarity

        ces = pyautogui.screenshot(
                region=(70, 400, 1130, 340))

        pyautogui.click(x=90, y=70)                         # Close
        pyautogui.click(x=90, y=70)                         # Close

        results = Image.new('RGB', (1130, 880))
        results.paste(servants, (0, 0))
        results.paste(ces, (0, 540))
        results.save(os.path.join(folder_name,
                                'rolls.png'))

        # Bind Code

        while True:
            pyautogui.click(**MENU)
            pyautogui.click(x=1080, y=680)
            time.sleep(TIMING_MULT * 2)
            while not pyautogui.locateCenterOnScreen(
                    os.path.join('screenshots',
                                 'issue_transfer_number.png')):
                pyautogui.click(x=1260, y=650)              # Scroll
            pyautogui.click(x= 950, y=380)                  # Issue Transfer Number

            if not pyautogui.locateCenterOnScreen(
                os.path.join('screenshots',
                                 'successful_bind_code.png')):

                pyautogui.click(x=800, y=388)
                pyautogui.typewrite(PASSWORD, interval=0.25)
                pyautogui.click(x=800, y=470)
                pyautogui.click(x=800, y=470)
                pyautogui.typewrite(PASSWORD, interval=0.25)
                pyautogui.click(x=640, y=610)
                pyautogui.click(x=640, y=610)

            # In Memory of Account 17_07_05_15_44, we now make SURE
            # that a bind code was issued.

            time.sleep(TIMING_MULT * 5)

            if not pyautogui.locateCenterOnScreen(
                os.path.join('screenshots',
                                 'successful_bind_code.png')):
                # We failed to issue a bind code.
                pyautogui.click(**HOME_BUTTON)
                close_app()
                pyautogui.click(**GO_ICON)
                wait_until('tm')
                pyautogui.click(**GO_ICON)
                wait_until('relaunch_screen')
                pyautogui.click(x=1250, y= 65)              # Close Welcome Screen
                wait_until('protag')
            else:
                break

        bind_code = pyautogui.screenshot(
                region=(530, 330, 270, 70))
        bind_code.save(os.path.join(
                                folder_name, 'bind_code.png'))
        pyautogui.click(x=430, y=600)

        # Clear Data

        close_app()
        pyautogui.click(**CLEAR_DATA_ICON)
        time.sleep(TIMING_MULT * 1)