# > **ALERT**: This version of Mocha is no longer being worked on.

# **Mocha** :coffee: - A Text Based Python Mock OS
### "*What isn't built, will be built at some point.*" - **Somebody**

*Mocha* is a text based operating system built with the **Python** programming language. *Mocha* was created because i felt like it, even though it serves almost
no utilitarian use, besides the fact that it can be used to sort some **Python** applications you may have lying around.

### Although some cool things that *Mocha* can do, is...
* Application Framework and Management
* Organized And Readable Code For Beginners
* Easy To Learn Application Documentation

### Requirements
* Python (Base) - Download [Here](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe).
* Pyfiglet - *command line*: ```pip install pyfiglet```
* OpenAI - *command line*: ```pip install openai```

>The default login credidentials for *Mocha* are\
>**Username**: "admin"\
>**Password**: "password"

# **Application** Documentation
This section of the README will go over *Mocha* application development.

## Setting Up And Mouting Your App
Setting up your application can be done in a few different steps, as a majority of the work is already done for you.

### **Step 1**: Setting Up Basic Details
If you look over to the ```exampleApplication.py``` file, you should find this code inside of it:
```
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
```
This will be the foundation for your app. This *foundation* will hold all of the neccessary information about your app, including it's code.
Inside of the class: ```exampleApplication```, you can change your apps **name, tag, description, and version** respectively. All of this data
will be used when Mocha loads your application onto the homepage. **Create a copy of this file to make your own app.**

>**NOTE**: It's reccomended you change the class name (```exampleApplication```) to your file name, as this will make importing the application easier.

After you've finished setting your name, tag, description, etc to reflect your app, you can finally start coding your app.

>**NOTE**: Your project code will be held inside of the ```{appname}.launch()``` function. This will be called whenever somebody wants to start your app.

### **Step 2**: Mounting Your Application
Mounting your app is also really easy, and can also be done in a few steps. **Head over to the ```_mocha_home.py``` file. You should find something at the top of
the code that looks like this:
```

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
```
This is where you will mount your apps. Under the ```Imported Modules (If Needed)``` will be where you import your file by putting this under the other imports:
```
from apps.{appname} import {appname}

Example:
from apps.myapp import myapp
```
After you've done this, you should be able to fully import your app by adding your app class name into the **Load List**.
```
Example:

loadlist = [
  exampleApplication,
  aiplayground,
  myapp
]
```
Everything located inside of the loadlist will be loaded into *Mocha* home, if it doesn't throw any errors trying to load it.

And boom! You've created and mounted your application. Have fun!

>**NOTE**: Creating an application with intentionally malicious code is **illegal** and can get you into legal trouble. Please don't create
>any harmful programs.

## Application Documentation
This section will go over the various objects and functions created inside of *Mocha* to make app development easier. (*will change as Mocha gets updated*)

### **Class**: "console":
This class handles various functions created for the **terminal**.

#### **Function**: "console.clear()"...
> Clears the output console.
>
> **Example**:
> ```
> print('This text is here...')
> time.sleep(1)
> 
> console.clear()
> 
> print('And now it's gone!')
> ```

#### **Function**: "console.delete_last_line()"...
> Will delete the last printed line.
>
> **Example**:
> ```
> print('Hello, World!')
> print('This text is here...') # ONLY THIS TEXT WILL GET DELETED
> time.sleep(1)
> 
> console.delete_last_line()
> 
> print('And now it's gone!')
> ```

#### **Function**: "console.title(*text*)"...
> Utilizes PyFiglet to create ascii art text using the supplied string.
>
> **Example**:
> ```
> console.title('Bruh')
> ```

#### **Function**: "console.wait(*wait_time*)"...
> Instead of using ```time.sleep(*int*)```, created ```console.wait(*wait_time*)``` purely for convenience.
>
> **Example**:
> ```
> print('Waiting one second...')
> 
> console.wait(1)
> 
> print('Waited one second!')
> ```

### **Class**: "mocha":
This class holds data for **Mocha** itself.

#### **Object (str)**: "mocha.name"...
> Gets the name of *Mocha*, usually "Mocha" but can be changed if it's a different rendition of *Mocha*.

#### **Object (str)**: "mocha.creator"...
> Gets the creator of *Mocha*, wether the creator Rhet0rical, or the repo creator.

#### **Object (bool)**: "mocha.developer_mode"...
> Gets the current setting of developer mode. Developer mode allows for certain applications to show, or certain settings to appear
> in the configuration tool. Usually **True or False**.

### **Subclass**: "mocha.version":
This class holds data for *Mocha*'s version.

#### **Object (str)**: "mocha.version.build_type"...
> Defines the build type of the version of *Mocha* your running. Will show on the bootscreen of *Mocha* too.

#### **Object (str)**: "mocha.version.num"...
> Defines the version number of *Mocha*

#### **Object (str)**: "mocha.version.full_version"...
> Complete version of *Mocha*. Mixes both ```build_type``` and ```num```. Example: ```pre_0.3```

### **Subclass**: "mocha.github":
This class holds data for *Mocha*'s github page.

#### **Object (str)**: "mocha.github.link"...
> Holds the link to the *Mocha* GitHub Repository.

#### **Object (str)**: "mocha.github.version"...
> Fetches the version of *Mocha* currently published on GitHub. Fetches from the ```system/version.txt``` file.

### **Subclass**: "mocha.config":
This holds the configuration settings for *Mocha*.

#### **Object (bool)**: "mocha.config.start_on_run"...
> Decides if the OS will immediately start if the ```main.py``` file is ran. It not, it'll wait for input before starting.

#### **Object (bool)**: "mocha.config.force_user_login"...
> Decides if the OS will force the host to login before using Mocha. If not, the OS will boot to *Mocha* home.

#### **Object (bool)**: "mocha.config.show_ip_on_boot"...
> Decides if the OS will show the IP Address of the host computer on the bootscreen.

#### **Object (bool)**: "mocha.config.show_hostname_on_boot"...
> Decides if the OS will show the hostname of the host computer on the bootscreen.

#### **Object (bool)**: "mocha.config.check_for_updates"...
> Decides if the OS will check for updates while booting.

### **Class**: "client":
This class holds data for the Client/Host.

#### **Object (str)**: "client.platform"...
> Gets the platform the Host is running *Mocha* on.

#### **Object (str)**: "client.ip_address"...
> Gets the IP Address of the Client.

#### **Object (str)**: "client.hostname"...
> Gets the hostname of the Client.
