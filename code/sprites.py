from settings import * 
from spritesheet import Spritesheet
from timer import Timer
from random import choice

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        
class Chicken(CollisionSprite):
    def __init__(self, pos, groups):
        self.load_images()
        self.state, self.frame_index = 'resting', 0
        surf = self.frames[self.state][self.frame_index]
        super().__init__(pos, surf, groups)
        self.state_timer = Timer(500, func = lambda:print(choice(["rest", "move"])), autostart = True, repeat = True)
        
        # movement 
        self.direction = pygame.Vector2()
        self.speed = 500
        #self.collision_sprites = collision_sprites
        
    def load_images(self):
        self.spritesheet = Spritesheet(join('world', 'graphics', 'Characters', 'Free Chicken Sprites.png'), 
                                  (TILE_SIZE,TILE_SIZE), 
                                  scale=(TILE_SIZE*SCALING_FACTOR, TILE_SIZE*SCALING_FACTOR))
        self.frames = {'resting': [], 'moving right': [], 'moving left': []}
        moving_frame_num = 4
        resting_frame_num = 2
                
        #resting frames
        for frame in range(resting_frame_num):
            surf = self.spritesheet.get_sprite((0, frame))
            self.frames['resting'].append(surf)
            
        #moving frames
        for frame in range(moving_frame_num):
            surf = self.spritesheet.get_sprite((0, frame))
            self.frames['moving right'].append(surf)
            self.frames['moving left'].append(pygame.transform.flip(surf, True, False))
            
    def update(self, dt):
        self.state_timer.update()