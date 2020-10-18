#Let's have a look at the below example.

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

regex = r"\[(\d+)\]"

result = re.search(regex, log)

print(result[1])        #=====> 12345

#The first character of the pattern is the backslash, which is used as the escape character. This means that the next character, which is a square bracket here, is treated literally for matching purposes. 

#After the square bracket, comes the first parentheses. Since it isn't escaped, we know it'll be used as a capturing group. The capturing group parentheses are wrapping the backslash d+ symbols. 

#From our discussion of special characters and repetition qualifiers, we know that this expression will match one or more numerical characters. 

#After the closing parentheses of the capturing group, we have the closing square bracket symbol, also proceeded by the escape character. 
 
#After calling the search function, we know that because we're capturing groups in an expression, we can access the matching data by accessing the value at index 1. Let's try our expression on a different string and check that it really works, no matter what the rest of the text is.

result = re.search(regex, "A completely different string that also has numbers [34567]")

print(result[1])        #=====> 34567

#Okay, this looks fine. But what if our string didn't actually have a block of numbers between the square brackets?

result = re.search(regex, "99 elephants in a [cage]")

#print(result[1]) - Please be vigilant to uncomment this line of code in order to 

'''
Traceback (most recent call last):
  File "d:\MyDev\projects\Python\Google-IT-Automation-Scripts-Python\Google-Using-Python-to-Interact-with-the-Operating-System\Python_Regular_Expressions_Extracting_PID.py", line 30, in <module>
    print(result[1])
TypeError: 'NoneType' object is not subscriptable
'''

#The above error was given because, we tried to access the index 1 of a variable that was none. 

#As Python tells us, this isn't something that we can do. So what should we do instead? 

#We should have a function that extracts the process ID or PID when possible, and does something else if not. It's something like this; will start by defining a function called extract_pid.

def extract_pid(log_line): 
    
    #Now, we'll use the same RegEx as before, and we'll store the result of the search function in a result value, just like this.
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)   
    if result is None: 
            return ""
    return result[1]

#We can now test our function with the original log line to check that it still does the right thing.
print(extract_pid(log))     #=====> 12345

#Nice, let's wrap this up by trying it out with a string that broke our code before.
print(extract_pid("99 elephants in a [cage]"))      #=====> No result(empty)

#Great. It didn't match so return an empty string. That's exactly what we wanted. All right. We now have a function that lets us correctly extract PIDs from log lines without it breaking other lines.

#Example 01 - Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.

import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]\: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
