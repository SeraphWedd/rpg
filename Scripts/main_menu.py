"""
Main Menu Screen

Main junction of the game. Connects to all the other views of the game.
"""
import mouse
import arcade
import arcade.gui as ag

from Scripts.transition import TransitionView


class MainMenuView(TransitionView):
    def __init__(self, speed=1):
        super().__init__(speed)
        #Initialize fade_in on start
        self.start_fade_in()
        #Set the background color of the view
        arcade.set_background_color(arcade.color.GRAY_BLUE)
        
    def setup(self):
        '''
        Setup for the Main Menu.
        '''
        #Set the target_key or the key/name of the next view to render
        self.target_key = 'None'
        # Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = ag.UIManager()
        self.manager.enable()
        #Get the size of the current viewport
        self.px, self.wd, self.py, self.ht = self.window.get_viewport()
        #To enable scaling, we reference the viewport size for use
        width = self.wd//4
        height = self.ht//16
        
        self.v_box = ag.UIBoxLayout()

        #The style to use for the buttons
        self.default_style = {
            "font_name": "times",
            "font_size": height//3,
            "font_color": arcade.color.WHITE,
            "border_width": height//16,
            "border_color": (255, 255, 255),
            "bg_color": (21, 19, 21),

            #used if button is pressed
            "bg_color_pressed": arcade.color.WHITE,
            "font_color_pressed": arcade.color.BLACK,
            #used when hovered
            "border_color_pressed": arcade.color.YELLOW,
        }
        #Buttons on the main menu would be
        #New Game, Continue, Options, Credits, Quit
        #New Game
        self.new_game_btn = ag.UIFlatButton(
            text='New Game',
            width=width,
            height=height,
            style=self.default_style,
        )
        self.v_box.add(
            self.new_game_btn.with_space_around(
                bottom=width//20
            )
        )
        #Add a new on_click event for the button        
        @self.new_game_btn.event("on_click")
        def on_click_new_game(event):
            print("New game!") #Debugging
            self.target_key = 'new_game'
            self.manager.disable()
            self.start_fade_out()
            
        #Continue
        self.continue_btn = ag.UIFlatButton(
            text='Continue',
            width=width,
            height=height,
            style=self.default_style,
        )
        self.v_box.add(
            self.continue_btn.with_space_around(
                bottom=width//20
            )
        )
        @self.continue_btn.event("on_click")
        def on_click_continue(event):
            print("Continue!") #Debugging
            self.target_key = 'continue'
            self.manager.disable()
            self.start_fade_out()
            
        #Options
        self.options_btn = ag.UIFlatButton(
            text='Options',
            width=width,
            height=height,
            style=self.default_style,
        )
        self.v_box.add(
            self.options_btn.with_space_around(
                bottom=width//20
            )
        )
        @self.options_btn.event("on_click")
        def on_click_options(event):
            print("Options.") #Debugging
            self.target_key = 'options'
            self.manager.disable()
            self.start_fade_out()
            
        #Credits
        self.credits_btn = ag.UIFlatButton(
            text='Credits',
            width=width,
            height=height,
            style=self.default_style,
        )
        self.v_box.add(
            self.credits_btn.with_space_around(
                bottom=width//20
            )
        )
        @self.credits_btn.event("on_click")
        def on_click_credits(event):
            print("Credits.") #Debugging
            #self.target_key = 'credits' #Use for proper credits
            self.target_key = 'splash'
            self.manager.disable()
            self.start_fade_out()
            
        #Quit
        self.quit_btn = ag.UIFlatButton(
            text='Quit',
            width=width,
            height=height,
            style=self.default_style,
        )
        self.v_box.add(
            self.quit_btn.with_space_around(
                bottom=width//20
            )
        )
        @self.quit_btn.event("on_click")
        def on_click_quit(event):
            print("Quitting game.") #Debugging
            self.window.close()
            arcade.exit()

        #Place the widget on-screen
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
        self.current_button = 0
        self.button_positions = []
        px, _ = self.v_box.center
        py = self.ht*.77
        for b in self.v_box.children:
            dx, dy = b.rect.center
            self.button_positions.append((px+dx, py+dy))
        
    def on_draw(self):
        self.clear()
        self.manager.draw()

        #These two should always be placed last to allow
        # drawing over all other parts of the view
        self.fade_in() #Only called on starting view
        self.fade_out(
            self.window.views.get(self.target_key, MainMenuView)
        ) #Only called before closing view

    def on_key_press(self, key, modifiers):
        '''
        Handle key presses.
        '''
        if key in (arcade.key.DOWN,arcade.key.RIGHT,arcade.key.S,arcade.key.D):
            self.current_button += 1
            self.current_button %= len(self.button_positions)
            px, py = self.button_positions[self.current_button]
            self.window.set_mouse_position(int(px), int(py))
            
        elif key in (arcade.key.UP,arcade.key.LEFT,arcade.key.W,arcade.key.A):
            self.current_button -= 1
            self.current_button %= len(self.button_positions)
            px, py = self.button_positions[self.current_button]
            self.window.set_mouse_position(int(px), int(py))

        elif key in (arcade.key.SPACE, arcade.key.ENTER):
            mouse.click('left') #Simulate a click
        
        
    def on_mouse_motion(self, x, y, dx, dy):
        #Look for the closest from the buttons
        #and set is at the target
        distances = [
            (px-x)**2+(py-y)**2 for px, py in self.button_positions
        ]
        self.current_button = distances.index(min(distances))
