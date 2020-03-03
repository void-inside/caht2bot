# -*- coding: utf-8 -*

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

SAVE_PATH = os.path.join(os.getcwd(), 'bots')

def starts_with_date(line):

    if '/' in line[0:7]:
        holder = line[0:7].split('/')

        return len(holder) == 3
    return False

class Whatsapp2Bot:

    def __init__(self, verbose=False):
        self._file = u''
        self._saveAs = u''
        self.chat_matrix = []
        self._verbose = verbose
        self._bot = None
        self._small_sample = None

        if not os.path.exists(SAVE_PATH):
            os.mkdir(SAVE_PATH)


    def gather_data(self):

        with open(self._file) as fp:
            line = fp.readline()
            interaction = 0
            author = u''
            message = u''
            time = ''                   # Unused now
            date = ''                   # Unused now
            ln_cnt = 1
            new_interaction = True

            try:

                if self._verbose:
                    print('[*] Loading data from %s' % self._file)

                while line:

                    # Starts with date == new msg
                    if starts_with_date(line):
                
                        date, holder = [x.strip() for x in line.split(',', 1)]
                        time, holder = [x.strip() for x in holder.split('-', 1)]
                        author, message = [x.strip() for x in holder.split(':', 1)]

                        # Discard media msgs
                        if message[0] == '<' and message[-1] == '>':
                            line = fp.readline()
                            continue

                        # Discard starting msgs made by the target
                        if new_interaction and author == self._saveAs:
                            line = fp.readline()
                            continue

                        # Check whether a new interaction begins
                        if not new_interaction and author != self._saveAs:
                            new_interaction = True
                            interaction += 1
                        
                        # Create row for each interaction
                        if new_interaction:
                            self.chat_matrix.append([])
                            new_interaction = False

                    # Add it to the matrix
                    self.chat_matrix[interaction].append(message)

                    # Prepare new iteration
                    line = fp.readline()
                    ln_cnt += 1

            except:
                print('[!!] Breaks in line: %s' % line)
                return

            if self._verbose:
                print('[*] Loaded %s lines of chat' % ln_cnt)

            if self._small_sample:

                if self._verbose:
                    print('[*] Using whole chat in order to add samples')

                for i in range(len(self.chat_matrix)):
                    interaction = self.chat_matrix[i]
                    self.chat_matrix.append([interaction[0], '.'.join(interaction[1:])])


    def set_params(self, in_file, target_name, small_sample=True):

        self._small_sample = small_sample
        self._file = in_file
        self._saveAs = target_name


    def make_bot(self):

        if len(self.chat_matrix) <= 0:
            print('[!!] Not enough data supplemented.')
            return
        
        # Create Object
        self._bot = ChatBot(
            self._saveAs,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///' + os.path.join(SAVE_PATH, self._saveAs + '.sqlite3')
            )

        # Create trainer
        trainer = ListTrainer(self._bot)

        # Train bot
        if self._verbose:
            for i,x in enumerate(self.chat_matrix):
                print('{} of {}'.format(i, len(self.chat_matrix)))
                trainer.train(x)
        else:
            [trainer.train(x) for x in self.chat_matrix]

        return self.get_bot()

    def get_bot(self):
        return self._bot



# Testing
if __name__ == "__main__":
    
    wb = Whatsapp2Bot(True)
    wb.set_params('chat.txt', 'test')
    wb.gather_data()
    bot = wb.make_bot()