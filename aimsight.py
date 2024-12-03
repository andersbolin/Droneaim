import pygame, random

class Aimsight(pygame.sprite.Sprite):
  def __init__(self, type, x, y):
    super().__init__()
    self.type = type
    self.x = x
    self.y = y
    path = f"Graphics/aimsight.png"
    self.image = pygame.image.load(path)
    self.rect = self.image.get_rect(topleft = (x, y))
    

  def update(self, x, y):
    self.rect.x = x
    self.rect.y = y

  def position(self, x, y):
    self.x = x
    self.y = y

  