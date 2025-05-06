from settings import *
from sprites import *
from spritesheet import Spritesheet

class Egg(CollisionSprite):
    def __init__(self, pos, groups):
        self.spritesheet = Spritesheet(join('world', 'graphics', 'Characters', 'Egg_And_Nest.png'), 
                                  (TILE_SIZE,TILE_SIZE), 
                                  scale=(TILE_SIZE*SCALING_FACTOR, TILE_SIZE*SCALING_FACTOR))
        surf = self.spritesheet.get_sprite((0, 0))
        super().__init__(pos, surf, groups)