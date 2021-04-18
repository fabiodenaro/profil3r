import sys
from itertools import chain, combinations
from profil3r import core
from profil3r.colors import Colors
from multiprocessing import Process

CONFIG = './config.json'

def print_logo():
    print(Colors.OKGREEN + Colors.BOLD + '''
    ____             _____ _______     
   / __ \_________  / __(_) /__  /_____
  / /_/ / ___/ __ \/ /_/ / / /_ </ ___/
 / ____/ /  / /_/ / __/ / /___/ / /    
/_/   /_/   \____/_/ /_/_//____/_/     
                                       
''' + Colors.ENDC)

    print(Colors.HEADER + "Version 1.1.1 - Developped by Rog3rSm1th")
    print("You can buy me a coffee at : https://www.buymeacoffee.com/givocefo\n" + Colors.ENDC)


# Start the program
print_logo()

profil3r = core.Core(CONFIG, sys.argv[1:])
profil3r.get_permutations()

# Use command line arguments
arguments = sys.argv[1:]

# No argument
if not len(arguments):
    print('''Profil3r is an OSINT tool that allows you to find potential profiles of a person on social networks, as well as their email addresses. This program also alerts you to the presence of a data leak for the found emails.

Usage : ./main.py <arguments>
for exemple : ./main.py john doe
            ./main.py john doe 67''')

else:
    profil3r.run()