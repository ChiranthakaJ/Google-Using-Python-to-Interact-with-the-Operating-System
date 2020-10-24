#When we open a terminal application on a Linux computer, whether it's local or a remote machine, the application that reads and executes all commands is called a shell.

#A shell is a command line interface used to interact with your operating system. The most commonly used shell on Linux is called Bash. Other popular shells are Zsh and Fish, while they operate in similar ways, for this and upcoming videos, when we talk about the Linux shell, we mean Bash. 

#Our Python programs get executed inside a shell command-line environment. The variable set in that environment which are called you guessed it environment variables are another source of information that we can use in our scripts. 

#Understanding and being able to change environment variables can be really useful to quickly alter a program's behavior. Usually, we can do this by just making some minor changes in the environment the programs are running in. From a command line prompt, we can check these variables using the env or nth command. 

#Display all environment variables names.
#=======================================================================

#Linux-Bash command: $ env
#PowerShell command: Get-Childitem -path env:
#Windows Command Prompt: set

#Wow, that's a lot of different variables, but what are they for? It all depends on the variable itself. Some are more important than others. For example, the path variable is a very important one. Let's print out the contents of just that one using the echo command.

#Display the content of a specific environment variable
#=============================================================================

#Linux Bash command: $ echo $variablename
#PowerShell command: Get-Childitem env:variablename
#Windows Command Prompt: echo %ENVIRONMENT_VARIABLE%

#The shell uses this environment variable to figure out where to look for executable files, and we call them while specifying a directory. All those directories listed there are where the shell will look for programs. 

#For example, when we call the Python 3 program, the shell checks each of the directories listed in the path variable in order, and when it finds a program called Python 3, it executes it. So as we said, we can read the contents of these variables from Python. Let's use a Python script to check that out.

#Example 01 
#------------------------------------------------------------------------------

import os

#Linux version
#------------------------------------------------------------------------------
'''
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
# export FRUIT=Pineapple
print("FRUIT: " + os.environ.get("FRUIT", ""))
'''

#Windows version
#------------------------------------------------------------------------------

print("HOMEPATH: " + os.environ.get("HOMEPATH", ""))
print("USERPROFILE: " + os.environ.get("USERPROFILE", ""))
# export FRUIT=Pineapple    $env:FRUIT = "Pineapple"
print("FRUIT: " + os.environ.get("FRUIT", ""))

#So to access environment variables, we use the Environ dictionary provided by the OS module. In this case, we're using a dictionary method that we haven't used before. The getMethod is a bit similar to how we've been accessing dictionary values up until now. 

#The difference is what happens when the value isn't present. When we retrieve a value from a dictionary using the key as in OS.environ[fruit] and the key isn't present, we get an error. 

#If we use a getMethod instead, we can specify what value should be returned if the key isn't present. In other words, the getMethod allows us to specify a default value when the key that we're looking for isn't in the dictionary. 

#So what we're asking Python to do is try to retrieve the value associated with the key, but if the key's not defined return an empty string instead. We're doing this for three different variables; home, shell, and fruit. Let's run the script and see what happens.

#HOMEPATH: \Users\Chiranthaka
#USERPROFILE: C:\Users\Chiranthaka
#FRUIT:


#We got the values for home and shell, but not for fruit. Well, that's because that variable isn't defined in the current environment. To define it in a way that our script we'll be able to see it, we need to run this in our command-line.

#Setting an environment variable vale.
#================================================================

#Linux Bash command: $ export FRUIT=Mango
#PowerShell command: $env:FRUIT = "Mango"