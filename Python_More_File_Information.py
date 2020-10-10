#We can get a lot more info about our files using functions in OS.path module. For example, to check how big a file is, we can use the getsize function which returns the file size in bytes.

import os.path

file_size = os.path.getsize("Spider.txt")

print(file_size)

#To check when the file was last modified, the getmtime function comes in really handy. Let's check out how this works.

date_created = os.path.getatime("spider.txt")  

print(date_created)  #=====>    1602343127.5123258

#t doesn't look like time, does it? That's because it's a timestamp. In this case specifically, it's a Unix timestamp. It represents the number of seconds since January 1st, 1970.

#Seems a bit random, but there's actually a really good reason behind this date. This was adopted years ago to store the times associated to files in computers. 

#Since that's when they started publishing Unix operating systems, Unix uses that date because there couldn't be any file created before that time.

#While Unix timestamps have a 50-year history, they're still very much present today. They're used by file systems to show when a file was created, accessed, or modified. They are also used in other systems like databases.

#We can use the datetime module to make it easier for us humans to read, like this.

import datetime

date_created = os.path.getmtime("Spider.txt")
readable_date = datetime.datetime.fromtimestamp(date_created)

print(readable_date)        #=====> 2020-10-10 20:48:47.522331


#Example 02

import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))


#Example 03 - Another cool feature of the functions is that we can work with both relative and absolute paths. In our examples, we've been using the relative file names without having to specify their full paths. In some cases, we may need to specify exactly where the file is to work with it in our script. This is where the abspath function can help.  

print(os.path.abspath("Spider.txt"))    #=====> D:\MyDev\projects\Python\Google-IT-Automation-Scripts-Python\Google-Using-Python-to-Interact-with-the-Operating-System\Spider.txt


    


