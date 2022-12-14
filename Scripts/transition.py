"""
Transition Class

Allows views to transition to and from each other.
"""
import arcade


class TransitionView(arcade.View):
    '''
    TransitionView Class handles fade-in/out transition from one View to
    another.

    :param speed: The speed (in seconds) of the fade-in animation
    '''
    def __init__(self, speed=2):
        super().__init__()
        self.is_fade_in = False
        self.is_fade_out = False
        self.fade_val = 255
        self.fade_rate = 255/speed
        self.status = 'fade_in'
        
    def setup(self):
        '''
        Placeholder for the setup call for inherited class
        '''
        pass

    def on_update(self, dt):
        '''
        Placeholder for the on_update call for inherited class
        '''
        self.fade_update(dt)

    def fade_update(self, dt):
        '''
        Updates the status of the fade-in/out animation
        '''
        if self.status == 'fade_in':
            self.fade_val = max(0, int(self.fade_val - self.fade_rate*dt))
            if not self.fade_val: #Finish fade in
                self.status = 'None'
        if self.status == 'fade_out':
            #Fade out should be quick, so the speed is double of fade_in
            self.fade_val = min(255, int(self.fade_val + self.fade_rate*dt*2))
            if self.fade_val == 255: #Finish fade out
                self.status = 'None'

    def start_fade_in(self):
        '''
        Begin the fade_in animation
        '''
        self.status = 'fade_in'
        self.is_fade_in = True
        self.is_fade_out = False

    def start_fade_out(self):
        '''
        Begin the fade_out animation
        '''
        self.status = 'fade_out'
        self.is_fade_in = False
        self.is_fade_out = True

    def fade_in(self):
        '''
        Slowly decrease alpha of a black screen to unhide current view
        '''
        if self.is_fade_in and self.fade_val:
            arcade.draw_rectangle_filled(
                self.window.width/2, self.window.height/2, #Center
                self.window.width, self.window.height, #Image Size
                (0, 0, 0, self.fade_val) #color and alpha_value
            )
        else:
            self.is_fade_in = False

    def fade_out(self, next_view):
        '''
        Slowly increase alpha of a black screen to hide current view
        '''
        if self.is_fade_out and self.fade_val<=255:
            arcade.draw_rectangle_filled(
                self.window.width/2, self.window.height/2, #Center
                self.window.width, self.window.height, #Image Size
                (0, 0, 0, self.fade_val) #color and alpha_value
            )
            #Check if fade_out ended and transition to next view
            if self.fade_val == 255:
                self.is_fade_out = False
                next_screen = next_view()
                next_screen.setup()
                self.window.show_view(next_screen)
        else:
            self.is_fade_out = False

    def on_key_press(self, key, modifiers):
        '''
        Handle key presses for the transition class
        '''
        #If any key is pressed, by default, skip to fade out
        self.start_fade_out()
