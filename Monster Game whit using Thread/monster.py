import arcade
from bubble import Bubble

class Monster(arcade.Sprite):
    def __init__(self , game):
        super().__init__("mmm.png")
        self.center_x=60
        self.center_y=game.height//2
        self.width=100
        self.height=100
        self.speed=3
        self.score=0
        self.game_height=game.height
        self.bubbles=[]


    def move(self,game):
        self.center_y += self.change_y * self.speed

        if self.center_y  == game.height:
            self.change_y = -1
        if self.center_y ==0:
            self.change_y = 1


    def fire(self): 
        new_bubble=Bubble(self)
        self.bubbles.append(new_bubble)