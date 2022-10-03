"""
Splash screen
"""
import arcade

class SplashView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLUE_GRAY)
        self.shadow_size = 3
        #arcade.load_font(":Font:BeautyMountainsPU-od7z.ttf")
        self.title = arcade.create_text_sprite(
            "SeraphGames",
            -self.window.width * 0.5,
            self.window.height * 0.5,
            arcade.color.AERO_BLUE,
            font_size=100,
            width=self.window.width,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )
        self.shadow = arcade.create_text_sprite(
            "SeraphGames",
            -self.window.width * 0.5+self.shadow_size,
            self.window.height * 0.5-self.shadow_size,
            arcade.color.BLACK_OLIVE,
            font_size=100,
            width=self.window.width,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )

    def on_draw(self):
        arcade.start_render()
        self.shadow.draw()
        self.title.draw()   

    def setup(self):
        pass

    def on_update(self, dt: float):
        x, y = self.title.position
        self.title.set_position(min(self.window.width*.5, x+500*dt), y)
        x, y = self.shadow.position
        self.shadow.set_position(
            min(self.window.width*.5+self.shadow_size, x+500*dt), y)
