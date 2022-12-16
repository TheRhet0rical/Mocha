# {application name} | {date created}, {creator}
# {description}, {license, if applicable}

# Imported Modules (If Needed)
from system.config import *

# Class Data
class exampleApplication:
  name = 'Example Application'                                # (STR) Application Name.
  tag = 'APP'                                                 # (STR) App Tag, Usually 'SYS', 'APP', Or 'TST' Respectively.
  description = 'This is an tutorial / example application.'  # (STR) App Description, Self Explanitory
  version = '1.0'                                             # (INT, STR) App Version, Also Self Explanitory OR (STR) 'nv' To Not Show Version.

  def launch():                                               # Every Application Will Need A Launch Function. Put Your App Code In This Function.
    print(f'Hello, World!')