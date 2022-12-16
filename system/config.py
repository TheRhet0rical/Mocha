# Mocha Configuration File
# Needed for basic function of Mocha. Only edit if you know what your doing!

# You can view the objects in more detail in the Application Documentation.

# Imports
from platform import system as syss
from socket import gethostname, gethostbyname
from os.path import exists
from time import sleep
from os import system
from sys import stdout
from random import choice, randint
from pyfiglet import figlet_format
from urllib.request import urlopen

# Color Codes - Makes Mocha look fancier.
class c:
  white = "\033[0m"
  red = "\033[0;31m"
  blue = "\033[0;34m"
  green = "\033[0;32m"
  yellow = "\033[0;33m"
  purple = "\033[0;35m"
  
  italic = '\x1B[3m'
  underline = "\033[4m"
  crossed = "\033[9m"
  clear = '\x1B[0m'

# Console Class - Handles terminal functions.
class console:

    def clear():
      system('cls||clear')

    def delete_last_line():
      stdout.write('\x1b[1A')
      stdout.write('\x1b[2K')

    def title(text):
      banner = figlet_format(text)
      print(banner)

    def pause():
      input("Pause: ")
      console.delete_last_line()

    def wait(wait_time):
      sleep(wait_time)

# Mocha/System Class - Handles data that Mocha uses.
class mocha:
    name = 'Mocha'
    creator = 'Rhet0rical'
    developer_mode = False

    class version:  # Version Class - Handles Mocha's version data.
      build_type = 'stb'
      num = '0.6'
      full_version = f'{build_type}_{num}'

    class github:  # Github Class - Handles Github Data.
      link = 'https://github.com/TheRhet0rical/mocha-python-os'
      version = urlopen("https://raw.githubusercontent.com/TheRhet0rical/mocha-python-os/main/system/version.txt").read().decode('utf-8')

    class config:  # Config Class - Holds various settings for Mocha.
      start_on_run = True
      force_user_login = True
      show_ip_on_boot = False
      show_hostname_on_boot = True
      check_for_updates = True

class client:      # Client Class - Holds Clientside data.
  platform = syss()
  hostname = gethostname()
  ip_address = gethostbyname(hostname)
    
class v:            # V Class - Holds visual data and strings.
  l = '|>-------------------------------------------------------------------|>'
  s = '|>--------------------------------------------------------|>'
  p = f'{c.yellow}>{c.white}'