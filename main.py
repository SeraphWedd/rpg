"""
RPG Game

Author: SeraphWedd
Version: 0.1a
"""

import arcade
from Scripts.splash_screen import SplashView
from Scripts.main_menu import MainMenuView

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'RPG $Testing Phase$' #Temp
RESIZABLE = False
RETAIN_ASPECT_RATIO = True
ASPECT_RATIO = 16/9

class MainWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,
                         SCREEN_HEIGHT,
                         SCREEN_TITLE,
                         resizable=RESIZABLE,
                         fullscreen=False,
                         vsync=True)
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
        for k,v in resources.items():
            arcade.resources.add_resource_handle(k, v)

        self.views = {
            'splash'  :SplashView,
            'menu'    :MainMenuView
        }

        self.is_pressed = {}

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    def on_key_press(self, key, modifier):
        self.is_pressed[key] = True
        if (
            self.is_pressed.get(arcade.key.LALT, 0) or
            self.is_pressed.get(arcade.key.RALT, 0)
            ) and (self.is_pressed.get(arcade.key.ENTER, 0)):
                self.is_pressed[arcade.key.ENTER] = False #Avoid false truth
                if RESIZABLE:
                    self.set_fullscreen(not self.fullscreen)

    def on_key_release(self, key, modifier):
        self.is_pressed[key] = False
        
window = None
def main():
    global window
    window = MainWindow()
    window.center_window()
    start_view = SplashView()
    start_view.setup()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
