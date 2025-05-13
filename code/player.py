from settings import * 
from spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, game_data, groups, collision_sprites, collectable_sprites, cow_sprites):
        super().__init__(groups)
        self.load_images()
        self.state, self.frame_index = 'right', 0
        self.image = self.spritesheet.get_sprite((self.frame_index, self.frame_index))
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-140, -155)
        self.starting_point = pos
    
        # movement 
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites
        self.cow_sprites = cow_sprites
        self.cow_sound = pygame.mixer.Sound(join('audio', 'moo.aiff'))
        self.cow_sound.set_volume(0.5)
        
        # collecting
        self.game_data = game_data
        self.collectable_sprites = collectable_sprites
        self.collect_sound = pygame.mixer.Sound(join('audio', 'collect_egg.mp3'))
        self.collect_sound.set_volume(0.5)
        
    def egg_collecting(self):
        for sprite in self.collectable_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                self.collect_sound.play()
                sprite.kill()
                self.game_data['score'] += 1

    def cow_collide(self):
        for sprite in self.cow_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                self.cow_sound.play()
                self.game_data['health'] -= 1
                self.hitbox_rect.center = self.starting_point
                if self.game_data['health'] == 0:
                    self.game_data['running'] = False

    def load_images(self):
        self.spritesheet = Spritesheet(join('world', 'graphics', 'Characters', 'Basic Charakter Spritesheet.png'), 
                                  (PLAYER_SIZE,PLAYER_SIZE), 
                                  scale=(PLAYER_SIZE*SCALING_FACTOR, PLAYER_SIZE*SCALING_FACTOR))
        index_pairs = {0: 'down', 1 : 'up', 2: 'left', 3: 'right'}
        self.frames = {'left': [], 'right': [], 'up': [], 'down': []}
        directions = 4
        direction_frame_num = 4
        
        for direction in range(directions):
            state = index_pairs[direction]
            for frame in range(direction_frame_num):
                surf = self.spritesheet.get_sprite((direction, frame))
                self.frames[state].append(surf)

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top

    def animate(self, dt):
        # get state 
        if self.direction.x != 0:
            self.state = 'right' if self.direction.x > 0 else 'left'
        if self.direction.y != 0:
            self.state = 'down' if self.direction.y > 0 else 'up'

        # animate
        self.frame_index = self.frame_index + 5 * dt if self.direction else 0
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

    def update(self, dt):
        self.egg_collecting()
        self.cow_collide()
        self.input()
        self.move(dt)
        self.animate(dt)