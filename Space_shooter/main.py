import arcade
from game_play import GamePlay

window=arcade.Window(1200,800,"Game1")
game_play=GamePlay(1200,800)

window.show_view(game_play)
arcade.run()