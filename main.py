import sys
from setting import *
from grid import Grid
from snake import Snake
from food import Food
from front import Front

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((FIELD_WIDTH, FIELD_HEIGHT))
        self.clock = pygame.time.Clock()
        self.grid = Grid()
        self.snake = Snake()
        self.food = Food()
        self.front = Front()
        self.start = False
        self.game_over = False

    def restart(self):
        self.snake.snake_rect = snake_rect
        self.food.food_rect[0] = random.randint(1, 19) * tileSize
        self.food.food_rect[1] = random.randint(1, 19) * tileSize

    def draw(self):
        self.screen.fill("black")
        if self.start:
            self.grid.grid_box(self.screen)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
        else:
            self.front.front(self.screen)
            self.restart()

        pygame.display.flip()

    def collision_event(self):
        if self.snake.snake_rect.colliderect(self.food.food_rect):
            self.food.food_rect[0] = random.randint(1, 19) * tileSize
            self.food.food_rect[1] = random.randint(1, 19) * tileSize
            self.snake.grow_tail()

        head = tail[0]
        for part in tail[2:]:
            if head.colliderect(part):
                self.start = False

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    self.start = True

    def update(self):
        if self.start:
            self.snake.control()
            self.collision_event()
        self.clock.tick(fps)

    def run(self):
        while True:
            self.draw()
            self.check_event()
            self.update()

if __name__ == "__main__":
    app = App()
    app.run()