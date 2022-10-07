'''
Entity Class

Class that handles the physics of all characters in-game.
'''
import arcade
import random

class GameEntity(arcade.Sprite):
    '''
    Base class for all game entities.
    '''
    def __init__(self, name='player', x=0, y=0, stat_scaling=1.0):
        super().__init__()
        self.name = name
        self.pos_x = x
        self.pos_y = y
        self.stat_scaling = stat_scaling
        #Main Stats of the entity
        self.stats = {
            'lvl': 1, #Level: Life level of character
            'str': 1., #Strenth: Phy. Damage
            'agi': 1., #Agility: Phy. Atk. Speed and evasion
            'int': 1., #Intelligence: Mag. Damage
            'stm': 1., #Stamina: Health and Phy. Defense
            #Wisdom: Mana capacity, Mag. Cast Speed,
            #Mag. Defense, and evasion
            'wis': 1., 
        }
        self.update_substat()
        self.set_stat_growth()
        self.bonus_stat = 10

    def package_content(self):
        return {
            'name': self.name,
            'x': self.pos_x,
            'y': self.pos_y,
            'scaling': self.stat_scaling,
            'stat': self.stats,
            'growth': self.stat_growth,
            'bonus': self.bonus_stat
        }
    
    def load_content(self, source, name='player'):
        if name == 'player':
            self.name = source[name]['name']
            self.pos_x = source[name]['x']
            self.pos_y = source[name]['y']
            self.stat_scaling = source[name]['scaling']
            self.stats = source[name]['stat']
            self.stat_growth = source[name]['growth']
            self.bonus_stat = source[name]['bonus']
            self.update_substat()
            
    def add_stat(self, key, value):
        '''
        Add value to selected stat (key) permanently
        '''
        if value > self.bonus_stat:
            self.stats[key] += self.bonus_stat
            self.bonus_stat = 0
        else:
            self.stats[key] += value
            self.bonus_stat -= value
        self.update_substat()

    def add_stat_from_equipment(self, key, value):
        '''
        Increase the stat value based on the equipment properties
        '''
        if key in self.stats.keys():
            self.stats[key] += value
            self.update_substats()
        else:
            self.substats[key] += value

    def update_substat(self):
        '''
        Set the value of substats based on main stats
        '''
        #Sub stats of the entity derives from the current stats
        self.substats = {
            #Property types
            'health': self.stats['stm']*self.stat_scaling * (
                50 + self.stats['lvl']*25
            ), #Damage: 50 + 25*level per scale
            'mana': self.stats['wis']*self.stat_scaling * (
                20 + self.stats['lvl']*3
            ), #Damage: 20 + 3*level per scale
            
            #Damage Types
            'phy_dmg': self.stats['str']*self.stat_scaling * (
                10 + self.stats['lvl']*5
            ), #Damage: 10 + 5*level per scale
            'mag_dmg': self.stats['int']*self.stat_scaling * (
                10 + self.stats['lvl']*7
            ), #Damage: 10 + 7*level per scale
            
            #Defense Types
            'phy_def': self.stats['stm']*self.stat_scaling * (
                5 + self.stats['lvl']*2
            ), #Defense: 5 + 2*level per scale
            'mag_def': self.stats['wis']*self.stat_scaling * (
                5 + self.stats['lvl']*3
            ), #Defense: 5 + 3*level per scale
            
            #Attack Speed Types
            'phy_spd': 1 + self.stats['agi']*self.stat_scaling * (
                self.stats['lvl']*0.005
            ), #Speed: 100% + 0.5%*level per scale
            'mag_spd': 1 + self.stats['wis']*self.stat_scaling * (
                self.stats['lvl']*0.002
            ), #Speed: 100% + 0.2%*level per scale

            #Evasion Types
            'eva': min(
                (self.stats['agi']+self.stats['wis'])*self.stat_scaling /
                (self.stats['agi'] + self.stats['wis'] + 256),
                #Evasion: (agi+wis)/(agi+wis+256) per scale
                0.90 #maximum evasion is 90%
            ),
        }

    def set_stat_growth(
        self,
        strength=1.,
        agility=1.,
        intelligence=1.,
        stamina=1.,
        wisdom=1.,
    ):
        '''
        Stat growth needs to have a total of 5 points.
        Floating points are accepted.
        '''
        assert (strength+agility+intelligence+stamina+wisdom) == 5.0, \
               "Stat growth must be a total of 5 points (float included.)"
        self.stat_growth = {
            'str': strength,
            'agi': agility,
            'int': intelligence,
            'stm': stamina,
            'wis': wisdom,
        }

    def on_level_up(self):
        '''
        Increase stats based on stat growth on level up
        '''
        self.stats['lvl'] += 1
        for k,v in self.stat_growth.items():
            self.stats[k] += v
        self.update_substat()
        self.bonus_stat += 10

    def use_bonus_stat(self, randomize=False):
        '''
        Use up bonus stat based on stat growth.
        Used for mobs to assign stats based on stat growth.
        Random setting available.
        '''
        if not randomize:
            for i in range(0, self.bonus_stat+1, 5):
                for k,v in self.stat_growth.items():
                    self.stats[k] += v
            self.bonus_stat -= i
            
        else:
            add = [random.randint(0, 100) for _ in range(5)] #Randomize 5 stats
            s = sum(add) #Get the aggregate of all values
            #Scale the values as percentage of the remaining bonus stat
            add = [self.bonus_stat*stat/s for stat in add]
            for n,k in enumerate(['str','agi','int','stm','wis']):
                self.stats[k] += add[n]
                
        self.update_substat()


if __name__ == "__main__":
    test = GameEntity('test', 0, 0, 2)
    test.set_stat_growth(2, .5, .5, 1, 1)
    print("Before Distribution:", 
          test.stats,
          test.substats,
          test.bonus_stat,
          sep='\n'
         )
    test.use_bonus_stat()
    print("After Distribution:", 
          test.stats,
          test.substats,
          test.bonus_stat,
          sep='\n'
         )
    test.on_level_up()
    print("After Levelup Distribution:",
          test.stats,
          test.substats,
          test.bonus_stat,
          sep='\n'
         )
    test.use_bonus_stat(True)
    print("After Distribution:", 
          test.stats,
          test.substats,
          test.bonus_stat,
          sep='\n'
         )
