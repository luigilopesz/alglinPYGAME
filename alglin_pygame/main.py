import pygame 
from alglin_pygame.Events import *
from alglin_pygame.Draw import *
from alglin_pygame.Monster import *
import os

class Game:
  def __init__(self):
    pygame.init() 
    pygame.display.set_caption("Algebra Linear") 
    self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    self.screen_larg = self.screen.get_width()
    self.screen_alt = self.screen.get_height()
    self.clock = pygame.time.Clock()
    base_path = os.path.dirname(os.path.abspath(__file__))
    self.state = {
      'loop': True,
      'mouse_pos': [0,0],
      'atirou': False,
      'colisao': False,
      'lvl': 0,
      'dia': 0,
      'astronauta_pos': [self.screen_larg * 0.098, self.screen_alt * 0.49],
      'aliens': [],
      'terra': {
        'pos': [self.screen_larg * 0.085, self.screen_alt * 0.59],
      },
      'lua': {
        'pos': [0, 0],
        'vel': 0
      },
      'jupiter': {
        'pos': [self.screen_larg * 0.4, self.screen_alt * 0.6]
      },
      'marte': {
        'pos': [self.screen_larg * 0.5, self.screen_alt * 0.15]
      },
      'Q': 'Dados os vetores V1 e V2: v1 = [6, 8, 3, 3] e v2 = [5, 3, 1, -1]. Calcule v1 + v2.',
      'resposta_jogador': '',
      'resposta_correta': '1142'
    }
    
    monster = Monster(self.screen, self.state)
    for i in range(5):
      self.state['aliens'].append(monster.cria_alien())

    self.stats = {
      'escolha': 'tiro',
      'tiro_pos': np.array([self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]]),
      'tiro_vel': [0,0],
      'teleguiado_pos': np.array([self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]]),
      'entidade_pos': [0,0],
      'teleguiado': False,
      'ammo': 10
    }

    self.assets = {
            'astronauta': pygame.image.load(os.path.join(base_path, 'assets', 'Astronaut', 'Astronaut_Idle.png')),
            'alien': pygame.image.load(os.path.join(base_path, 'assets', 'Alien', 'Alien_idle.png')),
            'diamante': pygame.image.load(os.path.join(base_path, 'assets', 'Other sprites', 'Diamond.png')),
            'terra': pygame.image.load(os.path.join(base_path, 'assets', 'AssetJam', 'Earth.png')),
            'lua': pygame.image.load(os.path.join(base_path, 'assets', 'AssetJam', 'Moon.png')),
            'marte': pygame.image.load(os.path.join(base_path, 'assets', 'AssetJam', 'Mars.png')),
            'jupiter': pygame.image.load(os.path.join(base_path, 'assets', 'AssetJam', 'Jupiter.png')),
            'bg': pygame.image.load(os.path.join(base_path, 'assets', 'AssetJam', 'BackGround.png')),
            'tiro': pygame.image.load(os.path.join(base_path, 'assets', 'Astronaut', 'Tiro.png')),
            'teleguiado': pygame.image.load(os.path.join(base_path, 'assets', 'Astronaut', 'Tiro2.png'))
        }

  def game_loop(self):

    self.clock.tick(60)

    draw = Draw(self.screen, self.assets, self.state, self.stats)
    while self.state['loop']: 
      event = Events(self.state, self.stats, self.assets, self.screen).event()

      if self.state['lvl'] == 0:
        draw.draw_menu()
      elif self.state['lvl'] == 1:
        draw.draw_1()
      
      pygame.display.flip()

      self.state['dia'] += 1

def main():
    game = Game()
    try:
        game.game_loop()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
  main()