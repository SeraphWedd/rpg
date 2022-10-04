"""
RPG Game

Author: SeraphWedd
Version: 0.1a
"""

import arcade
from Scripts.splash_screen import SplashView

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'RPG $Testing Phase$' #Temp
RESIZABLE = True
RETAIN_ASPECT_RATIO = True

class MainWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,
                         SCREEN_HEIGHT,
                         SCREEN_TITLE,
                         resizable=RESIZABLE)

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

        self.views = {}

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)


def main():
    window = MainWindow()
    window.center_window()
    start_view = SplashView()
    start_view.setup()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
