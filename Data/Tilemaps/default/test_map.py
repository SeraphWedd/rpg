import arcade

class MainWindow(arcade.Window):
    def __init__(self):
        super().__init__()
        self.tm = arcade.load_tilemap('default.json')
        arcade.set_background_color(arcade.color.BLACK)
        self.camera = arcade.Camera()
        self.pos_x, self.pos_y = 0, 0
        self.pan_to_pos()
        self.set_mouse_visible(False)
        self.set_exclusive_mouse(True)

    def pan_to_pos(self):
        self.camera.move_to((self.pos_x, self.pos_y))

    def on_draw(self):
        self.camera.use()
        self.clear()
        for k in self.tm.sprite_lists.keys():
            self.tm.sprite_lists[k].draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.pos_x += dx*5
        self.pos_y += dy*5
        self.pan_to_pos()

if __name__ == "__main__":
    win = MainWindow()
    win.run()
