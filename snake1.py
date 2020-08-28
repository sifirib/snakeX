# class olustur ve yilanin feature larini gir
# tailsize
# positionYilan
# velocity
# positionElma
# yilanin parcalarini bir arreye ekleyip o arrayi ekrana yazdirman lazim

import pygame

# Intialize the pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))


class Snake:

    def __init__(self, tail_size, position_x, position_y, velocity, position_ex, position_ey):
        self.tail_size = tail_size
        self.position_x = position_x
        self.position_y = position_y
        self.position_ex = position_ex
        self.position_ey = position_ey
        self.velocity = velocity


snake = Snake(10, 20, 20, 5, 40, 40)


def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))

