import threading
import time
import arcade

from monster import Monster
from enemy import Enemy
from heart import Heart
from bubble import Bubble


class Game(arcade.Window):
    def __init__(self):
      super().__init__(width=600 , height=450 , title="War under the Sea🌊")
      arcade.set_background_color(arcade.color.BLUE_YONDER)
      self.background = arcade.load_texture("sea-background-video-conferencing_23-2148626865.webp")
      self.me=Monster(self)
      self.enemy=Enemy(self.width , self.height)
      self.enemys=[]
      self.hearts=[]
      self.laser_sound = arcade.load_sound("Food_drink_big_bubble_blown_into_glass_through_drinking_straw_1.mp3")
      self.time_speed=0.4
      self.time=time.time()
      self.my_thread=threading.Thread(target=self.create_enemy)
      self.my_thread.start()


      for i in range(3):
        self.heart=Heart(i+1)
        self.hearts.append(self.heart)
      self.game_status=" "
      
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,600,450, self.background)
        self.me.draw()
        
        for bubble in self.me.bubbles:
            bubble.draw()
            
        for enemy in self.enemys:
             enemy.draw()
        for heart in self.hearts:
            heart.draw()
        arcade.draw_text("score: ",510,15,arcade.color.RED , 17,30)
        arcade.draw_text(self.me.score , 575,15 ,arcade.color.RED , 17 , 30)

        if self.game_status=="gameover":
            self.clear()
            arcade.draw_rectangle_filled(self.width//2 , self.height//2,self.width,self.height , arcade.color.BLACK)
            arcade.draw_text("GAME OVER",100,230,arcade.color.RED , 45,45)
            
           



    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.UP:
            self.me.change_y = 1
        if symbol==arcade.key.DOWN:
           self.me.change_y = -1
        if symbol==arcade.key.SPACE:
            self.me.fire()
            arcade.play_sound(self.laser_sound)

    def create_enemy(self):
        
        while 1==1:
                self.enemy=Enemy(self.width , self.height)
                self.enemys.append(self.enemy)
                for enemy in self.enemys:
                        self.enemy.speed -= self.time_speed
                self.enemy.speed+=0.4
                time.sleep(5)
                self.time = time.time()
   
    def update(self, delta_time: float):
        for enemy in self.enemys:
            enemy.move()

        for enemy in self.enemys:
            if enemy.center_x < 0:
                self.enemys.remove(enemy)
                if len (self.hearts)>0:
                 self.hearts.pop(-1)

    
        for bubble in self.me.bubbles:
            bubble.move()
            if bubble.center_x > self.width:
                self.me.bubbles.remove(bubble)

        for enemy in self.enemys:
            if arcade.check_for_collision(self.me,enemy):
                self.game_status="gameover"

        if self.enemy.center_x +30 < 0:
            if len (self.hearts)>0:
                self.hearts.remove(self.heart)
               
        if len(self.hearts)==0:
            self.game_status="gameover"
        for bubble in self.me.bubbles:
            for enemy in self.enemys:
                if arcade.check_for_collision(bubble ,enemy):
                    arcade.play_sound(self.enemy.bomb_sound)
                    self.me.bubbles.remove(bubble)
                    self.enemys.remove(enemy)
                    self.me.score+=1
        
        
                
        self.me.move(self)

        



window=Game()

arcade.run()