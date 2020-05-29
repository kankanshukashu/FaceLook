from FrontEnd.Elements.Element import Element
from FrontEnd.Elements.text_default import text_default
import pygame


class MainMenu(Element):
    image = pygame.Surface((150, 80))
    image.fill((255, 255, 255))

    def __init__(self, process, location, user):
        Element.__init__(self, process)
        self.disable()
        self.location = location
        self.user = user
        self.size = (150, 80)
        self.surface = MainMenu.image
        self.createChild(MainMenuBlock, (0, 0), user, 0)
        self.createChild(MainMenuBlock, (0, 40), user, 1)

    def getEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            event.pos = (event.pos[0] - self.location[0], event.pos[1] - self.location[1])
        for child in self.childs:
            child.getEvent(event)
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            event.pos = (event.pos[0] + self.location[0], event.pos[1] + self.location[1])


class MainMenuBlock(Element):
    # block_type==0 个人资料
    # block_type==1 ？？？
    image = pygame.Surface((150, 40))
    image.fill((250, 250, 250))
    image_onHover = pygame.Surface((150, 40))
    image_onHover.fill((240, 240, 240))

    def __init__(self, process, location, user, block_type):
        Element.__init__(self, process)
        if block_type == 0:
            self.text = '个人资料'
        elif block_type == 1:
            self.text = '？？？'
        self.block_text = self.createChild(text_default, (12, 6), self.text, (0, 0, 0))
        self.surface = MainMenuBlock.image
        self.location = location
        self.size = (150, 40)
        self.block_type = block_type
        self.user = user

    def pos_in(self, pos):
        x, y = pos[0], pos[1]
        if self.location[0] < x < self.location[0] + self.size[0] and self.location[1] < y < self.location[1] + \
                self.size[1]:
            return True
        return False

    def getEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.pos_in(event.pos):
                self.state = 1
                self.surface = MainMenuBlock.image_onHover
            else:
                self.state = 0
                self.surface = MainMenuBlock.image
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            if self.pos_in(event.pos):
                print(self.text)

                # do something