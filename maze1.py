  ##! /usr/bin/env python
## coding: utf-8
from random import randint

import pygame
from pygame.locals import *

from constants import *


pygame.init()

file = "Maze.txt"
def load():
    structure_maze = []
    with open(file, "r") as filename:
        for line in filename:
            line_maze = []
            for letter in line:
                if letter != "\n":
                    line_maze.append(letter)
            structure_maze.append(line_maze)
        return structure_maze

def position(position_x, position_y, direction, structure_maze):
    if direction == "q":
        if position_x > 0:
            if structure_maze[position_y][position_x-1] != "#":
                position_x -= 1
    elif direction == "d":
        if position_x < (len(structure_maze) - 1):
            if structure_maze[position_y][position_x+1] != "#":
                position_x += 1  
    elif direction == "z":
        if position_y > 0:
            if structure_maze[position_y-1][position_x] != "#":
                position_y -= 1
    elif direction == "s":
        if position_y < (len(structure_maze) - 1):
            if structure_maze[position_y+1][position_x] != "#":
                position_y += 1 
    return (position_x, position_y)           

def random_position(structure_maze):
    while True:
        position_y = randint(0, len(structure_maze) - 1)
        position_x = randint(0, len(structure_maze) - 1)
        if structure_maze[position_y][position_x] == " ":
            #x = position_x * letter_size 
            #y = position_y * letter_size    
            return (position_y, position_x)
           
def position_object(maze):
    for object in ["E", "N", "T"]:
        object_y, object_x = random_position(maze)
        maze[object_y][object_x] = object

def display(structure_maze):
    window = pygame.display.set_mode((450, 450))
    pygame.display.set_caption(window_title)
    WALL = pygame.image.load("images/wall.png").convert()
    MG = pygame.image.load("images/macgyver.png").convert_alpha() 
    GOAL = pygame.image.load("images/gardian.png").convert_alpha()
    FLOOR = pygame.image.load("images/floor.png").convert()
    ETHER = pygame.image.load("images/ethertest.png").convert_alpha()
    NEEDLE = pygame.image.load("images/needletest.png").convert()
    PIPE = pygame.image.load("images/pipetest.png").convert_alpha()
    ACCUEIL = pygame.image.load("images/title.PNG").convert()
    SYRINGE = pygame.image.load("images/seringue.png").convert_alpha()
    num_line = 0
    for line in structure_maze:
        num_col = 0
        for letter in line:     
            x = num_col * letter_size
            y = num_line * letter_size
            if letter == '#':
                window.blit(WALL, (x, y))   
                #if object_inventory == 3:
                    #window.blit(SYRINGE, (0, 0))
                
                if object_inventory == 1:
                    window.blit(ETHER, (0, 0)) or window.blit(PIPE, (0, 1))        
            elif letter == 'p' or letter == "M":
                window.blit(MG, (x, y))    
            elif letter == 'g':
                window.blit(GOAL, (x, y))   
            elif letter == " ":
                window.blit(FLOOR, (x, y))
            elif letter == "E":
                if object_inventory == 1:
                    window.blit(ETHER, (x, y))
                window.blit(ETHER, (x, y))    
            elif letter == "N":
                window.blit(NEEDLE, (x, y))  
            elif letter == "T":
                window.blit(PIPE, (x, y))   
            num_col += 1
        num_line += 1
    
    pygame.display.flip() 
def display_status(structure_maze, x, y, object_inventory):       
    if object_inventory == 3:
        window.blit(SYRINGE, (0,0))
        pygame.display.flip()
    if structure_maze[y][x] == "g":
        if object_inventory == 3:
            window.blit(GAME_WON,(0, 0))
            pygame.display.flip()
            pygame.time.delay(2000)
x = 1
y = 1
structure_maze = load()
position_object(structure_maze)
random_position(structure_maze)
object_inventory = 0
window = pygame.display.set_mode((450, 450))
pygame.display.set_caption(window_title)
#continue_game = 1
while True:
    accueil = pygame.image.load("images/title.png").convert()
    window.blit(accueil, (0, 0))
    pygame.display.flip()
    continue_game = 1
    continue_accueil = 1
   
    while continue_accueil:
        for event in pygame.event.get():
            if event.type == QUIT:
                continue_accueil = 0
                continue_game = 0
            elif event.type == KEYDOWN:				
               if event.key == K_F1:
                    continue_accueil = 0	
    
    ETHER = pygame.image.load("images/ethertest.png").convert_alpha()
    NEEDLE = pygame.image.load("images/needletest.png").convert()
    PIPE = pygame.image.load("images/pipetest.png").convert_alpha()
    SYRINGE = pygame.image.load("images/seringue.png").convert_alpha()    
    GAME_WON = pygame.image.load("images/game_won1.png").convert()
    GAME_OVER = pygame.image.load("images/game_over1.png").convert()
    while True:
        display(structure_maze) 
        display_status(structure_maze, x, y, object_inventory)
        #if structure_maze[y][x] == "g":
            #if object_inventory == 3:
                #window.blit(GAME_WON,(0, 0))
            #pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit() 
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = "q" 
                if event.key == K_RIGHT:
                    direction = "d"
                if event.key == K_UP:
                    direction = "z"
                if event.key == K_DOWN:
                    direction = "s"
                pygame.display.flip()
            
                structure_maze[y][x] = " "   
                x, y = position(x, y, direction, structure_maze)
                #print(x, y)   
                if structure_maze[y][x] in ["E", "N", "T"]:
                    object_inventory += 1
                    if structure_maze[y][x] in ["E"]:
                        window.blit(ETHER, (0, 0))
                    if structure_maze[y][x] in ["N"]:
                        window.blit(NEEDLE, (0,0)) 
                    if structure_maze[y][x] in ["T"]:
                        window.blit(PIPE, (0, 0))          
                    print(object_inventory)
                if structure_maze[y][x] == "g":
                    if object_inventory == 3:
                        window.blit(GAME_WON,(0, 0))
                        print("Game won")
                    else:
                        window.blit(GAME_OVER, (0, 0))
                        print("Game over")
                    #exit()
                structure_maze[y][x] = "M"
                pygame.display.flip()



