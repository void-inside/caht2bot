# -*- coding: utf-8 -*-
# import numpy as np

TARGET_BOT = u'Calvito Feliz😄'
TARGET_CHAT = u'chat.txt'
chat_matrix = []      # [<number interaction>] = [<my message>, <her response>]
chat_all = []

def starts_with_date(line):

    if '/' in line[0:7]:
        holder = line[0:7].split('/')

        return len(holder) == 3
    return False


# ̣Read file line by line
with open(TARGET_CHAT) as fp:
    line = fp.readline()
    interaction = 0
    author = u''
    message = u''
    time = ''
    date = ''
    ln_cnt = 1

    new_interaction = True

    try:
        while line:
            if starts_with_date(line):
                
                date, holder = [x.strip() for x in line.split(',', 1)]
                time, holder = [x.strip() for x in holder.split('-', 1)]
                author, message = [x.strip() for x in holder.split(':', 1)]

                if message[0] == '<' and message[-1] == '>':        # Multimedia
                    line = fp.readline()
                    continue

                if new_interaction and author == TARGET_BOT:
                    line = fp.readline()
                    continue

                if not new_interaction and author != TARGET_BOT:
                    new_interaction = True
                    interaction += 1
                
                if new_interaction:
                    chat_matrix.append([])
                    new_interaction = False

                chat_matrix[interaction].append(message)

            else:
                # Append to last interaction
                # TODO
                pass


            line = fp.readline()
            ln_cnt += 1

    except:
        print(line)

size = len(chat_matrix)
for i in range(len(chat_matrix)):
    interaction = chat_matrix[i]
    chat_matrix.append([interaction[0], '.'.join(interaction[1:])])



# print(chat_matrix[0:10])


# Carga el chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(TARGET_BOT, database=TARGET_BOT+'.sqlite3')

trainer = ListTrainer(bot)

# [trainer.train(x) for x in chat_matrix]

for i,x in enumerate(chat_matrix):

    print('{} de {}'.format(i, len(chat_matrix)))
    trainer.train(x)



