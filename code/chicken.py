from settings import *
from sprites import *
from spritesheet import Spritesheet
from timer import Timer
from random import choice

class Chicken(CollisionSprite):
    def __init__(self, pos, groups, collision_sprites):
        self.load_images()
        self.state, self.frame_index = 'resting', 0
        surf = self.frames[self.state][self.frame_index]
        super().__init__(pos, surf, groups)
        
        # movement 
        self.states = ['resting', 'moving horizontal', 'moving vertical', 'moving diagonal']
        self.state_timer = Timer(700, func = self.switch_state, autostart = True, repeat = True)
        self.direction = pygame.Vector2()
        self.speed = 200
        self.collision_sprites = collision_sprites
        
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
            surf = self.spritesheet.get_sprite((1, frame))
            self.frames['moving right'].append(surf)
            self.frames['moving left'].append(pygame.transform.flip(surf, True, False))
            
    def switch_state(self):
        self.state = choice(self.states)
        if self.state == 'moving horizontal':
            self.direction.x = choice([-1,1])
        elif self.state == 'moving vertical':
            self.direction.y = choice([-1,1])
        elif self.state == 'moving diagonal':
            self.direction.x = choice([-1,1])
            self.direction.y = choice([-1,1])
            self.direction = self.direction.normalize()
        else:
            self.direction.x = 0
            self.direction.y = 0
            
    def move(self, dt):
        if self.state == 'moving horizontal':
            self.rect.x += self.direction.x * self.speed * dt
            self.collision('horizontal')
        if self.state == 'moving vertical':
            self.rect.y += self.direction.y * self.speed * dt
            self.collision('vertical')
        if self.state == 'moving diagonal':
            self.rect.x += self.direction.x * self.speed * dt
            self.rect.y += self.direction.y * self.speed * dt
            self.collision('diagonal')
        self.rect.center = self.rect.center

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                elif direction == 'vertical':
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top
                else:
                    collision_spot = pygame.Vector2()
                    collision_spot.x = self.rect.centerx - sprite.rect.centerx
                    collision_spot.y = self.rect.centery - sprite.rect.centery
                    print(collision_spot)
                    
    def animate(self, dt):
        # get animation state 
        if self.direction.x == 0 and self.direction.y == 0: 
            animation = 'resting'
        elif self.direction.x < 0:
            animation = 'moving left' 
        else:
            animation = 'moving right'  

        # animate
        self.frame_index = self.frame_index + dt
        self.image = self.frames[animation][int(self.frame_index) % len(self.frames[animation])]
            
    def update(self, dt):
        self.state_timer.update()
        self.move(dt)
        self.animate(dt)