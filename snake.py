# class olustur ve yilanin feature larini gir
# tailsize
# positionYilan
# velocity
# positionElma 
# yilanin parcalarini bir arreye ekleyip o arrayi ekrana yazdirman lazim 

import pygame
from pygame import mixer
import math
import random

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


# Player
playerImg = pygame.image.load('snake-head.png')
playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0
player_speed = 0.3

# Apple
appleImg = pygame.image.load('apple.png')
appleX = 500
appleY = 500
appleX_change = 0.1
appleY_change = 0.1

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))



def player(x, y):
    screen.blit(playerImg, (x, y))

def apple(x, y):
    screen.blit(appleImg, (x, y))


def isCollission(appleX, appleY, playerX, playerY):
    distance = math.sqrt((math.pow(appleX - playerX, 2)) + (math.pow(appleY - playerY, 2)))
    if distance > 25.7 and distance < 25.9:
        return True
    else:
        return False

# Game loop
running = True
while running:

    # RGB
    screen.fill((0, 100, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # MOVING for Player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -player_speed
                playerY_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = player_speed
                playerY_change = 0
            if event.key == pygame.K_DOWN:
                playerY_change = player_speed
                playerX_change = 0
            if event.key == pygame.K_UP:
                playerY_change = -player_speed
                playerX_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pass

    playerX += playerX_change
    playerY += playerY_change
    # TELEPORT
    if playerX >= 800:
        playerX = 2
    if playerX <= 0:
        playerX = 798
    if playerY >= 600:
        playerY = 2
    if playerY <= 0:
        playerY = 598


    #Collision
    collision = isCollission(appleX, appleY, playerX, playerY)
    if collision:
        score_value += 1
        appleX = random.randint(50, 750)
        appleY = random.randint(50, 550)

    player(playerX, playerY)
    apple(appleX, appleY)
    show_score(textX, textY)
    pygame.display.update()





