import pygame
import math
pygame.init()

screenWindow = pygame.display.set_mode((1400,800))

class Symbol:
    def __init__(self,symbol):
        self.size = pygame.surface.Surface((200, 200))
        self.size.fill((255,255,255))
        self.rect = self.size.get_rect()
        self.symbol = symbol

    def Hover(self):
        pygame.draw.line(self.size, (0,0,0), (10,10), (10,190))
        pygame.draw.line(self.size, (0,0,0), (10,10), (190,10))
        pygame.draw.line(self.size, (0,0,0), (190,190), (10,190))
        pygame.draw.line(self.size, (0,0,0), (190,190), (190,10))
    
    def Draw(self):
        if self.symbol == None:
            pass
        elif self.symbol == "O":
            pygame.draw.circle(self.size, (0,0,0), (100,100), 60)
        elif self.symbol == "X":
            pygame.draw.line(self.size, (255,0,0), (20,20), (180,180), 5)
            pygame.draw.line(self.size, (255,0,0), (20,180), (180,20), 5)

class Board:
    def __init__(self):
        self.elements = [[Symbol(None),Symbol(None),Symbol(None)],
                        [Symbol(None),Symbol(None),Symbol(None)],
                        [Symbol(None),Symbol(None),Symbol(None)]]
        self.size = pygame.surface.Surface((600,600))
        self.size.fill((255,255,255))
        self.rect = self.size.get_rect()
        self.rect.center = (700,400)
        self.state = "O"
        self.lastpostion = None

    def Draw(self, screen, mouseUp):
        def DetectWin():
            elements = self.elements
            #Check from the last edited element its possibilities of winning
            x = self.lastpostion[1]
            y = self.lastpostion[0]
            #In a squa-
            # re of length 5, check every direction with a radius if 2. for loop 0-7 inclusive
            #Repeat 4 times, treat 'i' as the determinant of line orientation
            for i in range(0,4):
                #Initialise array 'line'
                line = []
                for j in range(-2,3):
                    #If index out of bounds, then 
                    try:
                        #East
                        if i ==  0:
                            if x + j < 0 or y < 0:
                                continue
                            line.append(elements[y][x+j])
                        #Northeast
                        elif i == 1:
                            if x + j < 0 or y-j < 0:
                                continue
                            line.append(elements[y-j][x+j])
                        #North
                        elif i == 2:
                            if x < 0 or y-j < 0:
                                continue
                            line.append(elements[y-j][x])
                        elif i == 3:
                            if x-j < 0 or y - j< 0:
                                continue
                            line.append(elements[y-j][x-j])
                    except:
                        continue
                print([a.symbol for a in line])
                if [a.symbol for a in line] == ['X','X','X'] or [a.symbol for a in line] == ['O','O','O']:
                    self.elements = [[Symbol(None),Symbol(None),Symbol(None)],
                            [Symbol(None),Symbol(None),Symbol(None)],
                            [Symbol(None),Symbol(None),Symbol(None)]]

            #Check if all spots are filled
            hasNone = False
            for row in elements:
                for element in row:
                    if element.symbol == None:
                        hasNone = True
                        break
            if hasNone == False:
                self.elements = [[Symbol(None),Symbol(None),Symbol(None)],
                            [Symbol(None),Symbol(None),Symbol(None)],
                            [Symbol(None),Symbol(None),Symbol(None)]]

        screen.blit(self.size, self.rect.topleft)
        for i in range(0, len(self.elements)):
            for j in range(0, len(self.elements[i])):
                element = self.elements[i][j]
                element.size.fill((255,255,255))
                element.rect.x = j * 200 + self.rect.left
                element.rect.y = i * 200 + self.rect.top
                if element.rect.collidepoint(pygame.mouse.get_pos()):
                    element.Hover()
                    if mouseUp == True:
                        if self.state == "O" and element.symbol == None:
                            element.symbol = "O"
                            self.state = "X"
                        elif self.state == "X" and element.symbol == None: 
                            self.state = "O"
                            element.symbol = "X"
                        self.lastpostion = [i,j]
                        DetectWin()
                        



                element.Draw()
               
                    
                screen.blit(element.size, element.rect.topleft)
        pygame.draw.line(screen, (0,0,0), (200+ self.rect.left,0+ self.rect.top), (200+ self.rect.left,600+ self.rect.top), 5)
        pygame.draw.line(screen, (0,0,0), (400+ self.rect.left,0+ self.rect.top), (400+ self.rect.left,600+ self.rect.top), 5)
        pygame.draw.line(screen, (0,0,0), (0+ self.rect.left,200+ self.rect.top), (600+ self.rect.left,200+ self.rect.top), 5)
        pygame.draw.line(screen, (0,0,0), (0+ self.rect.left,400+ self.rect.top), (600+ self.rect.left,400+ self.rect.top), 5)
        
            

            



board = Board()
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.MOUSEBUTTONUP:
            mouseUp = True
        else:
            mouseUp = False

    screenWindow.fill((0,0,0))
    board.Draw(screenWindow, mouseUp)
    pygame.display.update()

pygame.quit()