"""
Splash screen

Displays the company logo/name on spash screen.
(Just my name for now)
"""
import arcade

from Scripts.transition import TransitionView


class SplashView(TransitionView):
    def __init__(self, speed=2):
        super().__init__(speed)
        #Initialize fade_in on start
        self.start_fade_in()
        #Initialize timer for the duration of splash screen
        self.acc_timer = 0
        self.view_time = 5
        #Set the background color of the view
        arcade.set_background_color(arcade.color.BLUE_GRAY)

    def setup(self):
        #Set shadow size of the text
        self.shadow_size = 3
        #Get the size of the current viewport
        self.px, self.wd, self.py, self.ht = self.window.get_viewport()
        
        #arcade.load_font(":Font:BeautyMountainsPU-od7z.ttf")
        #Set the main title as a text sprite
        self.title = arcade.create_text_sprite(
            "SeraphGames",
            -self.wd * 0.5, #Starts from outside of the screen
            self.ht * 0.5,
            arcade.color.AERO_BLUE,
            font_size=100,
            width=self.wd,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )
        #Create a shadow of the text shifted by shadow_size
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
        '''
        Function called to draw all sprites and images to screen
        The first to be called will be at the bottom most while
        the last to be called will be on top.
        '''
        self.clear()
        self.shadow.draw()
        self.title.draw()

        #These two should always be placed last to allow
        # drawing over all other parts of the view
        self.fade_in() #Only called on starting view
        self.fade_out(self.window.views['menu']) #Only called before closing view


    def on_update(self, dt: float):
        #Move the text at a speed of 500px/sec to the right
        x, y = self.title.position
        self.title.set_position(min(self.wd*.5, x+500*dt), y)
        x, y = self.shadow.position
        self.shadow.set_position(
            min(self.wd*.5+self.shadow_size, x+500*dt), y)
        #Update fade animation (if active)
        self.fade_update(dt)

        #Add point to counter before fade out
        if self.acc_timer < self.view_time:
            self.acc_timer += dt
        else:
            self.start_fade_out()
