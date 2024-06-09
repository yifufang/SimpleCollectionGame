import pygame
import random

#--------------------------Constants----------------------------------
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player settings
PLAYER_SIZE = 50
PLAYER_COLOR = (0, 0, 255)
PLAYER_SPEED = 5

# Item settings
ITEM_SIZE = 20
ITEM_COLOR = (255, 0, 0)
ITEM_SPEED = 3

# Colors
BACKGROUND_COLOR = (255, 255, 255)

# Font settings
FONT_SIZE = 35

# Game settings
WIN_TEXT = 'You Win!'
WIN_TEXT_COLOR = (0, 255, 0)
WIN_TEXT_DELAY = 3000  # milliseconds

#----------------------Game Initialization--------------------------------------
# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Collecting Game')

# Player class
class Player(pygame.sprite.Sprite):
    #run only once when the object is created
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
    
    # update on every frame
    def update(self):
        #TO DO: Update player position
        keys = pygame.key.get_pressed()
        pass

# Item class
class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ITEM_SIZE, ITEM_SIZE))
        self.image.fill(ITEM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - ITEM_SIZE)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - ITEM_SIZE)
        
        #TO DO: assign random speed to item
        self.speed_x
        self.speed_y
    def update(self):
        #TO DO: Update item position
        
        pass

        # Keep item on screen
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

# Initialize player and items
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

items = pygame.sprite.Group()
for _ in range(20):
    item = Item()
    all_sprites.add(item)
    items.add(item)

# Main game loop
running = True
score = 0
clock = pygame.time.Clock()

#---------------------Game Running-------------------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    collected_items = pygame.sprite.spritecollide(player, items, True)
    score += len(collected_items)

    if len(items) == 0:
        font = pygame.font.SysFont(None, FONT_SIZE)
        win_text = font.render(WIN_TEXT, True, WIN_TEXT_COLOR)
        screen.blit(win_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(WIN_TEXT_DELAY)
        running = False

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)

    font = pygame.font.SysFont(None, FONT_SIZE)
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
