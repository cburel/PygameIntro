from Vector import Vector
import pygame
from pygame.locals import *

#setup
clock = pygame.time.Clock();

#the player class, a rectangle that moves across the screen
class Player():
	def __init__(self, pos: Vector(30, 30), vel: Vector(0, 0), size):
		self.pos = pos
		self.vel = vel
		self.size = size

	# draw the player rectangle on the screen
	def draw(self, screen):
		
		#make screen cornflower blue
		screen.fill((100,149,237))

		#draw the rectangle
		pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.pos.x, self.pos.y, self.size, self.size))

		# draw debug line
		lineStartX = self.pos.x + self.size/2
		lineStartY = self.pos.y + self.size/2
		lineEndX = (self.pos.x + self.size/2) + self.vel.x
		lineEndY = (self.pos.y + self.size/2) + self.vel.y
		pygame.draw.line(screen, (255, 0, 0), (lineStartX, lineStartY), (lineEndX, lineEndY), 3)


	# event handler
	def update(self):

		#setup
		keyPressed = pygame.key.get_pressed()
		spd = 1

		# event loop
		for event in pygame.event.get():

			#quit game
			if event.type == QUIT:
				pygame.quit()
				quit()

			#movement
			if keyPressed[pygame.K_w]:
				self.vel -= Vector(0, spd)
			if keyPressed[pygame.K_s]:
				self.vel += Vector(0, spd)
			if keyPressed[pygame.K_a]:
				self.vel -= Vector(spd, 0)
			if keyPressed[pygame.K_d]:
				self.vel += Vector(spd, 0)

			self.pos += Vector.normalize(self.vel)
				
			print("Pos: " + str(self.pos))
			print("Vel: " + str(self.vel))

			#flip display buffer
			pygame.display.flip()

			#constrain to 60 fps
			clock.tick(60)