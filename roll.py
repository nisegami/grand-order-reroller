from enum import Enum

class Category(Enum):
    SERVANT = 1
    CE = 2

class Rarity(Enum):
    FOUR_STAR = 4
    FIVE_STAR = 5


class Roll():
    def __init__(self):
        self.summons = {x: 0 for x in possible_summons}
        self.timestamp = ''
        self.total_points = 0
        self.screenshot_url = ''
        self.notes = '-'

    def gen_description_string(self, 
                               categories = [Category.SERVANT, Category.CE],
                               rarities = [Rarity.FOUR_STAR, Rarity.FIVE_STAR]):
        items = []
        for (real_name, _, category, rarity, _), count in self.summons.items():

            if ((not count) 
                    or (category not in categories) 
                    or (rarity not in rarities)):
                continue

            if count == 1:
                items.append(real_name)
            else:
                items.append('{}x {}'.format(count, real_name))

        desc = ', '.join(items)
        return desc if desc else '-'

    def tally_points(self):    
        self.total_points = 0    
        for (_, point_value, *_), count in self.summons.items():
            if not count:
                continue

        self.total_points += (count * point_value)
        return self.total_points

    def anything(self):
        return sum(self.summons.values())

possible_summons = [
    # Five Star Servants
    ('Waver', 200, Category.SERVANT, Rarity.FIVE_STAR, ('waver',)),
    ('Gilgamesh', 200, Category.SERVANT, Rarity.FIVE_STAR, ('gil', 'gil_large')),
    ('Arturia', 200, Category.SERVANT, Rarity.FIVE_STAR, ('saber', 'saber_large')),
    ('Jeanne', 150, Category.SERVANT, Rarity.FIVE_STAR, ('jeanne', 'jeanne_large')),
    ('Altera', 100, Category.SERVANT, Rarity.FIVE_STAR, ('altera',)),
    ('Vlad', 100, Category.SERVANT, Rarity.FIVE_STAR, ('vlad', 'vlad_large')),

    # Four Star Servants
    ('Heracles', 50, Category.SERVANT, Rarity.FOUR_STAR, ('herc', 'herc_large')),
    ('EMIYA', 50, Category.SERVANT, Rarity.FOUR_STAR, ('emiya', 'emiya_large')),
    ('Liz', 40, Category.SERVANT, Rarity.FOUR_STAR, ('liz', 'liz_large')),
    ('Lancelot', 40, Category.SERVANT, Rarity.FOUR_STAR, ('lancelot', 'lancelot_large')),
    ('Tamano-cat', 40, Category.SERVANT, Rarity.FOUR_STAR, ('tamacat', 'tamacat_large')),
    ('Siegfried', 40, Category.SERVANT, Rarity.FOUR_STAR, ('sieg', 'sieg_large')),
    ('Atalanta', 20, Category.SERVANT, Rarity.FOUR_STAR, ('atalanta', 'atalanta_large')),
    ('Saber Lily', 0, Category.SERVANT, Rarity.FOUR_STAR, ('lily', 'lily_large')),

    # Five Star CEs
    ('Kaleidoscope', 60, Category.CE, Rarity.FIVE_STAR, ('scope', 'scope_large')),
    ('Limited.Over Zero', 50, Category.CE, Rarity.FIVE_STAR, ('loz',)),
    ('Heaven\'s Feel', 45, Category.CE, Rarity.FIVE_STAR, ('hf', 'hf_large')),
    ('Formal Craft', 40, Category.CE, Rarity.FIVE_STAR, ('craft',)),
    ('Prisma Cosmos', 40, Category.CE, Rarity.FIVE_STAR, ('prisma', 'prisma_large')),
    ('Imaginary Around', 30, Category.CE, Rarity.FIVE_STAR, ('around',)),

    # Four Star CEs
    ('The Imaginary Element', 30, Category.CE, Rarity.FOUR_STAR, ('element',))
]