import arcade
from Scripts.transition import TransitionView

class ContinueView(TransitionView):
    def __init__(self, speed=1):
        super().__init__(speed)
        self.start_fade_in()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        
        self.px, self.wd, self.py, self.ht = self.window.get_viewport()
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
        self.title_1_sd.draw()
        self.title_2_sd.draw()
        self.title_1.draw()
        self.title_2.draw()
        self.draw_sf_boxes(4)
        self.draw_sf_boxes(color=arcade.color.LIGHT_BROWN)

        #These two should always be placed last to allow
        # drawing over all other parts of the view
        self.fade_in() #Only called on starting view
        self.fade_out(self.window.views['menu']) #Only called before closing view

    def on_key_press(self, key, modifier):
        if key == arcade.key.ESCAPE:
            self.start_fade_out()
