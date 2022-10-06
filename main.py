"""
RPG Game

Author: SeraphWedd
Version: 0.1a

Constants:
SCREEN_WIDTH: The default width of the game screen
SCREEN_HEIGHT: The default height of the game screen
SCREEN_TITLE: The text on the title bar
RESIZABLE: Allow resizing the game window
FULLSCREEN: Bool to allow/disallow fullscreen mode
VSYNC: Bool to allow/disallow V-Sync
RETAIN_ASPECT_RATIO: Allows window to retain the aspect ratio upon resize
ASPECT_RATIO: Value of aspect ratio to use
OPTIONS_DEFAULT: The default content of the options file
"""

import arcade
import pickle

from Scripts.options import OptionsView
from Scripts.main_menu import MainMenuView
from Scripts.splash_screen import SplashView
from Scripts.continue_view import ContinueView

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'RPG $Testing Phase$' #Temp
RESIZABLE = False
FULLSCREEN = False
VSYNC = True
RETAIN_ASPECT_RATIO = True
ASPECT_RATIO = 16/9
OPTIONS_DEFAULT = {
    'master_volume':1.0,
    'se_volume':1.0,
    'bgm_volume':1.0,
    'text_speed':1.0
}


class MainWindow(arcade.Window):
    """
    Main window to succeed all other view to be used in the game.
    """
    
    def __init__(self):
        super().__init__(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            SCREEN_TITLE,
            resizable=RESIZABLE,
            fullscreen=FULLSCREEN,
            vsync=VSYNC
        )
        resources = {
            #Text
            "Description": "Data/Text/Description",
            "Dialogue": "Data/Text/Dialogue",
            #Maps
            "Tilemap": "Data/Tilemaps",
            #Fonts
            "Font": "Resources/Fonts",
            #Images
            "Character": "Resources/Images/Characters",
            "Item": "Resources/Images/Items",
            "Map": "Resources/Images/Maps",
            "Misc": "Resources/Images/Misc",
            #Sound
            "BGM": "Resources/Sounds/BGM",
            "SE": "Resources/Sounds/SE",
        }
        #Add handles to the above resource paths
        for k,v in resources.items():
            arcade.resources.add_resource_handle(k, v)
            
        self.options = self.read_options()
        #Set value to default when read returns an error
        if len(self.options) == 0:
            self.options = OPTIONS_DEFAULT.copy()
            self.save_options(self.options)
        
        #Main handles for all available views
        self.views = {
            'splash': SplashView,
            'menu': MainMenuView,
            'options': OptionsView,
            'continue': ContinueView,
        }
        #dictionary for holding bool of pressed keys
        self.is_pressed = {}

    def on_resize(self, width, height):
        '''
        If resizing is enabled, the viewport will remain
        in the same aspect ratio/dimension
        '''
        super().on_resize(width, height)
        self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    def on_key_press(self, key, modifier):
        '''
        Set the dictionary value of the key in self.is_pressed to True
        '''
        self.is_pressed[key] = True
        #If user pressed ALT+ENTER, engage/disengage fullscreen mode
        if (
            self.is_pressed.get(arcade.key.LALT, 0) or
            self.is_pressed.get(arcade.key.RALT, 0)
            ) and (self.is_pressed.get(arcade.key.ENTER, 0)):
                self.is_pressed[arcade.key.ENTER] = False #Avoid false truth
                if RESIZABLE:
                    self.set_fullscreen(not self.fullscreen)

    def on_key_release(self, key, modifier):
        '''
        Set the dictionary value of the key in self.is_pressed to False
        '''
        self.is_pressed[key] = False

    def read_options(self, fname='options.cfg'):        
        '''
        Read the pickled value of options from file
        '''
        with open(fname, 'rb') as f:
            opt = pickle.load(f)
        return opt

    def save_options(self, options, fname='options.cfg'):
        '''
        Save the pickled value of self.options to file
        '''
        if not options: #Filter out error on save
            options = self.options
            
        f = open(fname, 'wb')
        pickle.dump(options, f)
        f.close()


#Temp value for debugging
window = None
def main():
    global window #Temp value for debugging
    window = MainWindow()
    window.center_window()
    start_view = SplashView()
    start_view.setup()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
