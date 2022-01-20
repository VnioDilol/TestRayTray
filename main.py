import pygame
from vars import *
from Map import *
from player import *

player = Player(center_pos)

class App:
	def __init__(self):
		self.sc = pygame.display.set_mode(res)


	def run(self):
		map1 = MAP(app, player)
		while True:
			player.move()
			map1.draw()
			pygame.display.flip()
			self.sc.fill('black')
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()

app = App()
app.run()
