import pygame, math, sys
from os import path
from button import Button
from config import *




class Settings:
	def __init__(self, game, screen, display_surface):
		self.game = game
		self.screen = screen
		self.display_surface = display_surface
		self.hard_mode = False

		folders = os.listdir(BUTTONS_FOLDER)
		for folder in folders:
			BUTTONS[folder] = (pygame.image.load(path.join(BUTTONS_FOLDER, folder, "primary.png")).convert_alpha(), pygame.image.load(path.join(BUTTONS_FOLDER, folder, "secondary.png")).convert_alpha()) 
		
		self.buttons = []
		self.buttons.append(Button(825, 250, BUTTONS["Settings"]))
		self.buttons.append(Button(885, 400, BUTTONS["Difficulty"], self.set_difficulty))
		self.buttons.append(Button(885, 550, BUTTONS["Back"], self.go_back))


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

	def set_difficulty(self):
		if self.hard_mode == False:
			self.hard_mode = True
		else:
			self.hard_mode = False
		pygame.time.delay(100)

	def go_back(self):
		print("Back")
		pygame.time.delay(100)
		self.game.restart()


