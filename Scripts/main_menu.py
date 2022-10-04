"""
Main Menu Screen
"""
import arcade
import arcade.gui as ag
from Scripts.transition import TransitionView

class MainMenuView(TransitionView):
    def __init__(self, speed=2):
        super().__init__(speed)
        self.start_fade_in()
        
        arcade.set_background_color(arcade.color.GRAY_BLUE)
        self.px, self.wd, self.py, self.ht = self.window.get_viewport()

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = ag.UIManager()
        self.manager.enable()

        self.v_box = ag.UIBoxLayout()
        self.target_key = 'None'

        #Buttons on the main menu would be
        #New Game, Continue, Options, Credits, Quit
        
        #New Game
        self.new_game_btn = ag.UIFlatButton(
            text='New Game', width=200, height=40,
        )
        self.v_box.add(self.new_game_btn.with_space_around(bottom=20))
        @self.new_game_btn.event("on_click")
        def on_click_new_game(event):
            print("New game!")
            self.target_key = 'new_game'
            self.start_fade_out()
            
        #Continue
        self.continue_btn = ag.UIFlatButton(
            text='Continue', width=200, height=40,
        )
        self.v_box.add(self.continue_btn.with_space_around(bottom=20))
        @self.continue_btn.event("on_click")
        def on_click_continue(event):
            print("Continue!")
            self.target_key = 'continue'
            self.start_fade_out()
            
        #Options
        self.options_btn = ag.UIFlatButton(
            text='Options', width=200, height=40,
        )
        self.v_box.add(self.options_btn.with_space_around(bottom=20))
        @self.options_btn.event("on_click")
        def on_click_options(event):
            print("Options.")
            self.target_key = 'options'
            self.start_fade_out()
            
        #Credits
        self.credits_btn = ag.UIFlatButton(
            text='Credits', width=200, height=40,
        )
        self.v_box.add(self.credits_btn.with_space_around(bottom=20))
        @self.credits_btn.event("on_click")
        def on_click_credits(event):
            print("Credits.")
            #self.target_key = 'credits'
            self.target_key = 'splash'
            self.start_fade_out()
            
        #Quit
        self.quit_btn = ag.UIFlatButton(
            text='Quit', width=200, height=40,
        )
        self.v_box.add(self.quit_btn.with_space_around(bottom=20))
        @self.quit_btn.event("on_click")
        def on_click_quit(event):
            print("Quitting game.")
            self.window.close()
            arcade.exit()

        #Place the widget on-screen
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
        
    
    def on_draw(self):
        arcade.start_render()
        self.manager.draw()

        #These two should always be placed last to allow
        # drawing over all other parts of the view
        self.fade_in() #Only called on starting view
        self.fade_out(
            self.window.views.get(self.target_key, MainMenuView)
        ) #Only called before closing view

    def setup(self):
        pass

    def on_update(self, dt: float):
        self.fade_update(dt)
