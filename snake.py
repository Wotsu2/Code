from setting import *

class Snake:
    def __init__(self):
        self.tail = tail
        self.tail.append(snake_rect)
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.snake_rect = snake_rect
    def draw(self, screen):
        self.snake_rect = pygame.Rect(player_pos[0] * tileSize, player_pos[1] * tileSize, tileSize, tileSize)
        for part in self.tail:
            pygame.draw.rect(screen, 'blue', part)

    def grow_tail(self):
        if self.tail:
            current_tail = self.tail[0]
            new_tail = current_tail.copy()
            self.tail.insert(0, new_tail)

    def control(self):
        new_tail_rect = self.snake_rect.copy()
        self.tail.append(new_tail_rect)
        self.tail.pop(0)
        
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.up = True
            self.down = False
            self.left = False
            self.right = False
        elif key[pygame.K_DOWN]:
            self.down = True
            self.up = False
            self.left = False
            self.right = False     
        elif key[pygame.K_LEFT]:
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        elif key[pygame.K_RIGHT]:
            self.right = True
            self.left = False
            self.up = False
            self.down = False
        
        if self.up:
            player_pos[1] -= 1
        elif self.down:
            player_pos[1] += 1
        elif self.left:
            player_pos[0] -= 1
        elif self.right:
            player_pos[0] += 1

        if player_pos[1] < 0:
            player_pos[1] = 20
        elif player_pos[1] > 20:
            player_pos[1] = 0
        if player_pos[0] < 0:
            player_pos[0] = 20
        elif player_pos[0] > 20:
            player_pos[0] = 0

    def update(self):
        self.control()
        self.tail.append(self.snake_rect.copy())