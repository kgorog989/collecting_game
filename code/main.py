from settings import *
from player import Player
from sprites import *
from chicken import Chicken
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Game')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.collectable_sprites = pygame.sprite.Group()
        
        # score
        self.font = pygame.font.SysFont('Arial', 40, bold=True)
        self.score = SCORE_DATA
        self.text_surface = self.font.render(str(self.score), True, (0, 0, 0))

        self.setup()
        
    def setup(self):
        map = load_pygame(join('world', 'tmx', 'world_map.tmx'))

        for x, y, image in map.get_layer_by_name('Water').tiles():
            Sprite((x * TILE_SIZE*SCALING_FACTOR,
                    y * TILE_SIZE*SCALING_FACTOR), 
                    pygame.transform.scale(image, (TILE_SIZE*SCALING_FACTOR,TILE_SIZE*SCALING_FACTOR)), 
                    self.all_sprites)
            
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE_SIZE*SCALING_FACTOR,
                    y * TILE_SIZE*SCALING_FACTOR), 
                    pygame.transform.scale(image, (TILE_SIZE*SCALING_FACTOR,TILE_SIZE*SCALING_FACTOR)), 
                    self.all_sprites)
            
        for x, y, image in map.get_layer_by_name('Dirt').tiles():
            Sprite((x * TILE_SIZE*SCALING_FACTOR,
                    y * TILE_SIZE*SCALING_FACTOR), 
                    pygame.transform.scale(image, (TILE_SIZE*SCALING_FACTOR,TILE_SIZE*SCALING_FACTOR)), 
                    self.all_sprites)
            
        for x, y, image in map.get_layer_by_name('Fences').tiles():
            Sprite((x * TILE_SIZE*SCALING_FACTOR,
                    y * TILE_SIZE*SCALING_FACTOR), 
                    pygame.transform.scale(image, (TILE_SIZE*SCALING_FACTOR,TILE_SIZE*SCALING_FACTOR)), 
                    (self.all_sprites, self.collision_sprites))
        
        for obj in map.get_layer_by_name('Objects'):
            image = pygame.transform.scale(obj.image, (obj.width*SCALING_FACTOR,obj.height*SCALING_FACTOR))
            CollisionSprite((obj.x*SCALING_FACTOR, 
                             obj.y*SCALING_FACTOR), 
                             image,
                             (self.all_sprites, self.collision_sprites))
        
        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x*SCALING_FACTOR, obj.y*SCALING_FACTOR), 
                            pygame.Surface((obj.width*SCALING_FACTOR, obj.height*SCALING_FACTOR)), 
                            self.collision_sprites)

        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x*SCALING_FACTOR,obj.y*SCALING_FACTOR), 
                                     self.score, 
                                     self.all_sprites, 
                                     self.collision_sprites, 
                                     self.collectable_sprites)
            if obj.name == 'Chicken':
                Chicken((obj.x*SCALING_FACTOR,obj.y*SCALING_FACTOR), 
                        self.all_sprites, 
                        self.collision_sprites, 
                        self.collectable_sprites)

    def run(self):
        while self.running:
            # dt 
            dt = self.clock.tick() / 1000

            # event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update 
            self.all_sprites.update(dt)

            # draw
            self.display_surface.fill(WATER_COLOR)
            self.all_sprites.draw(self.player.rect.center)
            self.text_surface = self.font.render(str(self.score['score']), True, (60, 60, 60))
            self.display_surface.blit(self.text_surface, (10, 10))
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()