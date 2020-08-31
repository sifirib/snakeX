
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


snake = Snake(400, 300, 0, 0, 1)
apple = Apple(400, 400)


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
    if distance > 5 and distance < 25.9:
        return True
    else:
        return False

j = 0
i = -1
sayac = 0
x_for_velocity = snake.x
y_for_velocity = snake.y
tails = []
step = 0
# Game loop
running = True
while running:

    snake_x = snake.x
    snake_y = snake.y

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
        if len(tails) > 0:
            if current_velocity == 'left':
                tails.append(Snake(tails[-1].x + 32, tails[-1].y, tails[-1].x_change, tails[-1].y_change, tails[-1].speed))
            if current_velocity == 'right':
                tails.append(Snake(tails[-1].x - 32, tails[-1].y, tails[-1].x_change, tails[-1].y_change, tails[-1].speed))
            if current_velocity == 'up':
                tails.append(Snake(tails[-1].x, tails[-1].y + 32, tails[-1].x_change, tails[-1].y_change, tails[-1].speed))
            if current_velocity == 'down':
                tails.append(Snake(tails[-1].x, tails[-1].y - 32, tails[-1].x_change, tails[-1].y_change, tails[-1].speed))
        if len(tails) == 0:
            if current_velocity == 'left':
                tails.append(Snake(snake.x + 32, snake.y, snake.x_change, snake.y_change, snake.speed))
            if current_velocity == 'right':
                tails.append(Snake(snake.x - 32, snake.y, snake.x_change, snake.y_change, snake.speed))
            if current_velocity == 'up':
                tails.append(Snake(snake.x, snake.y + 32, snake.x_change, snake.y_change, snake.speed))
            if current_velocity == 'down':
                tails.append(Snake(snake.x, snake.y - 32, snake.x_change, snake.y_change, snake.speed))
            snake_x = tails[0].x
            snake_y = tails[0].y



        score_value += 1
        apple.x = random.randint(50, 750)
        apple.y = random.randint(50, 550)

    draw_apple(apple.x, apple.y)
    draw_snake(snake.x, snake.y)


    print(i)
    print("  ", len(tails))
    if len(tails) == 1:
        tail = tails[i]
        tail.image = pygame.image.load('tail.png')
        if current_velocity == 'left':
            screen.blit(tail.image, (snake_x + 32, snake_y))
            old_position_x, old_position_y = tails[0].x, tails[0].y
            tails[0].x = snake_x + 32
            tails[0].y = snake_y
        if current_velocity == 'right':
            screen.blit(tail.image, (snake_x - 32, snake_y))
            old_position_x, old_position_y = tails[0].x, tails[0].y
            tails[0].x = snake_x - 32
            tails[0].y = snake_y
        if current_velocity == 'up':
            screen.blit(tail.image, (snake_x, snake_y + 32))
            old_position_x, old_position_y = tails[0].x, tails[0].y
            tails[0].x = snake_x
            tails[0].y = snake_y + 32
        if current_velocity == 'down':
            screen.blit(tail.image, (snake_x, snake_y - 32))
            old_position_x, old_position_y = tails[0].x, tails[0].y
            tails[0].x = snake_x
            tails[0].y = snake_y - 32


    if len(tails) > 1:
        tail = tails[i]
        tail.image = pygame.image.load('tail.png')
        if current_velocity == 'left':
            screen.blit(tail.image, (old_position_x + 32, old_position_y))
            old_position_xx, old_position_yy = tails[i].x, tails[i].y
            tails[i].x = old_position_x + 32
            tails[i].y = old_position_y
            old_position_x, old_position_y = old_position_xx, old_position_yy
        if current_velocity == 'right':
            screen.blit(tail.image, (old_position_x - 32, old_position_y))
            old_position_xx, old_position_yy = tails[i].x, tails[i].y
            tails[i].x = old_position_x - 32
            tails[i].y = old_position_y
            old_position_x, old_position_y = old_position_xx, old_position_yy
        if current_velocity == 'up':
            screen.blit(tail.image, (old_position_x, old_position_y + 32))
            old_position_xx, old_position_yy = tails[i].x, tails[i].y
            tails[i].x = old_position_x
            tails[i].y = old_position_y + 32
            old_position_x, old_position_y = old_position_xx, old_position_yy
        if current_velocity == 'down':
            screen.blit(tail.image, (old_position_x, old_position_y - 32))
            old_position_xx, old_position_yy = tails[i].x, tails[i].y
            tails[i].x = old_position_x
            tails[i].y = old_position_y - 32
            old_position_x, old_position_y = old_position_xx, old_position_yy


    show_score(textX, textY)
    pygame.display.update()

    x_for_velocity = snake.x
    y_for_velocity = snake.y


    if i == len(tails) - 1:
        i = -2
    i += 1



