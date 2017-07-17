import time
import os, os.path
from roll import Roll, Category, Rarity, possible_summons
from settings import PB_KEY, POINTS_THRESHOLD, IMGUR_ID

CLOSENESS_THRESHOLD = 0.80
DISTANCE_THRESHOLD = 15 # pixels

try:
    from pushbullet import Pushbullet
    pb = Pushbullet(PB_KEY)
    NOTIF_ENABLE = True
except:
    NOTIF_ENABLE = False

try:
    import pyimgur
    im = pyimgur.Imgur(IMGUR_ID)
    IMGUR_ENABLE = True
except:
    IMGUR_ENABLE = False

def record_data(roll):
    if not os.path.isfile('rolls.md'):
        import shutil
        shutil.copyfile('rolls.md.header', 'rolls.md')

    with open('rolls_2.md', 'a') as rolls_file:
        rolls_file.write('| {:03d} | {} | {} | {} | {} | Price | {} | No | {} |\n'.format(
            roll.tally_points(), 
            roll.gen_description_string(categories = [Category.SERVANT], rarities = [Rarity.FIVE_STAR]), 
            roll.gen_description_string(categories = [Category.SERVANT], rarities = [Rarity.FOUR_STAR]), 
            roll.gen_description_string(categories = [Category.CE]), 
            roll.screenshot_url, 
            roll.timestamp,
            roll.notes))

def upload_image(image_path, roll):
    if not IMGUR_ENABLE:
        return

    uploaded_image = None

    while not uploaded_image:
        try:
            uploaded_image = im.upload_image(image_path, title=roll.gen_description_string())
        except:
            time.sleep(5)

    return uploaded_image.link

def send_notif(roll):    
    if not NOTIF_ENABLE:
        return

    points = roll.tally_points()

    try:
        pb.push_note('Roll with {} points.'.format(roll.tally_points()), roll.gen_description_string())
    except:
        # Possibly Rate Limited
        pass                                                        

def filter_matches(points):
    filtered_points = []

    for new_point in points:
        x1, y1 = new_point
        for existing_point in filtered_points:
            x2, y2 = existing_point
            if ((abs(x1 - x2) < DISTANCE_THRESHOLD) 
                    and (abs(y1 - y2) < DISTANCE_THRESHOLD)):
                break
        else:
            filtered_points.append(new_point)

    return filtered_points

def identify_summons(image_path, this_roll = Roll()):
    import cv2
    import numpy as np

    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)

    for summon_data in possible_summons:
        real_name, point_value, category, rarity, file_names = summon_data
        pts = []

        for file_name in file_names:
            template = cv2.imread(
                    os.path.join('screenshots', 
                                 'summons', 
                                 file_name + '.png'), 
                    cv2.IMREAD_GRAYSCALE)

            res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= CLOSENESS_THRESHOLD)
            pts += zip(*loc[::-1])

        for pt in filter_matches(pts):
            this_roll.summons[summon_data] += 1

    return this_roll

def get_data(folder, rolls_folder = 'rolls', gen_link = True):
    if rolls_folder not in folder:
        folder_title = folder
        folder = os.path.join(rolls_folder, folder)
    else: 
        folder_title = folder.replace(rolls_folder, '')

    roll = Roll()
    roll.timestamp = folder_title.split(' - ')[0][1:]

    if os.path.isfile(os.path.join(folder, 'rolls.png')): 
        identify_summons(os.path.join(folder, 'rolls.png'), roll)
        roll.screenshot_url = (upload_image(os.path.join(folder, 'rolls.png'), roll) 
                                    if gen_link else 'Upon Request')

    # Only applicable to a few rolls, I'll tag the useful ones by hand.

    # else:
    #     if os.path.isfile(os.path.join(folder, 'servants.png')):
    #         identify_summons(os.path.join(folder, 'servants.png'), roll)

    #     if os.path.isfile(os.path.join(folder, 'ces.png')):
    #         identify_summons(os.path.join(folder, 'ces.png'), roll)

    #     if os.path.isfile(os.path.join(folder, 'servants.png')):
    #         roll.screenshot_url = upload_image(os.path.join(folder, 'servants.png'), roll)
    #         roll.notes = 'Screenshot does not include CEs, please ask.'

    new_folder = os.path.join(rolls_folder, 
        '{} - {} pts - {}'.format(
            roll.timestamp, 
            roll.tally_points(), 
            roll.gen_description_string()))

    return (new_folder, roll)

def process_roll(folder, rolls_folder = 'rolls'):
    if rolls_folder not in folder:
        folder = os.path.join(rolls_folder, folder)

    # if os.path.isfile(os.path.join(folder, '.done')):
    #     return

    new_name, roll = get_data(folder, rolls_folder)
    os.rename(folder, new_name)
    
    record_data(roll)

    # if roll.anything():
    #     open(os.path.join(new_name, '.done'), 'x').close()

    if roll.tally_points() >= POINTS_THRESHOLD:
        send_notif(roll)

    return (roll)

if __name__ == '__main__':
    rolls_folder = 'rolls'

    NOTIF_ENABLE = False

    for subdir, folders, files in os.walk(rolls_folder):
        for folder in folders:
            process_roll(folder, rolls_folder)
