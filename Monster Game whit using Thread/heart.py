import arcade

class Heart(arcade.Sprite):
     def __init__(self,x):
        super().__init__("icons8-bubble-48.png")
        self.center_x=25*x
        self.center_y=25
        self.width=25
        self.height=25
        