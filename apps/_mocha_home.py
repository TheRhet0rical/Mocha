# Mocha Home (Launcher) | 12/13/22, Rhet0rical
# Built-In Application Launcher For Mocha.

# Imported Modules (If Needed)
from system.config import *
from system.private.user_data import user
from apps.exampleApplication import exampleApplication
from apps.aiplayground import aiplayground

# Load List, Everything Here Will Be Loaded Into Home (If Imported Correctly, Shouldn't Show Up As An Error In Your IDE)
loadlist = [
  exampleApplication,
  aiplayground
]

# Class Data
class mocha_home:
  name = 'Mocha Home (Built-In Launcher)'                              # (STR) Application Name.
  tag = 'LAU'                                                          # (STR) App Tag, Usually 'SYS', 'APP', Or 'TST' Respectively.
  description = 'Built-In Application Launcher For Mocha.'             # (STR) App Description, Self Explanitory
  version = 'nv'                                                       # (INT, STR) App Version, Also Self Explanitory OR (STR) 'nv' To Not Show Version.

  def launch():
    console.clear()
    console.wait(1)
    print(f'{v.l}\n')

    # Title & Details
    console.title(f' > {mocha.name} v.{mocha.version.num}')
    print(f' {v.p} This Version Of Mocha Is Created By: {c.blue}{mocha.creator}{c.white}\n')
    print(f' {v.p} Active {c.purple}Session{c.white} Details:')
    print(f'  - Currently Logged In As: {c.blue}{user.display_name}{c.white}')
    print(f'  - Host Platform: {c.blue}{client.platform}/{client.hostname}{c.white}')
    print(f'  - Developer Mode: {c.blue}{mocha.developer_mode}{c.white}\n\n{v.s}\n')

    # App Launcher
    print(f' {v.p} Please Select Your {c.purple}Choice{c.white} From The Options Below...\n')

    currentitemnum = 0
    for x in range(len(loadlist)):
      currentitemname = loadlist[currentitemnum]
      try: 
        if currentitemname.version == 'nv':
          print(f' {c.yellow}{currentitemnum + 1}{c.white} - [{c.italic}{c.blue}{currentitemname.tag}{c.white}{c.clear}] {currentitemname.name}')
        else:
          print(f' {c.yellow}{currentitemnum + 1}{c.white} - [{c.italic}{c.blue}{currentitemname.tag}{c.white}{c.clear}] {currentitemname.name} v.{currentitemname.version}') 
        print(f'     {currentitemname.description}\n')
      except:
        print(f' {v.p} {c.yellow}{currentitemnum + 1}{c.white} | {c.red}Failed To Load Application{c.white}!')
      currentitemnum = currentitemnum + 1

    if len(loadlist) == 0:
      print(f' {c.red}!{c.white} - [{c.italic}ERR{c.clear}] No Found Applications!')
      print(f'     No Applications Detected In {c.italic}loadlist{c.clear}. Check Your Imports.\n')

    # Choice Input
    choice = input(f'{v.s}\n\n {v.p} Enter An {c.purple}Option{c.white}: ')

    if int(choice) < len(loadlist) + 1:
      print(f'  - Loading Application: {c.blue}{loadlist[int(choice) - 1].name}{c.white}...\n\n{v.l}')
      console.wait(2)
      console.clear()
      console.wait(0.3)
      loadlist[int(choice) - 1].launch()
    else:
      print(f'  - {c.red}Failed{c.white} To Load The App Based On The Supplied Answer.\n\n{v.l}')
      console.wait(2)
      mocha_home.launch()