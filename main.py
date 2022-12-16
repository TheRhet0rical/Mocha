# Mocha Main Initiation File | 12/13/22
# Main initiation file for Mocha.

# Imported Modules (If Needed)
from system.config import *
from system.misc.quotes import quotes
from apps._mocha_home import mocha_home
from system.private.user_data import user

console.clear()

# Class Data
class main:
  name = 'main'                                              # (STR) Application Name.
  tag = 'main'                                               # (STR) App Tag, Usually 'SYS', 'APP', Or 'TST' Respectively.
  description = 'Main initiation file for Mocha.'            # (STR) App Description, Self Explanitory
  version = 'nv'                                             # (INT, STR) App Version, Also Self Explanitory OR (STR) 'nv' To Not Show Version.

  def launch():                                              # Every Application Will Need A Launch Function. Put Your App Code In This Function.

    # Splash
    console.clear()
    console.title(f'{mocha.name} v.{mocha.version.num}')
    print(f'{v.p} Quote: {c.green}\"{choice(quotes)}\"{c.white}\n')
    print(f'{v.s}\n')
    print(f'{v.p} Running Version: {c.purple}\"{mocha.version.full_version}\"{c.white}...')
    console.wait(1.3)
    print(f'  - Creator: {c.yellow}\"{mocha.creator}\"{c.white}')
    print(f'  - GitHub: {c.yellow}\"{mocha.github.link}\"{c.white}\n')

    # If Developer Mode Is Enabled, Let The Host Know.
    if mocha.developer_mode == True:
      print(f'  - Alert: {c.red}DEVELOPER{c.white} mode is enabled!\n')

    # Check Build Status
    print(f'{v.p} Checking Build Status...')
    console.wait(1.3)
    if mocha.version.build_type == 'dev':
      print(f'  - Running In {c.yellow}DEVELOPER{c.white} Mode!\n')
    elif mocha.version.build_type == 'stb':
      print(f'  - Running A {c.green}STABLE{c.white} Build!\n')
    elif mocha.version.build_type == 'pre':
      print(f'  - Running A {c.blue}EARLY ACCESS{c.white} Build!\n')
    else:
      print(f'  - Running An {c.blue}UNKNOWN{c.white} Build!\n')

    # Check For Updates (If Enabled)
    print(f'{v.p} Checking For Updates...')
    console.wait(1.3)
    if mocha.config.check_for_updates == True:
      if mocha.version.num < mocha.github.version:
        print(f'  - You Are Running An {c.red}Old{c.white} Build Of Mocha ({c.yellow}{mocha.github.version.strip()}{c.white}).\n')
      else:
        print(f'  - You Are Running A {c.green}Current{c.white} Build Of Mocha ({c.yellow}{mocha.github.version.strip()}{c.white}).\n')
    else:
      print(f'  - Checking For Updates Has Been {c.red}Disabled{c.white} On Your System.\n')
        
    # Print System Information To Console
    print(f'{v.p} Retrieving {c.purple}System{c.white} Information...')
    console.wait(1.3)
    print(f'  - mocha.name: {c.blue}\"{mocha.name}\"{c.white}')
    print(f'  - mocha.creator: {c.blue}\"{mocha.creator}\"{c.white}')
    print(f'  - mocha.developer_mode: {c.blue}\"{mocha.developer_mode}\"{c.white}')
    print(f'  - mocha.version.full_version: {c.blue}\"{mocha.version.full_version}\"{c.white}\n')

    # Print Client/Host Information To Console
    print(f'{v.p} Retrieving {c.purple}Client{c.white} Information...')
    console.wait(1.3)
    print(f'  - client.platform: {c.blue}\"{client.platform}\"{c.white}')

    # Show Hostname (If Enabled)
    if mocha.config.show_hostname_on_boot == True:
      print(f'  - client.hostname: {c.blue}\"{client.hostname}\"{c.white}')
    else:
      print(f'  - client.hostname: {c.blue}\"{c.italic}hidden\"{c.clear}{c.white}')

    # Show IP (If Enabled)
    if mocha.config.show_ip_on_boot == True:
      print(f'  - client.ip_address: {c.blue}\"{client.ip_address}\"{c.white}\n')
    else:
      print(f'  - client.ip_address: {c.blue}\"{c.italic}hidden\"{c.clear}{c.white}\n')

    print(f'{v.s}\n')

    # Login To System (If Enabled)
    if mocha.config.force_user_login == True:
      username_guess = input(f'{v.p} Enter The Account {c.blue}Login ID{c.white}: ')

      if username_guess == user.login_id:
        print(f'  - {c.green}Successfully{c.white} Retrieved The User Data.\n')
        password_guess = input(f'{v.p} Enter The Account {c.blue}Password{c.white}: ')

        if password_guess == user.password:
          print(f'  - {c.green}Logging Into{c.white} Mocha As {user.display_name}. Loading Mocha Home...\n\n{v.s}\n')
          console.wait(2)
          mocha_home.launch()
        else:
          print(f'  - {c.red}Failed{c.white} To Log In. Check Your Password And Try Again.\n\n{v.s}')
          console.wait(2)
          exit()

      else:
        print(f'  - {c.red}Failed{c.white} To Log Into Mocha. Check Your Username And Try Again.\n\n{v.s}')
        console.wait(2)
        exit()

    else:
      print(f'{v.p} Logging Into Mocha As {c.yellow}\"{user.display_name}\"{c.white}. Loading Mocha Home...\n\n{v.s}')
      console.wait(2)
      mocha_home.launch()
        
# If enabled, will start on run
if mocha.config.start_on_run == True:
  main.launch()
else:
  print(f'{v.p} Variable \"{c.yellow}start_on_run{c.white}\" Set To: {mocha.config.start_on_run}, Disabling')
  print(f'  Mocha From Starting Automatically.')