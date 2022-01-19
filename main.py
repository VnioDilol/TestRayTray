import pygame

res = wd, hi = 800, 600
play_pos = 400, 300

class MAP:
	def __init__(self,app):
		self.color = (120,120,120)
		self.screen = app.sc
		self.map_text = (
			'#######',
			'#.....#',
			'#.#...#',
			'#..##.#',
			'#..#..#',
			'#######'
			)
		self.map_pos = list()


		for num_row, row in enumerate(self.map_text):
			for num_char, char in enumerate(row):
				if char == '#':
					self.map_pos.append((num_char * 25,num_row * 25))
		#print(self.map_pos)
	
	def draw(self):
		for pos in self.map_pos:
			pygame.draw.rect(self.screen,self.color,(* pos,25,25),2) 
			#print(pos)

class App:
	def __init__(self):
		self.sc = pygame.display.set_mode(res)


	def run(self):
		map1 = MAP(app)
		map1.draw()
		while True:
			pygame.display.flip()
			#self.sc.fill('black')
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()

app = App()
app.run()
