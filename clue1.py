import os
import pygame
import tkinter as tk
from pygame.locals import *
import win32gui, win32con
import time
from sys import exit

pygame.init()

def textObject(text, font, text_color):
    textSurface = font.render(text, True, text_color)
    return textSurface, textSurface.get_rect()


def clueOne(): 


   # name = e1.get()
   # major = e2.get()
   # guide = e3.get()
  #  pygame.mixer.music.stop()

    screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
    
#this stuff needs to be inside the function
    hwnd = win32gui.GetForegroundWindow() #you need this for the next line
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    pygame.display.set_caption('Clue 1')
    
#backgroundimage
    background = pygame.image.load('olmstedcartoon.JPG')
    pygame.display.set_icon(background)
    screen.fill((0,0,0))
    screen.blit(pygame.transform.scale(background, (500,500)), (0,0))
    pygame.display.flip()
    

    
    coffee_button_color = [215,132,121]
    soda_button_color = [215,132,121]
    redbull_button_color = [215,132,121]
    loop = True 

    while(loop): 
        riddle_box = pygame.draw.rect(screen, [225,225,225], [0, 0, 1400, 150])
        riddle_text = pygame.font.Font("freesansbold.ttf",45)
        textSurf, textRect = textObject("Dark roasted coffee beans have…", riddle_text, [0,0,0])
        textRect.center = ((0+(1400/2)), (0+(150/2)))
        screen.blit(textSurf, textRect)
        pygame.display.update()
        
        coffee_button = pygame.draw.ellipse(screen, coffee_button_color, [700, 600, 250, 100])
        coffee_button_text = pygame.font.Font("freesansbold.ttf",35)
        textSurf, textEllipse = textObject("Richer flavor", coffee_button_text, [0,0,0])
        textEllipse.center = ((700+(250/2)), (600+(100/2)))
        screen.blit(textSurf, textEllipse)
        pygame.display.update()
    
        
        
        soda_button = pygame.draw.ellipse(screen, soda_button_color, [1000, 600, 250, 100])
        soda_button_text = pygame.font.Font("freesansbold.ttf",35)
        textSurf, textEllipse = textObject("Less caffeine", soda_button_text, [0,0,0])
        textEllipse.center = ((1000+(250/2)), (600+(100/2)))
        screen.blit(textSurf, textEllipse)
        pygame.display.update()
    
        
        
        redbull_button = pygame.draw.ellipse(screen, redbull_button_color, [400, 600, 250, 100])
        redbull_button_text = pygame.font.Font("freesansbold.ttf",35)
        textSurf, textEllipse = textObject("Both", redbull_button_text, [0,0,0])
        textEllipse.center = ((400+(250/2)), (600+(100/2)))
        screen.blit(textSurf, textEllipse)
        pygame.display.update()
    
        pygame.event.pump()
    
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.quit: 
                quite()
                
            if 700+250 > pos[0] > 700 and 600+100 > pos[1] > 600:
                coffee_button_color = [55, 115, 250]
                coffee_button = pygame.draw.ellipse(screen, coffee_button_color, [700, 600, 250, 100])
                coffee_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Richer flavor", coffee_button_text, [0,0,0])
                textEllipse.center = ((700+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coffee_button_color = [55, 115, 150]
                    coffee_button = pygame.draw.ellipse(screen, coffee_button_color, [700, 600, 250, 100])
                    coffee_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Richer flavor", coffee_button_text, [0,0,0])
                    textEllipse.center = ((700+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    coffee_button_color = [215, 132, 121]
                    coffee_button = pygame.draw.ellipse(screen, coffee_button_color, [700, 600, 250, 100])
                    coffee_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Richer flavor", coffee_button_text, [0,0,0])
                    textEllipse.center = ((700+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
            else:
                coffee_button_color = [215, 132, 121]
                coffee_button = pygame.draw.ellipse(screen, coffee_button_color, [700, 600, 250, 100])
                coffee_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Richer flavor", coffee_button_text, [0,0,0])
                textEllipse.center = ((700+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                
            if 1000+250 > pos[0] > 1000 and 600+100 > pos[1] > 600:
                soda_button_color = [55, 115, 250]
                soda_button = pygame.draw.ellipse(screen, soda_button_color, [1000, 600, 250, 100])
                soda_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Less caffeine", soda_button_text, [0,0,0])
                textEllipse.center = ((1000+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    soda_button_color = [55, 115, 150]
                    soda_button = pygame.draw.ellipse(screen, soda_button_color, [1000, 600, 250, 100])
                    soda_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Less caffeine", soda_button_text, [0,0,0])
                    textEllipse.center = ((1000+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    soda_button_color = [215, 132, 121]
                    soda_button = pygame.draw.ellipse(screen, soda_button_color, [1000, 600, 250, 100])
                    soda_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Less caffeine", soda_button_text, [0,0,0])
                    textEllipse.center = ((1000+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
            else:
                soda_button_color = [215, 132, 121]
                soda_button = pygame.draw.ellipse(screen, soda_button_color, [1000, 600, 250, 100])
                soda_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Less caffeine", soda_button_text, [0,0,0])
                textEllipse.center = ((1000+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
            
            if 400+250 > pos[0] > 400 and 600+100 > pos[1] > 600:
                redbull_button_color = [55, 115, 250]
                redbull_button = pygame.draw.ellipse(screen, redbull_button_color, [400, 600, 250, 100])
                redbull_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Both", redbull_button_text, [0,0,0])
                textEllipse.center = ((400+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    redbull_button_color = [55, 115, 150]
                    redbull_button = pygame.draw.ellipse(screen, redbull_button_color, [400, 600, 250, 100])
                    redbull_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Both", redbull_button_text, [0,0,0])
                    textEllipse.center = ((400+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    redbull_button_color = [215, 132, 121]
                    redbull_button = pygame.draw.ellipse(screen, redbull_button_color, [400, 600, 250, 100])
                    redbull_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Both", redbull_button_text, [0,0,0])
                    textEllipse.center = ((400+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                    
            else:
                redbull_button_color = [215, 132, 121]
                redbull_button = pygame.draw.ellipse(screen, redbull_button_color, [400, 600, 250, 100])
                redbull_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Both", redbull_button_text, [0,0,0])
                textEllipse.center = ((400+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
        
            if event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
                pygame.display.flip()


 
clueOne()
