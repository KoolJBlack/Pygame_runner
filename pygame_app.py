from pygame_runner import *

class my_pygame_app(base_pygame_app):

	def setup(self):
		self.size(640, 480)

	def draw(self):
		pass

	def mouse_pressed(self, x, y):
		print 'mouse pressed'

	def key_pressed(self, key):
		if key == pygame.K_ESCAPE:
			self.quit()


# =============================================================================
# Runner Methods
# =============================================================================
if __name__ == '__main__':
	pygame_app = my_pygame_app()
	pygame_app.run()