from setting import *

class Grid:
    def __init__(self):
        pass

    def grid_box(self, screen):
        for x in range(FIELD_WIDTH):
            for y in range(FIELD_HEIGHT):
                pygame.draw.rect(screen, 'orange', (x * tileSize, y * tileSize, tileSize, tileSize), 1)