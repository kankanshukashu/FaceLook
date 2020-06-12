from FrontEnd.Elements.Window import Window
from FrontEnd.Elements.UserWindowBackground import UserWindowBackground
from Common.base import readData, writeData


class UserWindow(Window):
    def __init__(self, process):
        Window.__init__(self, process, 'FaceLook!', (350, 740), (255, 255, 255), True)
        self.bg = self.createChild(UserWindowBackground)
        self.set_rounded_rectangle(20)

    def getMessage(self, message):
        data = readData(self.process.data)

        # 获取好友列表
        try:
            if message['messageNumber'] == '4r':
                data['friendList'] = message['friendlist']
                writeData(self.process.data, data)
                self.bg.friend_list.refresh()
                return
        except KeyError:
            print('key error in 4r')

        # 获取未处理好友申请列表
        try:
            if message['messageNumber'] == '8r':
                data['friend_apply']['requestorList'] = message['requestorList']
                writeData(self.process.data, data)
                return
        except KeyError:
            print('key error in 8r')

        # 好友申请消息（服务端==>接收方）（仅限接收方在线）
        try:
            if message['messageNumber'] == '11r':
                data['friend_apply']['requestor'] = message
                writeData(self.process.data, data)
                return
        except KeyError:
            print('key error in 11r')

        # 好友申请回复结果（服务端==>申请方）（仅限申请方在线）
        try:
            if message['messageNumber'] == '13r':
                data['friend_apply']['receiver'] = message
                writeData(self.process.data, data)
                return
        except KeyError:
            print('key error in 13r')

        # 获取申请结果列表
        try:
            if message['messageNumber'] == '14r':
                data['friend_apply']['receiverList'] = message['receiverList']
                writeData(self.process.data, data)
                return
        except KeyError:
            print('key error in 14r')

        # 更改个人信息
        try:
            if message['messageNumber'] == '18r':
                data['user']['nickname'] = message['nickname']
                data['user']['avatarAddress'] = message['avatarAddress']
                data['user']['phoneNumber'] = message['phoneNumber']
                data['user']['invitee'] = message['invitee']
                data['user']['email'] = message['email']
                data['user']['occupation'] = message['occupation']
                data['user']['location'] = message['location']
                writeData(self.process.data, data)
                return
        except KeyError:
            print('key error in 18r')

        # 按昵称搜好友
        try:
            if message['messageNumber'] == '20r':
                data['search_nickname'] = message['userlist']
                writeData(self.process.data, data)
                return
        except KeyError:
            print('key error in 20r')

        # 按用户名搜好友
        try:
            if message['messageNumber'] == '21r':
                data['search_username'] = message['userlist']
                writeData(self.process.data, data)
        except KeyError:
            print('key error in 21r')
