import pygame
import math

class Player:
	def __init__(self,center_pos):
		self.cenX, self.cenY = center_pos
		self.speed = 0.0025
		self.angle = 0
		self.rad = 160 
		self.x, self.y = self.get_pos()

	def move(self):
		self.x, self.y = self.get_pos()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.angle -= self.speed
		if keys[pygame.K_d]:
			self.angle += self.speed
		#print(self.x,self.y)

	def get_pos(self):
		a = math.sin(self.angle) * self.rad
		b = math.cos(self.angle) * self.rad
		x = self.cenX + b
		y = self.cenY + a
		return (x, y)
