from vars import *
import pygame

class MAP:
	def __init__(self):
		self.color = (120,120,120)		
		self.map_text = (
			'#########################',
			'#.......................#',
			'#.......................#',
			'#..#....................#',
			'#.......................#',
			'#.......................#',
			'#.......................#',
			'#.......................#',
			'#...........##..........#',
			'#.........##............#',
			'#..............#........#',
			'#.......................#',
			'#.......................#',
			'#.......................#',
			'#.......................#',
			'#.......................#',
			'#.......................#',
			'#.......................#',
			'#..#....................#',
			'#########################'
			)
		self.map_pos = list()


		for num_row, row in enumerate(self.map_text):
			for num_char, char in enumerate(row):
				if char == '#':
					self.map_pos.append((num_char * (wd / 25),num_row * (hi / 20)))
		#print(self.map_pos)
	
	def draw(self,app,player):
		self.player = player
		self.screen = app.sc
		for pos in self.map_pos:
			pygame.draw.rect(self.screen,self.color,(* pos,30,30),2) 
			pygame.draw.rect(self.screen,'green',(self.player.x - 10, self.player.y - 10, 20, 20),1) 
			pygame.draw.line(self.screen,'green',(self.player.x, self.player.y), (400,300))
			#print(pos)))