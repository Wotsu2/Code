from setting import *

class Front:
    def __init__(self):
        pygame.font.init()
    def draw(self, screen):
        pygame.draw.rect(screen, 'black', (0, 0, FIELD_WIDTH, FIELD_HEIGHT))

    def front(self,screen):
        font = pygame.font.SysFont("arial", 15, bold = pygame.font.Font.bold)
        whole_text = "Snake Game Press Space To Start"
        text = font.render(whole_text, True, 'white')
        screen.blit(text, (35, FIELD_HEIGHT / 2 - 15))
    def game_over(self,screen):
        font = pygame.font.SysFont("arial", 15, bold = pygame.font.Font.bold)
        whole_text = "Game Over Press Enter to Start Again"
        text = font.render(whole_text, True, 'white')
        screen.blit(text, (25, FIELD_HEIGHT / 2 - 15))