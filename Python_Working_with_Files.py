#We may need to delete, rename or move files, or we might need information about a file, like the time it was last modified or its current size.
 
#Let's explore some of the many things that we can do with files in Python. For these operations, we'll be using functions provided by the OS module. 

#This module provides a layer of abstraction between Python and the operating system. It allows us to interact with the underlying system without us knowing whether we're working on a Windows, Mac, Linux, or any other operating system supported by Python. 

#This means that you can write and test a script on one operating system like Windows and then run it on a different operating system like Linux. 

#Paths can be different across different operating systems. So, whenever we're using an absolute path in our code, we need to make sure we can provide alternatives for the platforms we want to support.

#Let's have a look at this example.

#Example 01 - Using the remove() to remove a file from the OS file system.

import os

with open("novel.txt","w") as file: 
      new_text = file.write("New content V2")
      
print("File existence: " + str(os.path.exists("novel.txt")))    #With the exists() method in path sub module within the OS module.

'''
File existence: True
'''

os.remove("novel.txt")      #We can use the remove() function to remove an existinf file.
print("File existence: " + str(os.path.exists("novel.txt"))) 

'''
File existence: False
'''




