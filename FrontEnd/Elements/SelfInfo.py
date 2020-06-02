from FrontEnd.Elements.Element import Element
from FrontEnd.Elements.Avatar import Avatar
from FrontEnd.Elements.text_default import text_default
import pygame


class SelfInfo(Element):
    image = pygame.image.load('./resources/UserWindowUI/user_info.png')

    def __init__(self, process, location, user):
        Element.__init__(self, process)
        self.location = location
        self.user = user
        self.size = (350, 100)
        self.avatar = self.createChild(Avatar, (15, 15), user.get_avatarURL())
        self.nicknameText = self.createChild(text_default, (100, 36), self.user.nickname, (0, 0, 0))
        self.surface = SelfInfo.image
