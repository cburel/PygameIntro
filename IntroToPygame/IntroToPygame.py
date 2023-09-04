import pygame
from pygame.locals import *
from Player import Player
from Vector import Vector

#initialize pygame
pygame.init()

#setup
display_width = 800
display_height = 600
yPos = 30
xPos = 30
initVel = 0
size = 25
clock = pygame.time.Clock();
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_mode((display_width, display_height))
player = Player(Vector(xPos, yPos), Vector(initVel, initVel), (size))

#main gameplay loop
while True:

	#draw the player
	player.draw(screen)

	#update the player
	player.update()