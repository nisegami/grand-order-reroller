import time
import os, os.path
from pushbullet import Pushbullet
from settings import PB_KEY, POINTS_THRESHOLD

CLOSENESS_THRESHOLD = 0.8
pb = Pushbullet(PB_KEY)

possible_summons = {
    'waver': (200, 'Waver'),
    'gil': (200, 'Gilgamesh'),
    'gil_large': (200, 'Gilgamesh'),
    'saber': (200, 'Arturia'),
    'saber_large': (200, 'Arturia'),
    'jeanne': (150, 'Jeanne'),
    'jeanne_large': (150, 'Jeanne'),
    'altera': (100, 'Altera'),
    'vlad': (100, 'Vlad'),
    'vlad_large': (100, 'Vlad'),
    'scope': (60, 'Kaleidoscope'),
    'scope_large': (60, 'Kaleidoscope'),
    'herc': (50, 'Heracles'),
    'herc_large': (50, 'Heracles'),
    'emiya': (50, 'EMIYA'),
    'emiya_large': (50, 'EMIYA'),
    'loz': (45, 'Limited.Over Zero'),
    'loz_large': (45, 'Limited.Over Zero'),
    'hf': (45, 'Heaven\'s Feel'), 
    'hf_large': (45, 'Heaven\'s Feel'),   
    'liz': (40, 'Elizabeth'),   
    'liz_large': (40, 'Elizabeth'), 
    'sieg': (40, 'Siegfried'),
    'sieg_large': (40, 'Siegfried'),
    'craft': (40, 'Formal Craft'),
    'lancelot': (40, 'Lancelot'),
    'lancelot_large': (40, 'Lancelot'),
    'prisma': (40, 'Prisma Cosmos'),
    'prisma_large': (40, 'Prisma Cosmos'),
    'tamacat': (40, 'Tamano-cat'),
    'tamacat_large': (40, 'Tamano-cat'),
    'around': (30, 'Imaginary Around'),
    'atalanta': (20, 'Atalanta'),
    'atalanta_large': (20, 'Atalanta'),
    'lily': (0, 'Saber Lily'),
    'lily_large': (0, 'Saber Lily')
}

def send_notif(points, summons):
    pb.push_note('Roll with {} points.'.format(points), ', '.join(summons))
    time.sleep(2)

def identify_summons(image_path):
    import cv2
    import numpy as np

    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
    summons = []
    points = 0

    for file_name, (point_value, actual_name) in possible_summons.items():
        template = cv2.imread(os.path.join('screenshots', 'summons', file_name + '.png'), cv2.IMREAD_GRAYSCALE)

        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= CLOSENESS_THRESHOLD)

        for pt in zip(*loc[::-1]):

            # Due to weird behaviour, only add one instance of each summon
            if actual_name in summons:
                continue
            summons.append(actual_name)
            points += point_value

    return (summons, points) 

def rename_folder(folder, rolls_folder = 'rolls'):
    if rolls_folder not in folder:
        folder = os.path.join(rolls_folder, folder)

    if os.path.isfile(os.path.join(folder, '.done')):
        return

    new_name, summons, points = gen_new_folder_name(folder, rolls_folder)
    new_name = os.path.join(rolls_folder, new_name)
    os.rename(folder, new_name)

    if summons:
        open(os.path.join(new_name, '.done'), 'x').close()

    if points >= POINTS_THRESHOLD:
        send_notif(points, summons)

    return (summons, points)

def gen_new_folder_name(folder, rolls_folder = 'rolls'):
    if rolls_folder not in folder:
        folder_title = folder
        folder = os.path.join(rolls_folder, folder)
    else: 
        folder_title = folder.replace(rolls_folder, '')
    
    timestamp = folder_title.split(' - ')[0]
    summons, points = [], 0

    if os.path.isfile(os.path.join(folder, 'rolls.png')): 
        summons, points = identify_summons(os.path.join(folder, 'rolls.png'))

    else:
        if os.path.isfile(os.path.join(folder, 'servants.png')):
            summons_servants, points_servants = identify_summons(os.path.join(folder, 'servants.png'))
            summons += summons_servants
            points += points_servants
        if os.path.isfile(os.path.join(folder, 'ces.png')):
            summons_ces, points_ces = identify_summons(os.path.join(folder, 'ces.png'))
            summons += summons_ces
            points += points_ces

    new_folder = os.path.join(rolls_folder, '{} - {} pts - {}'.format(timestamp, points, (', '.join(summons) if points else 'Shit Roll')))[1:]

    return (new_folder, summons, points)

if __name__ == '__main__':
    rolls_folder = 'rolls'

    while True:
        try:
            for subdir, folders, files in os.walk(rolls_folder):
                for folder in folders:
                    rename_folder(folder, rolls_folder)
        except Exception as e:
            pb.push_note('Ay Arshad, we fucked up - Mal', repr(e))
        time.sleep(120)
