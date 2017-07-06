# Grand-Order-Reroller
Unattended rerolls for Fate/Grand Order

# Why It Exists
I know MEmu has macro support, but if you ask anyone who uses it, you'll hear that they only automate up until the tutorial 10-roll because the fourth fight is non-determinisitic. You will also hear tips like leaving a lot of time between actions to account for variations in timing, which lengthens the time it takes for you to do a run. Also, in my experience, using MEmu's macros drastically reduced the stability of MEmu. 

This script solves some of those problems:
- Completely unattended unless MEmu crashes (for now).
- Saves all accounts + rolls in a convinient format for easy access.
- can handle non-deterministic events.
  - can handle a variable number of yolo-rolls at the end.
  - can handle a variable number of turns in the fourth battle.
  - can naively handle things like IP bans (right now, just wait it out).
- Improved stability, since MEmu isn't doing anything extra.
- Ability to change and edit the script without redoing the entire macro, this script can easily be updated to account for changes in the tutorial in the future.

# Basic Instructions:
- [Install Python](https://wiki.python.org/moin/BeginnersGuide/Download). This project uses Python3.
- [Install PyAutoGUI](http://pyautogui.readthedocs.io/en/latest/install.html)
- Clone/download this repo.
- [Setup MEmu](https://www.reddit.com/r/grandorder/comments/6akkkq/emu_wars_episode_x_return_of_the_emu/)
- [Get Grand Order Image](https://www.reddit.com/r/grandorder/comments/6jompd/modified_memu_image_with_fgo_na_preloaded_and/)
- Setup your MEmu instance as 1280x720 (default) **and make sure it is at 0,0 (upper left) of your screen**.
- [Update Grand Order](https://drive.google.com/file/d/0B8tqm0cp0TuwWWNZRDgwZUFSMmM/view)
- (Optional) Install the Clear Data apk from this repo in MEmu for easy clearing of data.
- Play through the tutorial once and take all the necessary screenshots (see below).
- Fill in your preferred name and default password into settings.example.py and rename to settings.py.
- Open CMD/Shell **as admin** and cd into this repo.
- Run ```python main.py```

# Screenshots
PyAutoGUI is very fickle with using screenshots to detect elements on the screen. Even if you keep all the settings the same, it seems to only work with screenshots taken on that machine. In v1, I relied minimally on this feature as a result, but in an effort to minimize the time it takes to do a roll, I have chosen to use this feature for most things.

You can see what screenshots you need in the screenshots folder. I recommend sticking as close as possible to the choices I have made in what parts of the screen to capture.

# Notes
- You can adjust the timings for all time.sleep() calls and the delay between PyAutoGUI actions with the TIMING_MULT and PAUSE_TIME variables respectively.
- I recommend using a VPN to avoid IP bans. Ideally a fully unattended setup would try to get a new IP by disconnecting from and reconnecting to the VPN, but it doesn't do that yet.
- Possible issues:
  - IP ban handling may not work, it is hard to test.
  - There have been instances where bind codes have been lost due to an unknown issue. Because of the rarity of the problem, I am unable to determine the cause. However, after losing an account I quite liked, I decided to implement some additional checks that should correct the issue should it occur.
  - Yolo-summons (1x rolls) are quite hard to implement. If you encounter problems, the best solution right now may be to just comment out that section of code.
- I just rolled an Altria/Gil account while writing this. Nice.
  
# Clearing Data
There's an apk included in this repo. If you install that apk then click the icon, it will clear the data and allow you to reroll without downloading any data or messing in ES File Exporer. The script assumes you will have this apk installed and its icon will be located on the home screen directly to the left of the Grand Order icon's default position in the ova linked above.



