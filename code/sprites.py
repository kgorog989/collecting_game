from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        
class Player(Sprite):
    def __init__(self, pos, groups, collision_sprites):
        surf = pygame.Surface((20,40))
        surf.fill("red")
        super().__init__(pos, surf, groups)
        
        # movement section
        self.direction = pygame.Vector2()
        self.collision_sprites = collision_sprites
        self.speed = 400
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.collision("horizontal")
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.collision("vertical")
        self.direction = self.direction.normalize() if self.direction else self.direction
        
    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt
    
    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.direction.x > 0: self.rect.right = self.rect.left
                    if self.direction.x < 0: self.rect.left = self.rect.right
                if direction == "vertical":
                    if self.direction.y > 0: self.rect.bottom = self.rect.top
                    if self.direction.y < 0: self.rect.top = self.rect.bottom
    
    def update(self, dt):
        self.input()
        self.move(dt)