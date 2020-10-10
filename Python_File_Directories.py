#You might need to process all the files that are in a specific directory or generate a directory with the results of your data analysis. As with files, Python provides a bunch of different functions that let us create, delete and browse the contents of directories.

#You might remember when we talked about the current working directory and how important it is to know this when using a relative path to determine the location of a file. 

#To check which current directory your Python program is executing in, you can use the getcwd method. If you use a unix-like system, you might remember that the name of the command that prints the working directory is called pwd.

import os

print(os.getcwd())  #=====> D:\MyDev\projects\Python\Google-IT-Automation-Scripts-Python\Google-Using-Python-to-Interact-with-the-Operating-System

#In this case, the current directory is our user's home directory which is a default directory where we have stored our exercise files.

#To create a directory, we use the mkdir function. This function has the same name as both the Windows and Linux commands that do the same exact thing.

if os.path.exists("new_dir"):
    os.rmdir("new_dir") 

else:
    os.mkdir("new_dir")

#So we've just created a directory called newdir and it's located in the current working directory. You can also change directories in your program by using the chdir function and passing the directory you'd like to change to as a parameter. 

#Just like the other functions we've seen, we can use relative or absolute paths to do that.

#check the existence of the directory.
import os

os.path.exists("new_dir") 
os.chdir("new_dir")
print(os.getcwd())  #=====> D:\MyDev\projects\Python\Google-IT-Automation-Scripts-Python\Google-Using-Python-to-Interact-with-the-Operating-System\new_dir

#As you can see, we've changed the current working directory to the new directory that we created inside of the user's home directory. We use mkdir to create directories and we can use our rmdir to remove them like this.

os.mkdir("Newer_dir")
os.rmdir("Newer_dir")   #This rmdir() only works when the directory is empty.

#If we try to remove a directory that has files in it, we get an error. We need to first delete all the files and sub-directories in that directory before we can actually remove it but how can we find out what contents are in that directory?

#Well, there are a few techniques that we can use to do this. The os.listdir function returns a list of all the files and sub-directories in a given directory. Let's see how this looks for our website directory. '''

import os

#Going back to the previous folder.
os.chdir("D:\MyDev\projects\Python\Google-IT-Automation-Scripts-Python\Google-Using-Python-to-Interact-with-the-Operating-System")

#Displaying the current path of the working directory
print(os.getcwd())

#Displaying the content of a given directory.
print(os.listdir("website"))

'''
['images', 'index.html', 'pages', 'README.txt', 'scripts', 'styles']
'''

#So we've got a list of strings. Since they're just strings, we don't know if they're directories or files. To find out what they are, we can use functions like os.path.isdir but before we look at how that works.

#See how the list contains just file names. If we want to know whether one of these files is a directory, we need to use os.path.join to create the full path. Let's see all of this in action now.

dir = "website"
for name in os.listdir(dir): 
    fullname = os.path.join(dir, name) 
    if os.path.isdir(fullname): 
        print("{} is a directory".format(fullname))
    else: 
        print("{} is a directory".format(fullname))
        
'''
website\images is a directory
website\index.html is a directory
website\pages is a directory
website\README.txt is a directory
website\scripts is a directory
website\styles is a directory
'''

#This code is doing a bunch of interesting stuff but let's go through it step-by-step. 

#First, we're defining a dir variable with the name of the directory that we want to check. This makes our code more readable and more usable. 

#Then we're iterating through the file names returned by the os.listdir. We know from our previous execution of this function that these are just the names of the files without directory. So using os.path.

#join, we join the directory to each of those file names and create a String with a valid full name. 

#Finally, we use that full name to call os.path.isdir to check if it's a directory or a file. Maybe you're wondering what's up with that join function? 

#It seems to just add a slash between two strings. Well, the join function let's us be independent from the operating system again. 

#In Linux and MacOS, the portions of a file are split using a forward slash. On Windows, they're split using a backslash. By using the os.path.

#join function instead of explicitly adding a slash, we can make sure that our scripts work with all operating systems. It's another one of those handy little tools that help us avoid errors when working on different platforms.

