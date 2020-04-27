mport os
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

def wrong_answer():
    message = tk.Tk()
    tk.Label(message, text="Wrong answer!").grid(row=0)
    tk.Label(message, text="Be careful! You only get 3 wrong answers per game!").grid(row=1)
    
    message.mainloop()

def game_over():
    you_lost = tk.Tk()
    tk.Label(you_lost, text="Game Over!").grid(row=1)
    you_lost.mainloop()
    pygame.display.quit()
    welcomeScreen()

def clueFour(e1, e2, e3): 
    pygame.display.quit()

    name = e1.get()
    major = e2.get()
    guide = e3.get()
    pygame.mixer.music.stop()
    wrong_answers = 0

    screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
    
#this stuff needs to be inside the function
    hwnd = win32gui.GetForegroundWindow() #you need this for the next line
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    pygame.display.set_caption('Clue 1')
    
#backgroundimage
    background = pygame.image.load('sheslow.JPG')
    pygame.display.set_icon(background)
    screen.fill((0,0,0))
    screen.blit(pygame.transform.scale(background, (500,500)), (0,0))
    pygame.display.flip()
    

    
    option1_button_color = [215,132,121]
    option2_button_color = [215,132,121]
    option3_button_color = [215,132,121]
    loop = True 

    while(loop): 
        riddle_box = pygame.draw.rect(screen, [225,225,225], [0, 0, 1400, 150])
        riddle_text = pygame.font.Font("freesansbold.ttf",45)
        textSurf, textRect = textObject("Dark roasted coffee beans have…", riddle_text, [0,0,0])
        textRect.center = ((0+(1400/2)), (0+(150/2)))
        screen.blit(textSurf, textRect)
        pygame.display.update()
        
        option1_button = pygame.draw.ellipse(screen, option1_button_color, [700, 600, 250, 100])
        option1_button_text = pygame.font.Font("freesansbold.ttf",35)
        textSurf, textEllipse = textObject("Richer flavor", option1_button_text, [0,0,0])
        textEllipse.center = ((700+(250/2)), (600+(100/2)))
        screen.blit(textSurf, textEllipse)
        pygame.display.update()
    
        
        
        option2_button = pygame.draw.ellipse(screen, option2_button_color, [1000, 600, 250, 100])
        option2_button_text = pygame.font.Font("freesansbold.ttf",35)
        textSurf, textEllipse = textObject("Less caffeine", option2_button_text, [0,0,0])
        textEllipse.center = ((1000+(250/2)), (600+(100/2)))
        screen.blit(textSurf, textEllipse)
        pygame.display.update()
    
        
        
        option3_button = pygame.draw.ellipse(screen, option3_button_color, [400, 600, 250, 100])
        option3_button_text = pygame.font.Font("freesansbold.ttf",35)
        textSurf, textEllipse = textObject("Both", option3_button_text, [0,0,0])
        textEllipse.center = ((400+(250/2)), (600+(100/2)))
        screen.blit(textSurf, textEllipse)
        pygame.display.update()
    
        pygame.event.pump()
    
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.quit: 
                pygame.display.quite()
                
            if 700+250 > pos[0] > 700 and 600+100 > pos[1] > 600:
                option1_button_color = [55, 115, 250]
                option1_button = pygame.draw.ellipse(screen, option1_button_color, [700, 600, 250, 100])
                option1_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Richer flavor", option1_button_text, [0,0,0])
                textEllipse.center = ((700+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    option1_button_color = [55, 115, 150]
                    option1_button = pygame.draw.ellipse(screen, option1_button_color, [700, 600, 250, 100])
                    option1_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Richer flavor", option1_button_text, [0,0,0])
                    textEllipse.center = ((700+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    option1_button_color = [215, 132, 121]
                    option1_button = pygame.draw.ellipse(screen, option1_button_color, [700, 600, 250, 100])
                    option1_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Richer flavor", option1_button_text, [0,0,0])
                    textEllipse.center = ((700+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                    wrong_answers += 1
                    if wrong_answers > 3:
                        game_over()
                    else:
                        wrong_answer()
            else:
                option1_button_color = [215, 132, 121]
                option1_button = pygame.draw.ellipse(screen, option1_button_color, [700, 600, 250, 100])
                option1_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Richer flavor", option1_button_text, [0,0,0])
                textEllipse.center = ((700+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                
            if 1000+250 > pos[0] > 1000 and 600+100 > pos[1] > 600:
                option2_button_color = [55, 115, 250]
                option2_button = pygame.draw.ellipse(screen, option2_button_color, [1000, 600, 250, 100])
                option2_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Less caffeine", option2_button_text, [0,0,0])
                textEllipse.center = ((1000+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    option2_button_color = [55, 115, 150]
                    option2_button = pygame.draw.ellipse(screen, option2_button_color, [1000, 600, 250, 100])
                    option2_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Less caffeine", option2_button_text, [0,0,0])
                    textEllipse.center = ((1000+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    option2_button_color = [215, 132, 121]
                    option2_button = pygame.draw.ellipse(screen, option2_button_color, [1000, 600, 250, 100])
                    option2_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Less caffeine", option2_button_text, [0,0,0])
                    textEllipse.center = ((1000+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                    wrong_answers += 1
                    if wrong_answers > 3:
                        game_over()
                    else:
                        wrong_answer()
            else:
                option2_button_color = [215, 132, 121]
                option2_button = pygame.draw.ellipse(screen, option2_button_color, [1000, 600, 250, 100])
                option2_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Less caffeine", option2_button_text, [0,0,0])
                textEllipse.center = ((1000+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
            
            if 400+250 > pos[0] > 400 and 600+100 > pos[1] > 600:
                option3_button_color = [55, 115, 250]
                option3_button = pygame.draw.ellipse(screen, option3_button_color, [400, 600, 250, 100])
                option3_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Both", option3_button_text, [0,0,0])
                textEllipse.center = ((400+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    option3_button_color = [55, 115, 150]
                    option3_button = pygame.draw.ellipse(screen, option3_button_color, [400, 600, 250, 100])
                    option3_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Both", option3_button_text, [0,0,0])
                    textEllipse.center = ((400+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    option3_button_color = [215, 132, 121]
                    option3_button = pygame.draw.ellipse(screen, option3_button_color, [400, 600, 250, 100])
                    option3_button_text = pygame.font.Font("freesansbold.ttf",35)
                    textSurf, textEllipse = textObject("Both", option3_button_text, [0,0,0])
                    textEllipse.center = ((400+(250/2)), (600+(100/2)))
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                    #clueTwo(e1, e2, e3, wrong_answers)
                    
            else:
                option3_button_color = [215, 132, 121]
                option3_button = pygame.draw.ellipse(screen, option3_button_color, [400, 600, 250, 100])
                option3_button_text = pygame.font.Font("freesansbold.ttf",35)
                textSurf, textEllipse = textObject("Both", option3_button_text, [0,0,0])
                textEllipse.center = ((400+(250/2)), (600+(100/2)))
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
        
            if event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
                pygame.display.flip()