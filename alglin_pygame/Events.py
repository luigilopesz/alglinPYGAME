import pygame
from alglinPYGAME.Fisics import *
import sys

class Events:
    def __init__(self, state, stats, assets, screen):
        self.keys = pygame.key.get_pressed()
        self.state = state
        self.stats = stats
        self.screen = screen
        self.assets = assets

    def event(self):
        if self.state['lvl'] == 0:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:  # Corrigido 'event' para 'evento'
                        self.state['loop'] = False
                    if evento.key == pygame.K_BACKSPACE:
                        self.state['resposta_jogador'] = self.state['resposta_jogador'][:-1]
                    elif evento.key == pygame.K_RETURN:
                        # Verifica se a resposta está correta
                        if self.state['resposta_jogador'] == self.state['resposta_correta']:
                            self.state['lvl'] = 1
                            self.stats['teleguiado'] = True
                            self.stats['escolha'] = 'teleguiado'
                        else:
                            self.state['lvl'] = 1
                        self.state['resposta_jogador'] = ""  # Reseta a resposta para próxima pergunta
                    else:
                        self.state['resposta_jogador'] += evento.unicode
        else:
            self.state['mouse_pos'] = pygame.mouse.get_pos()
            if 0 > self.stats['entidade_pos'][0] or self.stats['entidade_pos'][0] > self.screen.get_width() or 0 > self.stats['entidade_pos'][1] or self.stats['entidade_pos'][1] > self.screen.get_height():
                self.state['atirou'] = False 
                self.stats['tiro_pos'] = np.array([self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]])
                self.stats['teleguiado_pos'] = np.array([self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]])
                self.stats['entidade_pos'] = [0,0]
            for evento in pygame.event.get():  
                if evento.type == pygame.KEYDOWN:  
                    if evento.key == pygame.K_ESCAPE:  
                        self.state['loop'] = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        if self.state['atirou'] == False:
                            self.state['atirou'] = True
                            if self.stats['escolha'] == 'tiro' and self.stats['ammo'] >= 0:
                                self.stats['ammo'] -= 1
                                if self.stats['ammo'] < 0:
                                    self.state['loop'] = False
                                self.stats['tiro_vel'] = att_tiro(self.stats['tiro_pos'], self.state['mouse_pos'], 8)

            if self.state['atirou'] == True:
              if self.stats['escolha'] == 'tiro' and self.stats['ammo'] >= 0:  # tiro
                  self.stats['tiro_pos'] += self.stats['tiro_vel']
                  self.stats['entidade_pos'] = self.stats['tiro_pos']
              elif self.stats['teleguiado'] == True:
                  self.stats['teleguiado_pos'] = att_teleguiado(self.stats['teleguiado_pos'], self.state['mouse_pos'], 5)  # Verifique a velocidade
                  self.stats['entidade_pos'] = self.stats['teleguiado_pos']

            
            tiro = self.assets['tiro'].convert_alpha()
            tiro = pygame.transform.scale(tiro, (80 * 0.7, 80 * 0.7))
            tiro_mask = pygame.mask.from_surface(tiro)
            
            alien = self.assets['alien'].convert_alpha()
            alien = pygame.transform.scale(alien, (32 * 4.5, 32 * 4.5))
            alien_mask = pygame.mask.from_surface(alien)

            raio_lua = 130
            lua_pos = (self.state['terra']['pos'][0] + self.state['lua']['pos'][0], 
                        self.state['terra']['pos'][1] + self.state['lua']['pos'][1])

            raio_jupiter = 200
            pos_jupiter = (self.state['jupiter']['pos'][0], self.state['jupiter']['pos'][1])

            raio_marte = 150
            pos_marte = (self.state['marte']['pos'][0], self.state['marte']['pos'][1])

            tiro_pos = self.stats['tiro_pos']

            # Calcular a distância entre o tiro e o centro do círculo
            distancia_lua = np.linalg.norm(np.array(tiro_pos) - np.array(lua_pos))
            gravidade_total = np.array([0.0, 0.0])

            if distancia_lua <= raio_lua:
                gravidade_lua = grav(tiro_pos, lua_pos)
                gravidade_total += gravidade_lua

            # Calcular a gravidade da terra
            distancia_jupiter = np.linalg.norm(np.array(tiro_pos) - np.array(pos_jupiter))

            if distancia_jupiter <= raio_jupiter:
                gravidade_jupiter = grav(tiro_pos, pos_jupiter)
                gravidade_total += gravidade_jupiter

            distancia_marte = np.linalg.norm(np.array(tiro_pos) - np.array(pos_marte))
            if distancia_marte <= raio_marte:
                gravidade_marte = grav(tiro_pos, pos_marte)
                gravidade_total += gravidade_marte

            # Aplicar a gravidade total ao tiro
            self.stats['tiro_vel'] += gravidade_total
                
            aliens = self.state['aliens']
            mortos = 0
            for alien in aliens:
                if alien['vida'] > 0:
                    if colide(tiro_mask, alien_mask, self.stats['tiro_pos'], alien['pos']):
                        alien['vida'] -= 1
                        self.state['atirou'] = False
                        self.stats['tiro_pos'] = np.array([self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]])
                        self.stats['teleguiado_pos'] = np.array([self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]])
                        self.stats['entidade_pos'] = [0,0]
                    if colide(tiro_mask, alien_mask, self.stats['teleguiado_pos'], alien['pos']):
                        alien['vida'] -= 1
                        self.state['atirou'] = False
                        self.stats['tiro_pos'] = np.array([self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]])
                        self.stats['teleguiado_pos'] = np.array([self.state['astronauta_pos'][0], self.state['astronauta_pos'][1]])
                        self.stats['entidade_pos'] = [0,0]
                        self.stats['teleguiado'] = False
                        self.stats['escolha'] = 'tiro'
                else:
                    mortos += 1
                    if mortos == 5:
                        self.state['loop'] = False
        pygame.display.update()
        return True
