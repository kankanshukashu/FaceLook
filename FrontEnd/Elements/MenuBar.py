from FrontEnd.Elements.Element import Element
import pygame


class MenuBar(Element):
    # state==0 idle
    # state==1 hover
    # state==2 select
    image = pygame.Surface((350, 45))
    image.fill((255, 255, 255))
    image_idle = pygame.Surface((117, 45))
    image_idle.fill((255, 255, 255))
    image_hover = pygame.Surface((117, 45))
    image_hover.fill((245, 245, 245))
    image_select = pygame.Surface((117, 45))
    image_select.fill((240, 240, 240))
    icon1 = pygame.transform.smoothscale(pygame.image.load('./resources/menuicon_1.png'), (30, 30))
    icon2 = pygame.transform.smoothscale(pygame.image.load('./resources/menuicon_2.png'), (30, 30))
    icon3 = pygame.transform.smoothscale(pygame.image.load('./resources/menuicon_3.png'), (30, 30))

    def __init__(self, process, location):
        Element.__init__(self, process)
        self.location = location
        self.size = (350, 45)
        self.buttonSize = (117, 45)
        self.icon = [MenuBar.icon1, MenuBar.icon2, MenuBar.icon3]
        self.surface = MenuBar.image
        self.buttonState = [2, 0, 0]
        self.buttonLocation = [(0, 0), (117, 0), (234, 0)]

    def posin(self, pos, index):
        x = pos[0]
        y = pos[1]
        if self.buttonLocation[index][0] < x < self.buttonLocation[index][0] + self.buttonSize[0] and \
                self.buttonLocation[index][1] < y < self.buttonLocation[index][1] + self.buttonSize[1]:
            return True
        return False

    def getEvent(self, event):
        if event.type == pygame.constants.MOUSEBUTTONDOWN or event.type == pygame.constants.MOUSEMOTION:
            event.pos = (event.pos[0] - self.location[0], event.pos[1] - self.location[1])
        if event.type == pygame.constants.MOUSEMOTION:
            for i in range(3):
                if self.buttonState[i] != 2:
                    if self.posin(event.pos, i):
                        self.buttonState[i] = 1
                    else:
                        self.buttonState[i] = 0
        if event.type == pygame.constants.MOUSEBUTTONDOWN and event.button == pygame.constants.BUTTON_LEFT:
            for i in range(3):
                if self.posin(event.pos, i):
                    self.buttonState = [0, 0, 0]
                    self.buttonState[i] = 2
        if event.type == pygame.constants.MOUSEBUTTONDOWN or event.type == pygame.constants.MOUSEMOTION:
            event.pos = (event.pos[0] + self.location[0], event.pos[1] + self.location[1])

    def display(self):
        surface = pygame.Surface.copy(self.surface)
        for i in range(3):
            if self.buttonState[i] == 0:
                surface.blit(MenuBar.image_idle, self.buttonLocation[i])
            elif self.buttonState[i] == 1:
                surface.blit(MenuBar.image_hover, self.buttonLocation[i])
            else:
                surface.blit(MenuBar.image_select, self.buttonLocation[i])
            surface.blit(self.icon[i], (self.buttonLocation[i][0] + 43, self.buttonLocation[i][1] + 7))
        for child in self.childs:
            if child.active:
                surface.blit(child.display(), child.location)
        return surface
