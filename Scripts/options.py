'''
Options Class

Handles the changing of game's global options.
Only handles Audio volume and text speed for now.
'''

import pickle
import arcade
import arcade.gui as ag
from arcade.experimental.uislider import UISlider

from Scripts.transition import TransitionView


class OptionsView(TransitionView):
    def __init__(self, speed=1):
        super().__init__(speed)
        #Initialize fade_in on start
        self.start_fade_in()
        #Set the background color of the view
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def setup(self):
        '''
        Setup for the Options.
        '''
        self.px, self.wd, self.py, self.ht = self.window.get_viewport()

        # Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = ag.UIManager()
        self.manager.enable()
        #Initialize local options variable to hold slider values
        self.options = self.window.read_options()

        #Title text
        self.title = arcade.create_text_sprite(
            "OPTIONS",
            self.wd * 0.5,
            self.ht * 0.75,
            arcade.color.BLACK,
            font_size=42,
            width=self.wd,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )
        #Banner/instruction text at the bottom 
        self.banner = arcade.create_text_sprite(
            "Press ESC to return...",
            self.wd * 0.5,
            self.ht * 0.15,
            arcade.color.BLACK,
            font_size=14,
            width=self.wd,
            font_name="times",
            anchor_x="center",
            anchor_y="center",
            align="center",
        )

        #Master Volume
        #Set the slider
        mv_slider = UISlider(
            value=self.options['master_volume']*100,
            width=300,
            height=50
        )
        #Set the slider value label
        mv_value = ag.UILabel(text=f"{mv_slider.value:02.0f}")
        #Set the slider name label
        mv_label = ag.UILabel(
            text=f"Master Volume",
            font_name='times',
            font_size=16,
            text_color=arcade.color.BLACK,
            bold=True
        )
        #Add slider event called when slider value changes
        @mv_slider.event()
        def on_change(event: ag.events.UIOnChangeEvent):
            mv_value.text = f"{mv_slider.value:02.0f}"
            self.options['master_volume'] = mv_slider.value/100
            mv_value.fit_content()
        #Add the slider, value label, and name label to manager
        self.manager.add(
            ag.UIAnchorWidget(
                child=mv_slider,
                align_x=100,
                align_y=60
            )
        )
        self.manager.add(
            ag.UIAnchorWidget(
                child=mv_value,
                align_x=100,
                align_y=60
            )
        )
        self.manager.add(
            ag.UIAnchorWidget(
                child=mv_label,
                align_x=-200,
                align_y=60
            )
        )

        #SE Volume
        se_slider = UISlider(
            value=self.options['se_volume']*100,
            width=300,
            height=50
        )
        se_value = ag.UILabel(text=f"{se_slider.value:02.0f}")
        se_label = ag.UILabel(
            text=f"Sound Effects Volume",
            font_name='times',
            font_size=16,
            text_color=arcade.color.BLACK,
            bold=True
        )
        @se_slider.event()
        def on_change(event: ag.events.UIOnChangeEvent):
            se_value.text = f"{se_slider.value:02.0f}"
            self.options['se_volume'] = se_slider.value/100
            se_value.fit_content()
            
        self.manager.add(
            ag.UIAnchorWidget(
                child=se_slider,
                align_x=100,
                align_y=20
            )
        )
        self.manager.add(
            ag.UIAnchorWidget(
                child=se_value,
                align_x=100,
                align_y=20
            )
        )
        self.manager.add(
            ag.UIAnchorWidget(
                child=se_label,
                align_x=-200,
                align_y=20
            )
        )

        #BGM Volume
        bg_slider = UISlider(
            value=self.options['bgm_volume']*100,
            width=300,
            height=50
        )
        bg_value = ag.UILabel(text=f"{bg_slider.value:02.0f}")
        bg_label = ag.UILabel(
            text=f"BGM Volume",
            font_name='times',
            font_size=16,
            text_color=arcade.color.BLACK,
            bold=True
        )
        @bg_slider.event()
        def on_change(event: ag.events.UIOnChangeEvent):
            bg_value.text = f"{bg_slider.value:02.0f}"
            self.options['bgm_volume'] = bg_slider.value / 100
            bg_value.fit_content()
            
        self.manager.add(
            ag.UIAnchorWidget(
                child=bg_slider,
                align_x=100,
                align_y=-20
            )
        )
        self.manager.add(
            ag.UIAnchorWidget(
                child=bg_value,
                align_x=100,
                align_y=-20
            )
        )
        self.manager.add(
            ag.UIAnchorWidget(
                child=bg_label,
                align_x=-200,
                align_y=-20
            )
        )

        #Text speed
        ts_slider = UISlider(
            value=self.options['text_speed']*100,
            width=300,
            height=50
        )
        ts_value = ag.UILabel(text=f"{ts_slider.value:02.0f}")
        ts_label = ag.UILabel(
            text=f"Text Speed",
            font_name='times',
            font_size=16,
            text_color=arcade.color.BLACK,
            bold=True
        )
        @ts_slider.event()
        def on_change(event: ag.events.UIOnChangeEvent):
            ts_value.text = f"{ts_slider.value:02.0f}"
            self.options['text_speed'] = ts_slider.value / 100
            ts_value.fit_content()
            
        self.manager.add(
            ag.UIAnchorWidget(
                child=ts_slider,
                align_x=100,
                align_y=-60
            )
        )
        self.manager.add(
            ag.UIAnchorWidget(
                child=ts_value,
                align_x=100,
                align_y=-60
            )
        )
        self.manager.add(
            ag.UIAnchorWidget(
                child=ts_label,
                align_x=-200,
                align_y=-60
            )
        )
        
    def on_draw(self):
        #Clear screen
        self.clear()
        #Draw entities
        self.title.draw()
        self.manager.draw()
        self.banner.draw()
        #These two should always be placed last to allow
        # drawing over all other parts of the view
        self.fade_in() #Only called on starting view
        self.fade_out(self.window.views['menu']) #Only called before closing view

    def on_update(self, dt: float):
        if self.window.is_pressed.get(arcade.key.ESCAPE, 0):
            self.window.save_options(self.options)
            #Avoid loop
            self.window.is_pressed[arcade.key.ESCAPE] = False
            self.start_fade_out()
        self.fade_update(dt)

    def on_key_press(self, key, modifier):
        pass
