'''
Continue Class

Contains the method to load game from save file and pass it to
the new game class.
'''

import arcade

from Scripts.transition import TransitionView


class ContinueView(TransitionView):
    def __init__(self, speed=1):
        super().__init__(speed)
        #Initialize fade_in on start
        self.start_fade_in()
        #Set the background color of the view
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def setup(self):
        self.px, self.wd, self.py, self.ht = self.window.get_viewport()
        #Set title 1 Main Text
        self.title_1 = arcade.create_text_sprite(
            "Save File 1",
            self.wd * 0.25,
            self.ht * 0.9,
            arcade.color.AERO_BLUE,
            font_size=24,
            width=self.wd,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )
        #Set title 2 Main Text
        self.title_2 = arcade.create_text_sprite(
            "Save File 2",
            self.wd * 0.75,
            self.ht * 0.9,
            arcade.color.AERO_BLUE,
            font_size=24,
            width=self.wd,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )
        #Set title 1 Shadow Text
        self.title_1_sd = arcade.create_text_sprite(
            "Save File 1",
            self.wd * 0.25+2,
            self.ht * 0.9-2,
            arcade.color.DARK_BLUE,
            font_size=24,
            width=self.wd,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )
        #Set title 2 Shadow Text
        self.title_2_sd = arcade.create_text_sprite(
            "Save File 2",
            self.wd * 0.75+2,
            self.ht * 0.9-2,
            arcade.color.DARK_BLUE,
            font_size=24,
            width=self.wd,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )

    def draw_sf_boxes(self, shadow=0, color=arcade.color.BLACK_BEAN):
        '''
        Draws two boxes as design on the screen

        :param shadow: The amount of offset the box will have
        :param color: The color of the box
        '''
        self.sf_box_1 = arcade.draw_rectangle_filled(
            self.wd*.25+shadow,
            self.ht*.45-shadow,
            self.wd*.4,
            self.ht*.75,
            color
        )
        self.sf_box_2 = arcade.draw_rectangle_filled(
            self.wd*.75+shadow,
            self.ht*.45-shadow,
            self.wd*.4,
            self.ht*.75,
            color
        )
        
    def on_draw(self):
        self.clear()
        #Draw the text shadows
        self.title_1_sd.draw()
        self.title_2_sd.draw()
        #Draw the main text over the shadows
        self.title_1.draw()
        self.title_2.draw()
        #Draw the box shadow with offset
        self.draw_sf_boxes(4)
        #Draw the actual box over the shadow without offset
        self.draw_sf_boxes(color=arcade.color.LIGHT_BROWN)

        #These two should always be placed last to allow
        # drawing over all other parts of the view
        self.fade_in() #Only called on starting view
        
        #The content of fade will change based on the selection
        #choices are selecting a save file leading to the game, or
        #to return to the main menu
        self.fade_out(self.window.views['menu'])#Temporary

    def on_key_press(self, key, modifier):
        if key == arcade.key.ESCAPE:
            self.start_fade_out()
