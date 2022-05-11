

import arcade
import random

PLAYER_TEXTURE=":resources:images/space_shooter/playerShip1_green.png"
PLAYER_SCALE=0.7
PLAYER_SPEED=300
SPACE_PROJECTILE=":resources:images/space_shooter/laserRed01.png"
PROJECTILE_SPEED=300
PROJECTILE_SCALE=0.5
BACKGROUND=":resources:images/backgrounds/abstract_1.jpg"
ROCK=":resources:images/space_shooter/meteorGrey_big4.png"
ROCK_TIME_RES=3

class GamePlay(arcade.View):
    def __init__(self,width,height):
        super().__init__()
        self.width=width
        self.height=height
        self.setup()
        self.left_arrow=False
        self.right_arrow=False
        self.background=arcade.load_texture(BACKGROUND)
        self.time_since_rock=0

        

    def setup(self):
        self.player=arcade.Sprite(PLAYER_TEXTURE,PLAYER_SCALE)
        self.player.center_x=self.width/2
        self.player.center_y=self.height/5
        self.projectiles=arcade.SpriteList()
        self.back=arcade.Sprite(BACKGROUND)
        self.rocks=arcade.SpriteList()      


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,1200,800,self.background)
        self.player.draw()
        self.projectiles.draw()
        self.rocks.draw()
        
        

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.left_arrow=True
        if symbol == arcade.key.RIGHT:
            self.right_arrow=True
        if symbol == arcade.key.SPACE:
            projectile=arcade.Sprite(SPACE_PROJECTILE,PROJECTILE_SCALE)
            projectile.center_x=self.player.center_x
            projectile.center_y=self.player.center_y
            self.projectiles.append(projectile)
    
    def spawn_rock(self):
        x=random.randint(0,self.width)
        speed_rock=random.randint(50,150)
        rock_sprite=arcade.Sprite(ROCK)
        rock_sprite.speed=-speed_rock
        rock_sprite.center_x=x
        rock_sprite.center_y=self.height
        self.rocks.append(rock_sprite)
                

    def on_key_release(self, symbol: int, _modifiers: int):
        if symbol == arcade.key.LEFT:
            self.left_arrow=False
        if symbol == arcade.key.RIGHT:
            self.right_arrow=False
    
    def on_update(self, delta_time):
        player_speed=0
        if self.left_arrow:
            player_speed-=PLAYER_SPEED
        if self.right_arrow:
            player_speed+=PLAYER_SPEED
        self.player.center_x+=player_speed*delta_time
        for p in self.projectiles:
            p.center_y+=PROJECTILE_SPEED*delta_time
        for r in self.rocks:
            r.center_y+=r.speed*delta_time
        self.time_since_rock+=delta_time
        if self.time_since_rock>=ROCK_TIME_RES:
            self.time_since_rock=0
            self.spawn_rock()
        self.coliding_rocks=arcade.check_for_collision_with_list(self.player,self.rocks)
        if len(self.coliding_rocks)>0:
            exit(0)
        
        
        
        