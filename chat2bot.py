#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyfiglet import Figlet
# f = Figlet(font='slant')
# print f.renderText('text to render')

import argparse

if __name__ == "__main__":
    # Header
    fig = Figlet(font='slant')
    print(fig.renderText('chat to bot') + '\n\t\t\t-v1.0-\n\n')

    # Arguments definition
    praser = argparse.ArgumentParser(
        description='Create chatbots from your Whatsapp\'s chats.'
    )

    praser.add_argument(
        '-l', '--load',
        nargs=1,
        help='Name of the bot to load.'
    )

    praser.add_argument(
        '-c', '--create',
        nargs=2,
        help='Chat\'s exported file from whatsapp and name of the target.'
    )

    praser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show more information during execution.'
    )

    try:

        # Grab passed args
        args = praser.parse_args()

        if args.load:
            # Import what I need
            from botLoader import Bot

            bot = Bot(args.load[0])
            if not bot.ok:
                exit()
            if args.verbose:
                print('[*] Loaded without a problem.')
                print('[*] Starting chat loop.')

            # Chat loop
            _in = input('[You] > ')
            while _in.lower() != 'exit':
                print(bot.interact(_in))
                _in = input('[You] > ')

        elif args.create:
            # Import what I need
            from whatsappConverter import Whatsapp2Bot
            w2b = Whatsapp2Bot(args.verbose)
            w2b.set_params(args.create[0], args.create[1])
            w2b.gather_data()
            w2b.make_bot()


    except:
        pass
