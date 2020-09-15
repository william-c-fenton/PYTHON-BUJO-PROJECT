#testing pygame GUI

import pygame, sys, os
 
# Setup pygame/window ---------------------------------------- #

from pygame.locals import *
from Bujo import *
 

WHITE = (255, 255, 255)
BLACK = (0,0,0)

class GUI(object):
    def __init__(self):
        self.mainClock = pygame.time.Clock()
        
        pygame.init()
        pygame.display.set_caption('game base')

        #constants for screen width and height
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 500

        #create screen and font
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT),0,32)
        self.font = pygame.font.SysFont(None, 20)
        self.screen.fill(WHITE)

        #Initialize the bullet journal object
        self.journal = BuJo()
        self.journal.DailySpread.add_text("test post")

    #Draws text with left corner at x,y
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    #draws rectangular button with text in it
    def draw_button(self, text, font, color, rect_color, surface, x, y, w, h):
        textobj = font.render(text, 1, color)
        textrect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(surface, rect_color, textrect)
        surface.blit(textobj, textrect)
        return textrect

    #Display the main menu
    def main_menu(self):
        click = False
        while True:
            #set up the screen
            self.screen.fill(WHITE)
            self.draw_text('main menu', self.font, BLACK, self.screen, int((self.SCREEN_WIDTH/2)), 20)

            #get mouse position into mx,my tuple
            mx, my = pygame.mouse.get_pos()

            #Draw the buttons
            button_1 = self.draw_button("month", self.font, BLACK, (255, 0, 0), self.screen, 50, 50, 200, 50)
            button_2 = self.draw_button("day", self.font, BLACK, (255, 0, 0), self.screen, 50, 100, 200, 50)
            button_3 = self.draw_button("exit", self.font, BLACK, (255, 0, 0), self.screen, 50, 150, 200, 50)

            #Check if buttons are hovered or clicked
            if button_1.collidepoint((mx, my)):
                if click:
                    self.month(None)
            if button_2.collidepoint((mx, my)):
                if click:
                    self.day(None)
            if button_3.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()
                    
            #reset click
            click = False

            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
     
            pygame.display.update()
            self.mainClock.tick(60)

    #Display the month's menu
    def month(self, spread):
        running = True
        click = False
        while running:
            #set up screen
            self.screen.fill(WHITE)
            self.draw_text('month', self.font, BLACK, self.screen, self.SCREEN_WIDTH/2, 20)

            #get mouse pos tuple
            mx, my = pygame.mouse.get_pos()

            #make list of days (make a day object or something for these)
            days = []

            #width of the calendar entries
            width = int((self.SCREEN_WIDTH - 100) / 10)
            height = width

            #place days onto screen
            rx = 5
            ry = 0
            currday = 1
            for i in range(3):
                ry += 50
                rx = 5
                
                for j in range(10):
                    day = self.draw_button(str(currday), self.font, BLACK, (255,0,0), self.screen, rx, ry, width, height)
                    days.append(day)
                    rx += 50
                    currday += 1

            #check if any days are clicked
            for day in days:
                if day.collidepoint((mx, my)):
                    if click:
                        click = False
                        self.day(None)

            #update display
            pygame.display.update()

            #TODO:
            #Make calendar entries redirect to seperate day objects
            #Make calendar show correct number of days for the month
            #Make calendar show the month's title
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            
            pygame.display.update()
            self.mainClock.tick(60)

    #Display the day's menu
    def day(self, spread):
        running = True
        click = False
        while running:
            #init screen
            self.screen.fill(WHITE)
            self.draw_text('day', self.font, BLACK, self.screen, self.SCREEN_WIDTH/2, 20)

            #TODO:
            #set up display of bullets / text
                #make space for bullets
                #make space for text
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        
            pygame.display.update()
            self.mainClock.tick(60)
            
if __name__ == '__main__':
    Bujo = GUI()
    Bujo.main_menu()
    
