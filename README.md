# Grand-Order-Reroller
Unattended rerolls for Fate/Grand Order

# Notes about this branch
This branch is experimental, and it is a more involved setup and debugging process than I am comfortable releasing to master and providing support for. Do not expect me to provide assistance this version, although I may still do so depending on your familiarity with this sort of stuff. 

Here is an incomplete list of things you may need to tinker with:
- Provide some form of VPN solution, although it should default to the old 'wait it out' approach if vpn.py is not defined. You can find the API spec in vpn.example.py.
- Change the MEMU_MANAGER_ICON variable to point to the coordinates of the MEmu manager icon on your taskbar, ensure that MEmu manager is in the upper left of the display and ensure that you have only one instance in MEmu manager.

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

However, it is not perfect. This method of rerolling has two major issues:
- It requires mouse focus, so it's diffult to do anything else on the same PC at the same time. I have a laptop that I'm not using right now, so that's what I use for this script.
- Only one instance, as a consequence of the above problem.

# Basic Instructions:
- [Install Python](https://wiki.python.org/moin/BeginnersGuide/Download). This project uses Python3. **Be sure to tick the 'add to path' button during setup.**
- Run `pip install pyautogui numpy opencv-python` to install dependencies.
- Download this repo.
- [Setup MEmu](https://www.reddit.com/r/grandorder/comments/6akkkq/emu_wars_episode_x_return_of_the_emu/)
- [Get Grand Order Image](https://www.reddit.com/r/grandorder/comments/6jompd/modified_memu_image_with_fgo_na_preloaded_and/)
- Setup your MEmu instance as 1280x720 (default) **and make sure it is at 0,0 (upper left) of your screen**.
- [Update Grand Order](https://drive.google.com/file/d/0B8tqm0cp0TuwWWNZRDgwZUFSMmM/view)
- (Optional) Install the Clear Data apk from this repo in MEmu for easy clearing of data.
- Fill in your preferred name and default password into settings.example.py and rename it to settings.py. Ignore other fields for now.
- Open CMD/Shell **as admin** and cd into this repo.
- Run ```python main.py```

# Screenshots
In v3, I switched from PyAutoGUI's image detection to naive computer vision with opencv and numpy. This is much faster and produces much less false negatives. And most importantly for end users, it does not require you to retake all screenshots. 

# Notes
- You can adjust the timings for all time.sleep() calls and the delay between PyAutoGUI actions with the TIMING_MULT and PAUSE_TIME variables respectively.
- I recommend using a VPN to avoid IP bans. Ideally a fully unattended setup would try to get a new IP by disconnecting from and reconnecting to the VPN, but it doesn't do that yet.
- Possible issues:
  - There have been instances where bind codes have been lost due to an unknown issue. Because of the rarity of the problem, I am unable to determine the cause. However, after losing an account I quite liked, I decided to implement some additional checks that should correct the issue should it occur.
- I just rolled an Altria/Gil account while writing this. Nice. Update: decided to main that account for now.
  
# Clearing Data
There's an apk included in this repo. If you install that apk then click the icon, it will clear the data and allow you to reroll without downloading any data or messing in ES File Exporer. The script assumes you will have this apk installed and its icon will be located on the home screen directly to the left of the Grand Order icon's default position in the ova linked above.

# Roll Tagging and Notifications
As of v3, there is now a roll tagging feature that will inspect rolls and provide some information about the summons in that roll. Right now, in order to avoid conflicting with the main purpose of the script, this functionality is in its own file, `roll_handler.py`. 

Running `python roll_handler.py` will scan the rolls folder every two minutes for completed but untagged rolls and will rename the folder to reflect what it found. 

If you install Pushbullet.py with `pip install pushbullet.py` and set your [API Key](https://docs.pushbullet.com/v1/) in `settings.py`, then you will also be notified of good rolls.

Be aware that there is no detection of duplicate rolls at this time.



