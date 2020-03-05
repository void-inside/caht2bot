# chat2bot
A CLI utility to transform exported whatsapp's chats into chatbots.


## How to

1. Export any chat you want from your whatsapp app whitout media.
1. Move the exported file to your computer.
1. Create a bot by 
```$ python chat2bot.py -c <path to the exported file> <target person to become a bot>```
1. To interact with the bot you jsut will need to load it.
  

## Usage

```bash
$ python chat2bot.py -h
        __          __     __           __          __ 
  _____/ /_  ____ _/ /_   / /_____     / /_  ____  / /_
 / ___/ __ \/ __ `/ __/  / __/ __ \   / __ \/ __ \/ __/
/ /__/ / / / /_/ / /_   / /_/ /_/ /  / /_/ / /_/ / /_  
\___/_/ /_/\__,_/\__/   \__/\____/  /_.___/\____/\__/  
                                                       

			-v1.0-


usage: chat2bot.py [-h] [-l LOAD] [-c CREATE CREATE] [-v]

Create chatbots from your Whatsapp's chats.

optional arguments:
  -h, --help            show this help message and exit
  -l LOAD, --load LOAD  Name of the bot to load.
  -c CREATE CREATE, --create CREATE CREATE
                        Chat's exported file from whatsapp and name of the
                        target.
  -v, --verbose         Show more information during execution.
```
