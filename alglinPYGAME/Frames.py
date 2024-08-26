import pygame

class Frames:
  def __init__(self, img):
    self.img = img

  def sprite(self, frame, larg, alt, tamanho, cor):
    sprite = pygame.Surface((larg, alt)).convert_alpha()
    sprite.blit(self.img, (0, 0), ((frame * larg), 0, larg, alt))
    sprite = pygame.transform.scale(sprite, (larg * tamanho, alt * tamanho))
    sprite.set_colorkey(cor)
    return sprite
  
  def astro(self, larg, alt, tamanho, cor):
    astro = pygame.Surface((larg, alt)).convert_alpha()
    astro.blit(self.img, (0, 0))
    astro = pygame.transform.scale(astro, (larg * tamanho, alt * tamanho))
    astro.set_colorkey(cor)
    return astro
  
  def bg(self, larg, alt, tamanho, cor):
    bg = pygame.Surface((larg, alt)).convert_alpha()
    bg.blit(self.img, (0, 0))
    bg = pygame.transform.scale(bg, (larg * tamanho, alt * tamanho))
    bg.set_colorkey(cor)
    return bg
