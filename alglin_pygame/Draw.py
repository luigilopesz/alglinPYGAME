import pygame
from alglin_pygame.Frames import *
from alglin_pygame.Fisics import *

class Draw:
  def __init__(self, screen, assets, state, stats):
    self.screen = screen
    self.screen_larg = screen.get_width()
    self.screen_alt = screen.get_height()

    self.assets = assets
    self.state = state
    self.stats = stats

    self.bg = Frames(assets['bg'].convert_alpha()).bg(522, 228, 2, (0,0,0))
    self.terra = Frames(assets['terra'].convert_alpha()).astro(25, 25, 6, (0,0,0))
    self.lua = Frames(assets['lua'].convert_alpha()).astro(25, 25, 3, (0,0,0))
    self.marte = Frames(assets['marte'].convert_alpha()).astro(25, 25, 6, (0,0,0))
    self.jupiter = Frames(assets['jupiter'].convert_alpha()).astro(25, 25, 10, (0,0,0))

    self.astronauta = Frames(assets['astronauta'].convert_alpha())
    self.astronauta_list = []
    for i in range(6):
      self.astronauta_list.append(self.astronauta.sprite(i, 24, 24, 4.5, (0,0,0)))

    self.alien = Frames(assets['alien'].convert_alpha())
    self.alien_list = []
    for i in range(4):
      self.alien_list.append(self.alien.sprite(i, 32, 32, 4.5, (0,0,0)))
    
    self.tiro = Frames(assets['tiro'])
    self.tiro_list = []
    for i in range(5):
      self.tiro_list.append(self.tiro.sprite(i, 80, 80, 0.7, (0,0,0)))

    self.teleguiado = Frames(assets['teleguiado'])
    self.teleguiado_list = []
    for i in range(5):
      self.teleguiado_list.append(self.teleguiado.sprite(i, 80, 80, 0.7, (0,0,0)))

    self.tick = pygame.time.get_ticks()
    self.cooldown = 100
    self.astronauta_frame = 0
    self.alien_frame = 0
    self.tiro_frame = 0
    self.teleguiado_frame = 0
    self.bg_frame_larg = 0
    self.bg_frame_alt = 0

  

  def draw_menu(self):
    def desenha_texto(texto, fonte, cor, superficie, x, y):
      obj_texto = fonte.render(texto, True, cor)
      rect_texto = obj_texto.get_rect()
      rect_texto.topleft = (x, y)
      superficie.blit(obj_texto, rect_texto)

    num_bg_x = (self.screen_larg // 1044) + 1
    num_bg_y = (self.screen_alt // 456) + 1

    for x in range(num_bg_x):
      for y in range(num_bg_y):
        self.screen.blit(self.bg, (x * 1044, y * 456))
    

    tick = pygame.time.get_ticks()
    if tick - self.tick >= self.cooldown:
      self.astronauta_frame += 1
      self.alien_frame += 1
      self.tiro_frame += 1
      self.teleguiado_frame += 1
      self.tick = tick
      if self.astronauta_frame >= len(self.astronauta_list):
        self.astronauta_frame = 0
      if self.alien_frame >= len(self.alien_list):
        self.alien_frame = 0
      if self.tiro_frame >= len(self.tiro_list):
        self.tiro_frame = 0
      if self.teleguiado_frame >= len(self.teleguiado_list):
        self.teleguiado_frame = 0


    self.state['lua']['pos'][0], self.state['lua']['pos'][1] = lua_pos(300, 1/600, self.state['dia'])


    desenha_texto(self.state['Q'], pygame.font.Font(None, 36), (255,255,255), self.screen, self.screen_larg * 0.2, self.screen_alt * 0.2)
    desenha_texto(f"Resposta: {self.state['resposta_jogador']}", pygame.font.Font(None, 36), (255,255,255), self.screen, self.screen_larg * 0.2, self.screen_alt * 0.3)
    desenha_texto(f"Resposta: 1142", pygame.font.Font(None, 36), (255,255,255), self.screen, self.screen_larg * 0.2, self.screen_alt * 0.5)
    self.screen.blit(self.terra, (self.state['terra']['pos'][0], self.state['terra']['pos'][1])) 
    self.screen.blit(self.lua, (self.state['terra']['pos'][0] + self.state['lua']['pos'][0], self.state['terra']['pos'][1] + self.state['lua']['pos'][1]))
    self.screen.blit(self.astronauta_list[self.astronauta_frame], (self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]))
    
  def draw_1(self):
    
    num_bg_x = (self.screen_larg // 1044) + 1
    num_bg_y = (self.screen_alt // 456) + 1

    for x in range(num_bg_x):
      for y in range(num_bg_y):
        self.screen.blit(self.bg, (x * 1044, y * 456))

    # astronauta idle
    tick = pygame.time.get_ticks()
    if tick - self.tick >= self.cooldown:
      self.astronauta_frame += 1
      self.alien_frame += 1
      self.tiro_frame += 1
      self.teleguiado_frame += 1
      self.tick = tick
      if self.astronauta_frame >= len(self.astronauta_list):
        self.astronauta_frame = 0
      if self.alien_frame >= len(self.alien_list):
        self.alien_frame = 0
      if self.tiro_frame >= len(self.tiro_list):
        self.tiro_frame = 0
      if self.teleguiado_frame >= len(self.teleguiado_list):
        self.teleguiado_frame = 0

    self.screen.blit(self.terra, (self.state['terra']['pos'][0], self.state['terra']['pos'][1])) 

    self.state['lua']['pos'][0], self.state['lua']['pos'][1] = lua_pos(300, 1/600, self.state['dia'])
    pygame.draw.circle(self.screen, (255, 255, 255), (self.state['terra']['pos'][0] + self.state['lua']['pos'][0] + 37.5, self.state['terra']['pos'][1] + self.state['lua']['pos'][1] + 37.5), 130, width=4)
    pygame.draw.circle(self.screen, (255, 255, 255), (self.state['jupiter']['pos'][0] + 125, self.state['jupiter']['pos'][1] + 125), 200, width=4)
    pygame.draw.circle(self.screen, (255, 255, 255), (self.state['marte']['pos'][0] + 75, self.state['marte']['pos'][1] + 75), 150, width=4)
    self.screen.blit(self.lua, (self.state['terra']['pos'][0] + self.state['lua']['pos'][0], self.state['terra']['pos'][1] + self.state['lua']['pos'][1]))
    self.screen.blit(self.astronauta_list[self.astronauta_frame], (self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]))
    self.screen.blit(self.jupiter, (self.state['jupiter']['pos'][0], self.state['jupiter']['pos'][1]))
    self.screen.blit(self.marte, (self.state['marte']['pos'][0], self.state['marte']['pos'][1]))


    for alien in self.state['aliens']:
      if alien['vida'] > 0:
        self.screen.blit(self.alien_list[self.alien_frame], alien['pos'])

    if self.state['atirou']:
      if self.stats['escolha'] == 'tiro':
        self.screen.blit(self.tiro_list[self.tiro_frame], self.stats['tiro_pos'])
      else:
        self.screen.blit(self.teleguiado_list[self.teleguiado_frame], self.stats['teleguiado_pos'])
