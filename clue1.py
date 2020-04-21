import os
import pygame 
from pygame.locals import *
import win32gui, win32con 
import time 

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
pygame.display.set_caption('Clue 1')

def textObject(text, font, text_color):
    textSurface = font.render(text, True, text_color)
    return textSurface, textSurface.get_rect()

def clueOne(): 

	screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
	
	#backgroundimage
	background = pygame.image.load('olmstedcartoon.JPG')
	pygame.display.set_icon(background)
	screen.fill((0,0,0))
	screen.blit(pygame.transform.scale(background, (500,500)), (0,0))
	pygame.display.flip()

	#riddle
	riddle = pygame.draw.rect(screen, [255,255,255], [500,275, 530, 340])
	riddle_text = pygame.font.Font("freesansbold.ttf", 20)
	textSurf, textRect = textObject("Riddle: Although I’m not magic, I am a type of bean. I’m something you can drink that has lots of caffeine. Please select the answer the riddle, if you are correct you will be transported to the next clue if not, you will get to choose again.", riddle_text, [125,125,125])
	screen.blit(textSurf,textRect)
	pygame.display.update() 


	#coffeebutton 
	coffee_button_color = [215,132,121]
	coffee_button = pygame.draw.circle(screen, coffee_cup_color, (100,215), 500)
	coffee_button_text = pygame.font.FONT("freesansbold.ttf", 20)
	textSurf, textPolygon = textObject()
	pygame.display.update()


	pygame.event.pump()

	for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.quit: 
                pygame.mixer.music.stop()
                quite()
                
            if 100 > pos[0] > 215 and  100 > pos[1] > 215:
                coffee_button_color = [215,132,121]
                begin_button = pygame.draw.cirlce(screen, coffee_button_color, (100,215), 500)
                button_text = pygame.font.Font("freesansbold.ttf", 20)
                textSurf, textCircle = textObject("Coffee", button_text, [0,0,0])
                screen.blit(textSurf, textCircle)
                pygame.display.update()
                if event.type == pygame.get_pressed(1,0,0):
                    coffee_button_color = [55, 115, 150]
                    coffee_begin_button = pygame.draw.ellipse(screen, button_color, (100,215), 500)
                    coffee_button_text = pygame.font.Font("freesansbold.ttf", 20)
                    textSurf, textCircle = textObject("Coffee", button_text, [0,0,0])
                    screen.blit(textSurf, textCircle)
                    pygame.display.update()
                    clueTwo(screen, button)
            else:
                coffee_button_color = [215, 132, 121]
                coffee_button = pygame.draw.circle(screen, button_color, (100,215), 500)
                coffee_button_text = pygame.font.Font("freesansbold.ttf", 20)
                textSurf, textCircle = textObject("Begin", button_text, [0,0,0])
                screen.blit(textSurf, textCircle)
                pygame.display.update()
           
        
            if event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
                pygame.display.flip()

    #sodabutton
    soda_button_color = [215,132,121]
	soda_button = pygame.draw.circle(screen, coffee_cup_color, (100,215), 500)
	soda_button_text = pygame.font.FONT("freesansbold.ttf", 20)
	textSurf, textCircle = textObject()
	pygame.display.update()


	pygame.event.pump()

	for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.quit: 
                pygame.mixer.music.stop()
                quite()
                
            if 100 > pos[0] > 215 and  100 > pos[1] > 215:
                coffee_button_color = [215,132,121]
                begin_button = pygame.draw.circle(screen, button_color,(700,800), 500)
                button_text = pygame.font.Font("freesansbold.ttf", 20)
                textSurf, textCircle = textObject("Soda", button_text, [0,0,0])
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_color = [55, 115, 150]
                    begin_button = pygame.draw.ellipse(screen, button_color, (700,800), 500)
                    button_text = pygame.font.Font("freesansbold.ttf", 20)
                    textSurf, textCircle = textObject("Begin", button_text, [0,0,0])
                    screen.blit(textSurf, textCircle)
                    pygame.display.update()
                    clueOne(screen, button)

            else:
                button_color = [230, 135, 0]
                begin_button = pygame.draw.circle(screen, button_color, (700,800), 500)
                button_text = pygame.font.Font("freesansbold.ttf", 20)
                textSurf, textEllipse = textObject("Begin", button_text, [0,0,0])
                textEllipse.center = (100, 215
                screen.blit(textSurf, textCircle)
                pygame.display.update()
           
        
            if event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
                pygame.display.flip()

    #redbullbutton
    redbull_button_color = [215,132,121]
	redbull_button = pygame.draw.circle(screen, coffee_cup_color, (1400, 1500), 500)
	redbull_button_text = pygame.font.FONT("freesansbold.ttf", 20)
	textSurf, textCircle = textObject()
	pygame.display.update()


	pygame.event.pump()

	for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.quit: 
                pygame.mixer.music.stop()
                quite()
                
            if 100 > pos[0] > 215 and  100 > pos[1] > 215:
                redbull_button_color = [215,132,121]
                redbull_button = pygame.draw.circle(screen, button_color,(1400,1500), 500)
                redbull_button_text = pygame.font.Font("freesansbold.ttf", 20)
                textSurf, textCircle = textObject("Soda", button_text, [0,0,0])
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_color = [55, 115, 150]
                    begin_button = pygame.draw.ellipse(screen, button_color,)
                    button_text = pygame.font.Font("freesansbold.ttf", 20)
                    textSurf, textEllipse = textObject("Begin", button_text, [0,0,0])
                    screen.blit(textSurf, textEllipse)
                    pygame.display.update()
                    clueTwo(screen, button)

            else:
                button_color = [230, 135, 0]
                begin_button = pygame.draw.ellipse(screen, button_color, (1400,1500), 500)
                button_text = pygame.font.Font("freesansbold.ttf", 20)
                textSurf, textEllipse = textObject("Begin", button_text, [0,0,0])
                screen.blit(textSurf, textEllipse)
                pygame.display.update()
           
        
            if event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
                pygame.display.flip()



clueOne()


