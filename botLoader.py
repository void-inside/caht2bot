# -*- coding: utf-8 -*-

import os
from whatsappConverter import SAVE_PATH
from chatterbot import ChatBot

class Bot:

    def __init__(self, name):

        if not os.path.isfile(os.path.join(SAVE_PATH, name + '.sqlite3')):
            print('[!!] Couldnt find a bot named %s' % name)
            self.ok = False
            return
        
        self.ok = True
        self._name = name
        self._bot = ChatBot(
            name,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///' + os.path.join(SAVE_PATH, name + '.sqlite3')
            )


    def interact(self, s):
        return '[' + self._name + '] ' + str(self._bot.get_response(s))


if __name__ == "__main__":
    bot = Bot('test')

    _in = input('>')

    while _in.lower() != 'exit':
        print(bot.interact(_in))
        _in = input('>')
