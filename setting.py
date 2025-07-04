import pygame
import random

FIELD_WIDTH, FIELD_HEIGHT = 300, 300
fps = 30
tileSize = 15

player_pos = [10, 10]

food_pos = [random.randint(1, 19), random.randint(1, 19)]
tail = []

snake_rect = pygame.Rect(player_pos[0] * tileSize, player_pos[1] * tileSize, tileSize, tileSize)