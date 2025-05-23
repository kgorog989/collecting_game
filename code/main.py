from settings import *
from player import Player
from sprites import *
from chicken import Chicken
from cow import Cow
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Egg Hunt!')
        self.clock = pygame.time.Clock()
        self.game_data = GAME_DATA
        try:
            score_file = open(join('data', 'highscore.txt'), 'r')
            self.game_data['highscore'] = int(score_file.read())
            score_file.close()
        except:
            pass

        # groups 
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.collectable_sprites = pygame.sprite.Group()
        self.cow_sprites = pygame.sprite.Group()
        
        # score and health
        self.font = pygame.font.Font(join('fonts', 'Masaaki-Regular.otf'), FONT_SIZE)
        self.score_egg = pygame.transform.scale(pygame.image.load(join('world', 'graphics', 'Objects', 'Egg_item.png')).convert_alpha(), 
                                                (TILE_SIZE*SCALING_FACTOR, TILE_SIZE*SCALING_FACTOR))
        self.score_egg_rect = self.score_egg.get_frect(topleft = (5, 5))
        self.heart = pygame.transform.scale(pygame.image.load(join('images', 'heart.png')).convert_alpha(), 
                                                (HEART_SIZE, HEART_SIZE))
        self.heart_rect = self.heart.get_frect(topleft = (WINDOW_WIDTH / 1.17, 10))
        
        # invincible, highscore text
        self.text_surface_invincible = self.font.render('Invincible', True, FONT_COLOR)
        self.text_surface_highscore = self.font.render('Highscore: ' + str(self.game_data['highscore']), True, FONT_COLOR)
        
        # audio
        self.game_audio = pygame.mixer.Sound(join('audio', 'relaxing_chiptune_music.mp3'))
        self.game_audio.set_volume(0.4)
        self.game_audio.play(-1)

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
                                     self.game_data, 
                                     self.all_sprites, 
                                     self.collision_sprites, 
                                     self.collectable_sprites, 
                                     self.cow_sprites)
            if obj.name == 'Chicken':
                Chicken((obj.x*SCALING_FACTOR,obj.y*SCALING_FACTOR), 
                        self.all_sprites, 
                        self.collision_sprites, 
                        self.collectable_sprites)
            if obj.name == 'Cow':
                Cow((obj.x*SCALING_FACTOR,obj.y*SCALING_FACTOR), 
                        (self.all_sprites, self.cow_sprites), 
                        self.collision_sprites, 
                        self.collectable_sprites)

    def update_displayed_data(self):
        # score
        self.display_surface.blit(self.score_egg, self.score_egg_rect)
        self.text_surface_score = self.font.render(str(self.game_data['score']), True, FONT_COLOR)
        self.display_surface.blit(self.text_surface_score, (self.score_egg_rect.width + 10, -5))
        
        # health
        self.display_surface.blit(self.heart, self.heart_rect)
        self.text_surface_health = self.font.render(str(self.game_data['health']), True, FONT_COLOR)
        self.display_surface.blit(self.text_surface_health, (WINDOW_WIDTH / 1.07, -5))
        
        # invincibility
        if self.player.invincible:
            self.display_surface.blit(self.text_surface_invincible, (5, WINDOW_HEIGHT - 80))
            
        # highscore
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.display_surface.blit(self.text_surface_highscore, 
                                      (WINDOW_WIDTH - self.text_surface_highscore.width - 5, WINDOW_HEIGHT - 80))

    def run(self):
        while self.game_data['running']:
            # dt 
            dt = self.clock.tick() / 1000

            # event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_data['running'] = False
                    if self.game_data['score'] > self.game_data['highscore']:
                        try:
                            mkdir('data')
                        except:
                            pass
                        score_file = open(join('data', 'highscore.txt'), 'w')
                        score_file.write(str(self.game_data['score']))
                        score_file.close()

            # update 
            self.all_sprites.update(dt)

            # draw
            self.display_surface.fill(WATER_COLOR)
            self.all_sprites.draw(self.player.rect.center)
            self.update_displayed_data()
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()