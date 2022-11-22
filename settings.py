import pygame, math, sys
from os import path
from button import Button
from config import *




class Settings:
	def __init__(self, game, engine, mode, screen, display_surface):
		self.game = game 
		self.engine = engine
		self.mode = mode
		self.screen = screen
		self.display_surface = display_surface

		folders = os.listdir(BUTTONS_FOLDER)
		BUTTONS = (pygame.image.load(path.join(BUTTONS_FOLDER, SETTINGS_IMAGES_FOLDER, "primary.png")).convert_alpha(), pygame.image.load(path.join(BUTTONS_FOLDER, SETTINGS_IMAGES_FOLDER, "secondary.png")).convert_alpha())
		
		self.buttons = []
		self.buttons.append(Button(760, 250, BUTTONS))


	def input_handler(self, event):
		return

	def standard(self):
		self.update()
		self.draw()

	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		for button in self.buttons:
			button.update(mouse_pos)

	def draw(self):
		self.screen.fill(WHITE)
		for button in self.buttons:
			self.screen.blit(button.current_image, (button.rect.x, button.rect.y))
		pygame.display.flip()
