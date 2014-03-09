import pygame
pygame.init()

# =============================================================================
# Constants 
# =============================================================================
# Screen size
DEFAULT_WIDTH = 640
DEFAULT_HEIGHT = 480
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# =============================================================================
# Base class
# =============================================================================
class BasePygameApp:

	def __init__(self):
		self.running = False

	def init_runner(self):
		pass

	def run(self):
		# Init the runner
		self.init_runner()

		# Setup the app
		self.setup()

		# Loop on draw while app runs
		self.running = True
		while self.running:
			# Process all pygame events 
			for event in pygame.event.get():
				# Quitting
				if event.type == pygame.QUIT: 
					running = False
				# Mouse Events
				elif event.type == pygame.MOUSEBUTTONDOWN:
					#pos = pygame.mouse.get_pos()j
					pos = event.pos
					self.mouse_pressed(pos[0], pos[1])
				elif event.type == pygame.KEYDOWN:
					key = event.key
					self.key_pressed(key)
				else:
					#print event.type
					continue


			# Draw the app
			self.draw()

			# Update the screen
			pygame.display.flip()

	# =============================================================================
	# Methods to extend
	# =============================================================================
	def setup(self):
		self.size(DEFAULT_WIDTH, DEFAULT_HEIGHT)

	def draw(self):
		pass

	def mouse_pressed(self, x,y):
		pass

	def key_pressed(self, key):
		pass

	# =============================================================================
	# Util Methods
	# =============================================================================
	def size(self, width, height):
		self.screen = pygame.display.set_mode((width, height))

	def background(self, color):
		self.screen.fill(color)

	def quit(self):
		self.running = False
