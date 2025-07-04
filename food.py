from setting import *

class Food:
    def __init__(self):
        self.food_rect = pygame.Rect(food_pos[0] * tileSize, food_pos[1] * tileSize, tileSize, tileSize)

    def draw(self, screen):
        pygame.draw.rect(screen, 'red', self.food_rect)