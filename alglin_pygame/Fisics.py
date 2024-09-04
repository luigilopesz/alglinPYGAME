import pygame
import numpy as np
import math

def lua_pos(dist, vel, dia):
  return dist * np.cos(2 * np.pi * dia * vel), dist * np.sin(2 * np.pi * dia * vel) / 1.5 # elipse 

def att_teleguiado(pos, mouse, velocidade):
  mouse = mouse[0] -28, mouse[1] -28
  vel = mouse - pos
  distancia = np.linalg.norm(vel)  
  if distancia != 0:  
    vel_normalizado = vel / distancia  
    return pos + (vel_normalizado * velocidade)
  return pos 

def att_tiro(pos, mouse, velocidade):
  mouse = mouse[0] -28, mouse[1] -28
  vel = mouse - pos
  distancia = np.linalg.norm(vel)    
  vel_normalizado = vel / distancia  
  return vel_normalizado * velocidade

def colide(tiro_mask, coisa_mask, tiro_pos, coisa_pos):
  return coisa_mask.overlap(tiro_mask, (tiro_pos[0] - coisa_pos[0], tiro_pos[1] - coisa_pos[1]))

def grav(posicao_objeto, posicao_planeta, fator_forca=30.0):
    posicao_objeto = np.array(posicao_objeto)
    posicao_planeta = np.array(posicao_planeta)
    
    # Calcular o vetor direção da posição do objeto para a posição do planeta
    vetor_direcao = posicao_planeta - posicao_objeto
    
    # Calcular a distância entre o objeto e o planeta
    distancia = np.linalg.norm(vetor_direcao)
    
    if distancia == 0:
        return (0.0, 0.0)  # O objeto já está na posição do planeta, não há movimento
    
    # Normalizar o vetor direção
    vetor_direcao_normalizado = vetor_direcao / distancia
    
    # Calcular a força inversamente proporcional à distância (quanto mais perto, mais forte)
    forca = fator_forca / distancia
    
    # Calcular o vetor de velocidade como produto da força e o vetor direção normalizado
    vetor_velocidade = vetor_direcao_normalizado * forca
    
    # Retornar como uma tupla
    return tuple(vetor_velocidade)