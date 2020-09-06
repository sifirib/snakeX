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
# Create menu screen
win = pygame.display.set_mode((800, 600))
# Caption and icon
pygame.display.set_caption("SnakeX")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

class Snake:

    def __init__(self, x, y, x_change, y_change, speed):
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

the_value = 0
snake = Snake(400, 300, 0, 0, 32)
apple = Apple(400, 400)
game_speed = 0.05

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)
textX = 10
textY = 10

class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def redrawWindow():
    easyButton.draw(win)
    mediumButton.draw(win)
    hardButton.draw(win)
    insaneButton.draw(win)

easyButton = button((0, 100, 0), 150, 225, 120, 80, 'EASY')
mediumButton = button((0, 100, 0), 350, 225, 120, 80, 'MEDIUM')
hardButton = button((0, 100, 0), 550, 225, 120, 80, 'HARD')
insaneButton = button((0, 100, 0), 350, 350, 120, 80, 'INSANE')

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def draw_snake(x, y):
    screen.blit(snake.image, (x, y))

def draw_apple(x, y):
    screen.blit(apple.image, (x, y))

def isCollission(apple_x, apple_y, snake_x, snake_y):
    distance = math.sqrt((math.pow(apple_x - snake_x, 2)) + (math.pow(apple_y - snake_y, 2)))
    if distance > 0 and distance < 33:
        return True
    else:
        return False

# Main menu
run_menu = True
running = False
color = (0, 100, 0)
while run_menu:
    win.fill(color)
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        # MOUSE behaviours
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easyButton.isOver(pos) or mediumButton.isOver(pos) or hardButton.isOver(pos) or insaneButton.isOver(pos):
                run_menu = False
                running = True
        if event.type == pygame.MOUSEMOTION:
            if easyButton.isOver(pos):
                easyButton.color = (255, 255, 100)
                game_speed = 0.1
            else:
                easyButton.color = (0, 100, 0)
            if mediumButton.isOver(pos):
                mediumButton.color = (255, 255, 0)
                game_speed = 0.04

            else:
                mediumButton.color = (0, 100, 0)
            if hardButton.isOver(pos):
                hardButton.color = (255, 255, 0)
                game_speed = 0.01

            else:
                hardButton.color = (0, 100, 0)
            if insaneButton.isOver(pos):
                insaneButton.color = (255, 0, 0)
                easyButton.color = (255, 0, 0)
                mediumButton.color = (255, 0, 0)
                hardButton.color = (255, 0, 0)
                color = (255, 0, 0)
                easyButton.height -= 10
                easyButton.width -= 10
                mediumButton.height -= 10
                hardButton.height -= 10
                hardButton.width += 10
                pygame.display.update()
                game_speed = 0.005

            else:
                insaneButton.color = (0, 100, 0)
                color = (0, 100, 0)

    sayac = 0
    x_for_velocity = snake.x
    y_for_velocity = snake.y
    tails = []
    step = 0
    # Game loop
    while running:
        time.sleep(game_speed)
        snake_x = snake.x
        snake_y = snake.y

        # RGB
        screen.fill((0, 100, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run_menu = False

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
                tails.append(Snake(tails[-1].x + 1, tails[-1].y, tails[-1].x_change, tails[-1].y_change, tails[-1].speed))
            if len(tails) == 0:
                tails.append(Snake(snake.x + 1, snake.y, snake.x_change, snake.y_change, snake.speed))
                snake_x = tails[0].x
                snake_y = tails[0].y

            score_value += 1
            apple.x = random.randint(50, 750)
            apple.y = random.randint(50, 550)
            if score_value >= 200:
                apple.x = random.randint(50, 750)
                apple.y = random.randint(50, 550)

        draw_apple(apple.x, apple.y)
        draw_snake(snake.x, snake.y)

        for i in range(0, len(tails)):
            tail = tails[i]
            tail.image = pygame.image.load('tail.png')
            print(tail.x)
            print(tail.y)
            if tail.x <= snake.x <= tail.x + 1 and tail.y <= snake.y <= tail.y + 1:
                print("Game over")
                running = False
                run_menu = True
                score_value = 0
                snake.x = 400
                snake.y = 300
                snake.x_change = 0
                snake.y_change = 0
                text = font.render("Game Over", True, (255, 255, 255))
                screen.fill(color)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                screen.blit(text, [text_x, text_y])
                pygame.display.update()
                time.sleep(2)

            if i == 0:
                if current_velocity == 'left':
                    screen.blit(tail.image, (snake_x + the_value, snake_y))
                    old_position_x, old_position_y = tails[0].x, tails[0].y
                    tails[0].x = snake_x + the_value
                    tails[0].y = snake_y
                if current_velocity == 'right':
                    screen.blit(tail.image, (snake_x - the_value, snake_y))
                    old_position_x, old_position_y = tails[0].x, tails[0].y
                    tails[0].x = snake_x - the_value
                    tails[0].y = snake_y
                if current_velocity == 'up':
                    screen.blit(tail.image, (snake_x, snake_y + the_value))
                    old_position_x, old_position_y = tails[0].x, tails[0].y
                    tails[0].x = snake_x
                    tails[0].y = snake_y + the_value
                if current_velocity == 'down':
                    screen.blit(tail.image, (snake_x, snake_y - the_value))
                    old_position_x, old_position_y = tails[0].x, tails[0].y
                    tails[0].x = snake_x
                    tails[0].y = snake_y - the_value

            if i > 0:
                if current_velocity == 'left':
                    screen.blit(tail.image, (old_position_x + the_value, old_position_y))
                    old_position_xx, old_position_yy = tails[i].x, tails[i].y
                    tails[i].x = old_position_x + the_value
                    tails[i].y = old_position_y
                    old_position_x, old_position_y = old_position_xx, old_position_yy
                if current_velocity == 'right':
                    screen.blit(tail.image, (old_position_x - the_value, old_position_y))
                    old_position_xx, old_position_yy = tails[i].x, tails[i].y
                    tails[i].x = old_position_x - the_value
                    tails[i].y = old_position_y
                    old_position_x, old_position_y = old_position_xx, old_position_yy
                if current_velocity == 'up':
                    screen.blit(tail.image, (old_position_x, old_position_y + the_value))
                    old_position_xx, old_position_yy = tails[i].x, tails[i].y
                    tails[i].x = old_position_x
                    tails[i].y = old_position_y + the_value
                    old_position_x, old_position_y = old_position_xx, old_position_yy
                if current_velocity == 'down':
                    screen.blit(tail.image, (old_position_x, old_position_y - the_value))
                    old_position_xx, old_position_yy = tails[i].x, tails[i].y
                    tails[i].x = old_position_x
                    tails[i].y = old_position_y - the_value
                    old_position_x, old_position_y = old_position_xx, old_position_yy

        show_score(textX, textY)
        pygame.display.update()

        x_for_velocity = snake.x
        y_for_velocity = snake.y

        step += 1
