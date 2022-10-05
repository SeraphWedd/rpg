"""
Splash screen
"""
import arcade
import random
from Scripts.transition import TransitionView

class SplashView(TransitionView):
    def __init__(self, speed=2):
        super().__init__(speed)
        self.start_fade_in()
        self.acc_timer = 0
        self.view_time = 5 #seconds
        arcade.set_background_color(arcade.color.BLUE_GRAY)
        self.shadow_size = 3
        self.px, self.wd, self.py, self.ht = self.window.get_viewport()
        
        #arcade.load_font(":Font:BeautyMountainsPU-od7z.ttf")
        self.title = arcade.create_text_sprite(
            "SeraphGames",
            -self.wd * 0.5,
            self.ht * 0.5,
            arcade.color.AERO_BLUE,
            font_size=100,
            width=self.wd,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )
        self.shadow = arcade.create_text_sprite(
            "SeraphGames",
            -self.wd * 0.5+self.shadow_size,
            self.ht * 0.5-self.shadow_size,
            arcade.color.BLACK_OLIVE,
            font_size=100,
            width=self.wd,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )

    def on_draw(self):
        self.clear()
        self.shadow.draw()
        self.title.draw()

        #These two should always be placed last to allow
        # drawing over all other parts of the view
        self.fade_in() #Only called on starting view
        self.fade_out(self.window.views['menu']) #Only called before closing view

    def setup(self):
        pass

    def on_update(self, dt: float):
        x, y = self.title.position
        self.title.set_position(min(self.wd*.5, x+500*dt), y)
        x, y = self.shadow.position
        self.shadow.set_position(
            min(self.wd*.5+self.shadow_size, x+500*dt), y)
        self.fade_update(dt)

        #Add point to fade out
        if self.acc_timer < self.view_time:
            self.acc_timer += dt
        else:
            self.start_fade_out()
