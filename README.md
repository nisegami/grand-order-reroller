# Grand-Order-Reroller
Automated rerolls for Fate/Grand Order

This should work fairly okay as it is, but I will continue working on it for a while and will hopefully improve it.


# Basic Instructions:
- [Install Python](https://wiki.python.org/moin/BeginnersGuide/Download). This project uses Python3.
- [Install PyAutoGUI](http://pyautogui.readthedocs.io/en/latest/install.html)
- Clone this repo.
- [Setup MEmu](https://www.reddit.com/r/grandorder/comments/6akkkq/emu_wars_episode_x_return_of_the_emu/)
- [Get Grand Order Image](https://www.reddit.com/r/grandorder/comments/6jompd/modified_memu_image_with_fgo_na_preloaded_and/)
- (Optional) Install the Clear Data apk from this repo in MEmu for easy clearing of data.
- Setup your MEmu instance as 1280x720 (default) **and make sure it is at 0,0 (upper left) of your screen**.
- Open CMD/Shell **as admin** and cd into this repo.
- Run ```python main.py```

# Notes
- Right now I am hard coding timings, depending on your machine, it may not be accurate.
- There are some janky parts of this script:
  - Summoning Servants is hard to get the timing right because it depends on what you summon. I attempt to handle it by looking for the summon button that appears after the tutorial 10 roll, but I just end the script after doing the second 10 roll.
  - Some parts of this script reply on looking for small images on the screen while waiting for something to happen. If those things never trigger for you, play through once and replace my screenshots with ones from your instance as closely as you can.
  - There is a small chance that at the end of the fourth and final battle, depending on what servants you roll/get as support and what cards you get, that the battle may not end when the script thinks it will. It usually does, but if that happens, just exit the script and continue normally. 
  
# Clearing Data
There's an apk included in this repo. If you install that apk then click the icon, it will clear the data and allow you to reroll without downloading any data or messing in ES File Exporer. It does not currently prompt you or notify you that anything happens. I'll fix that eventually, but in the meanwhile be careful if you use it.


