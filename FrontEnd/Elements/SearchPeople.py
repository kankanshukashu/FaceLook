from FrontEnd.Elements.Element import Element
from FrontEnd.Elements.DropDownMenu import DropDownMenu
from FrontEnd.Elements.SingleInputBox import InputBox
from FrontEnd.Elements.TextButton import TextButton

import pygame


class SearchPeople(Element):
    input_border = pygame.image.load('./resources/SearchWindowUI/people_input_border.png')

    def __init__(self, process, location):
        Element.__init__(self, process)
        self.surface = pygame.Surface((700, 400))
        self.surface.fill((255, 255, 255))
        self.location = location
        self.menu = self.createChild(DropDownMenu, (50, 20), ['用户名', '昵称', '手机号', '邮箱'])
        self.input = self.createChild(InputBox, (200, 22), 350, 'dengxian', 24, (0, 0, 0), (255, 255, 255))
        self.search_button = self.createChild(TextButton, (580, 20), '搜索', 20, (80, 30))

    def getEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            event.pos = (event.pos[0] - self.location[0], event.pos[1] - self.location[1])
        for child in self.childs:
            if child.active:
                child.getEvent(event)
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            event.pos = (event.pos[0] + self.location[0], event.pos[1] + self.location[1])

    def display(self):
        surface = self.surface.copy()
        surface.blit(SearchPeople.input_border, (195, 20))
        for child in self.childs:
            if child.active:
                surface.blit(child.display(), child.location)
        return surface
