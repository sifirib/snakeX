# yilanin parcalarini bir arreye ekleyip o arrayi ekrana yazdirman lazim

import pygame
from pygame import mixer
import math
import random
import time

# Intialize the pygame
pygame.init()
clock = pygame.time.Clock()
# Create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and icon
pygame.display.set_caption("SnakeX")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

class Snake:

    def __init__(self, x, y, x_change, y_change, speed ):
        self.image = pygame.image.load('head.png')
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.speed = speed



class Apple:

    def __init__(self, x, y):
        self.image = pygame.image.load('apple.png')
        self.x = x
        self.y = y


snake = Snake(400, 300, 0, 0, 0.3)
apple = Apple(500, 500)


# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))



def draw_snake(x, y):
    screen.blit(snake.image, (x, y))

def draw_apple(x, y):
    screen.blit(apple.image, (x, y))


def isCollission(apple_x, apple_y, snake_x, snake_y):
    distance = math.sqrt((math.pow(apple_x - snake_x, 2)) + (math.pow(apple_y - snake_y, 2)))
    if distance > 25.7 and distance < 25.9:
        return True
    else:
        return False
x
x_for_velocity = snake.x
y_for_velocity = snake.y
tails = []
step = 0
# Game loop
running = True
while running:
    # RGB
    screen.fill((0, 100, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        key = ''
        # MOVING for Player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.x_change = -snake.speed
                snake.y_change = 0
            if event.key == pygame.K_RIGHT:
                snake.x_change = snake.speed
                snake.y_change = 0
            if event.key == pygame.K_DOWN:
                snake.y_change = snake.speed
                snake.x_change = 0
            if event.key == pygame.K_UP:
                snake.y_change = -snake.speed
                snake.x_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pass

    snake.x += snake.x_change
    snake.y += snake.y_change

    # TELEPORT
    if snake.x >= 800:
        snake.x = 2
    if snake.x <= 0:
        snake.x = 798
    if snake.y >= 600:
        snake.y = 2
    if snake.y <= 0:
        snake.y = 598


    # CURRENT VELOCITY
    if x_for_velocity > snake.x:
        current_velocity = 'left'
    if x_for_velocity < snake.x:
        current_velocity = 'right'
    if y_for_velocity > snake.y:
        current_velocity = 'up'
    if y_for_velocity < snake.y:
        current_velocity = 'down'


    # Collision
    collision = isCollission(apple.x, apple.y, snake.x, snake.y)
    if collision:
        if current_velocity == 'left':
            tails.append(Snake(snake.x, snake.y, snake.x_change, snake.y_change, snake.speed))
        if current_velocity == 'right':
            tails.append(Snake(snake.x, snake.y, snake.x_change, snake.y_change, snake.speed))
        if current_velocity == 'up':
            tails.append(Snake(snake.x, snake.y, snake.x_change, snake.y_change, snake.speed))
        if current_velocity == 'down':
            tails.append(Snake(snake.x, snake.y, snake.x_change, snake.y_change, snake.speed))

        score_value += 1
        apple.x = random.randint(50, 750)
        apple.y = random.randint(50, 550)

    draw_snake(snake.x, snake.y)
    draw_apple(apple.x, apple.y)

    for i in range(0, len(tails)):
        tail = tails[i]
        last_tail = tails[i - 1]
        tail.image = pygame.image.load('tail.png')

        if i == 0:
            if current_velocity == 'left':
                tail.x = snake.x + 40
                tail.y = snake.y
            if current_velocity == 'right':
                tail.x = snake.x - 40
                tail.y = snake.y
            if current_velocity == 'up':
                tail.y = snake.y + 40
                tail.x = snake.x
            if current_velocity == 'down':
                tail.y = snake.y - 40
                tail.x = snake.x
        elif i > 0:
            if current_velocity == 'left':
                tail.x = last_tail.x + 40
                tail.y = last_tail.y
            if current_velocity == 'right':
                tail.x = last_tail.x - 40
                tail.y = last_tail.y
            if current_velocity == 'up':
                tail.y = last_tail.y - 40
                tail.x = last_tail.x
            if current_velocity == 'down':
                tail.y = last_tail.y + 40
                tail.x = last_tail.x
        screen.blit(tail.image, (tail.x, tail.y))


    show_score(textX, textY)
    pygame.display.update()

    x_for_velocity = snake.x
    y_for_velocity = snake.y





