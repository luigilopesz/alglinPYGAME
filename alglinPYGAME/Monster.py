import numpy as np
from random import uniform 


class Monster:
  def __init__(self, screen, state):
    self.vida = 1
    self.state = state
    self.screen_larg = screen.get_width()
    self.screen_alt = screen.get_height()

  def cria_alien(self):
    larg = uniform(0.7, 0.9)
    alt = uniform(0.2, 0.8)
    pos = np.array([self.screen_larg * larg, self.screen_alt * alt])
    return {'vida': self.vida, 'pos': pos}