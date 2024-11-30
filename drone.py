import pygame, random

class Drone(pygame.sprite.Sprite):
  def __init__(self, type, x, y, speed):
    super().__init__()
    self.type = type
    self.x = x
    self.y = y
    self.speed = speed
    path = f"Graphics/drone_{type}.png"
    self.image = pygame.image.load(path)
    self.rect = self.image.get_rect(topleft = (x, y))
    

  def update(self, direction):
    self.rect.x += direction

  def position(self, x, y):
    self.x = x
    self.y = y