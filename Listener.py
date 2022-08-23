import datetime
import os
import threading
import time

import requests

import ciyun


class Listener:
    ip = '127.0.0.1'
    hp = '5700'
    wp = '8888'

    def __init__(self, i, h, w):
        self.ip = i
        self.hp = h
        self.wp = w

    def sendGroupMsg(self, group_id, msg):
        url = f'http://{self.ip}:{self.hp}/send_group_msg?group_id={group_id}&message={msg}'
        print(f'send|group|({group_id}){msg}')
        return requests.get(url)

    def sendPrivateMsg(self, user_id, msg):
        url = f'http://{self.ip}:{self.hp}/send_private_msg?user_id={user_id}&message={msg}'
        print(f'send|private({user_id}){msg}')
        return requests.get(url)

    def recG(self, group_id, user_id, msg, sender):
        """
            sender用于发送群聊消息，用法
            sender(group_id, msg)
        """
        try:
            if msg == '查看词云':
                f = open(f'./wordCloud/{group_id}.txt','r')
                word = f.read()
                f.close()
                cy = ciyun.cy(word, 15)
                filename = os.getcwd() + f'/wordCloud/{group_id}.png'
                cy.showWordCloud(filename)
                threading.Thread(target=self.sendGroupMsg, args=(group_id, f'[CQ:image,file=file:///{filename}]')).start()

            else:
                #   分群把文本填充到txt
                f = open(f'./wordCloud/{group_id}.txt','a')
                f.write(msg)
                f.close()
        except Exception as e:
            print(f"error=> {e}")
            return

    def recP(self, user_id, msg, sender):
        """
            sender用于发送私聊消息，用法
            sender(user_id, msg)
        """
        if msg == 'rm':
            autoclear()
        return ''

def autoclear():
    while True:
        time.sleep(60)
        #   每分钟执行一次
        tm = datetime.datetime.now()
        if tm.hour == 0 & tm.minute == 0:
            for file in os.listdir('./wordCloud'):
                os.remove('./wordCloud/' + file)
