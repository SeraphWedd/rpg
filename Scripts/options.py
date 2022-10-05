import pickle
import arcade
import arcade.gui as ag
from arcade.experimental.uislider import UISlider
from Scripts.transition import TransitionView

class OptionsView(TransitionView):
    def __init__(self, speed=1):
        super().__init__(speed)
        self.start_fade_in()
        
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.px, self.wd, self.py, self.ht = self.window.get_viewport()

        self.manager = ag.UIManager()
        self.manager.enable()
        self.options = self.window.read_options()

        #Master Volume
        mv_slider = UISlider(value=self.options['master_volume']*100,
                             width=300, height=50)
        mv_value = ag.UILabel(text=f"{mv_slider.value:02.0f}")
        mv_label = ag.UILabel(text=f"Master Volume",
                              font_name='times',
                              font_size=16,
                              text_color=arcade.color.BLACK,
                              bold=True)

        @mv_slider.event()
        def on_change(event: ag.events.UIOnChangeEvent):
            mv_value.text = f"{mv_slider.value:02.0f}"
            self.options['master_volume'] = mv_slider.value / 100
            mv_value.fit_content()
            
        self.manager.add(ag.UIAnchorWidget(
            child=mv_slider, align_x=100, align_y=60
            ))
        self.manager.add(ag.UIAnchorWidget(
            child=mv_value, align_x=100, align_y=60
            ))
        self.manager.add(ag.UIAnchorWidget(
            child=mv_label, align_x=-200, align_y=60
            ))

        #SE Volume
        se_slider = UISlider(value=self.options['se_volume']*100,
                             width=300, height=50)
        se_value = ag.UILabel(text=f"{se_slider.value:02.0f}")
        se_label = ag.UILabel(text=f"Sound Effects Volume",
                              font_name='times',
                              font_size=16,
                              text_color=arcade.color.BLACK,
                              bold=True)

        @se_slider.event()
        def on_change(event: ag.events.UIOnChangeEvent):
            se_value.text = f"{se_slider.value:02.0f}"
            self.options['se_volume'] = se_slider.value / 100
            se_value.fit_content()
            
        self.manager.add(ag.UIAnchorWidget(
            child=se_slider, align_x=100, align_y=20
            ))
        self.manager.add(ag.UIAnchorWidget(
            child=se_value, align_x=100, align_y=20
            ))
        self.manager.add(ag.UIAnchorWidget(
            child=se_label, align_x=-200, align_y=20
            ))

        #BGM Volume
        bg_slider = UISlider(value=self.options['bgm_volume']*100,
                             width=300, height=50)
        bg_value = ag.UILabel(text=f"{bg_slider.value:02.0f}")
        bg_label = ag.UILabel(text=f"BGM Volume",
                              font_name='times',
                              font_size=16,
                              text_color=arcade.color.BLACK,
                              bold=True)

        @bg_slider.event()
        def on_change(event: ag.events.UIOnChangeEvent):
            bg_value.text = f"{bg_slider.value:02.0f}"
            self.options['bgm_volume'] = bg_slider.value / 100
            bg_value.fit_content()
            
        self.manager.add(ag.UIAnchorWidget(
            child=bg_slider, align_x=100, align_y=-20
            ))
        self.manager.add(ag.UIAnchorWidget(
            child=bg_value, align_x=100, align_y=-20
            ))
        self.manager.add(ag.UIAnchorWidget(
            child=bg_label, align_x=-200, align_y=-20
            ))

        #Text speed
        ts_slider = UISlider(value=self.options['text_speed']*100,
                             width=300, height=50)
        ts_value = ag.UILabel(text=f"{ts_slider.value:02.0f}")
        ts_label = ag.UILabel(text=f"Text Speed",
                              font_name='times',
                              font_size=16,
                              text_color=arcade.color.BLACK,
                              bold=True)

        @ts_slider.event()
        def on_change(event: ag.events.UIOnChangeEvent):
            ts_value.text = f"{ts_slider.value:02.0f}"
            self.options['text_speed'] = ts_slider.value / 100
            ts_value.fit_content()
            
        self.manager.add(ag.UIAnchorWidget(
            child=ts_slider, align_x=100, align_y=-60
            ))
        self.manager.add(ag.UIAnchorWidget(
            child=ts_value, align_x=100, align_y=-60
            ))
        self.manager.add(ag.UIAnchorWidget(
            child=ts_label, align_x=-200, align_y=-60
            ))
        

    def on_draw(self):
        self.clear()
        self.manager.draw()
        #These two should always be placed last to allow
        # drawing over all other parts of the view
        self.fade_in() #Only called on starting view
        self.fade_out(self.window.views['menu']) #Only called before closing view

    def setup(self):
        pass

    def on_update(self, dt: float):
        if self.window.is_pressed.get(arcade.key.ESCAPE, 0):
            self.window.save_options(self.options)
            #Avoid loop
            self.window.is_pressed[arcade.key.ESCAPE] = False
            self.start_fade_out()
        self.fade_update(dt)

    def on_key_press(self, key, modifier):
        pass
