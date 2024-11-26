import pygame, random

class Drone(pygame.sprite.Sprite):
  def __init__(self, type, x, y):
    super().__init__()
    self.type = type
    path = f"Graphics/drone_{type}.png"
    self.image = pygame.image.load(path)
    self.rect = self.image.get_rect(topleft = (x, y))
    

  def update(self, direction):
    self.rect.x += direction

  def position(self, speed):
    