#When working with log files and scripts, our first step is usually to open them so our code can access their contents. We've discussed various methods of operating on files. 

#The usual technique is to call the open function which returns a file object and then iterate through each of its lines using a for-loop. For example, to open a file received as a parameter of our script, we can use code like this one. 

#Remember that for performance reasons, when files are large, it's generally a good practice to read them line by line instead of loading the entire contents into memory. For our example, let's say the log file contains these messages.

import re
import sys

logfile = sys.argv[0]
with open(logfile) as f: 
    for line in f: 
        print(line.strip())
        

#The server that generates this log file has been acting strangely and we suspect it's due to a Cron job started by one of the system administrators. You may remember that Cron jobs are used to schedule scripts on UNIX-based operating systems. 

#To find out what's happening with the server, we want to audit the log files and see exactly who's been launching CRON jobs. By looking at the sample log, we can see that the lines that'll be most interesting to us are the ones that contain the Cron substring. 

#These lines also show the user who started the Cron job wrapped in parentheses. With this info, we can ignore any line without the Cron substring in it. We can check for this using the "in" keyword.

import re
import sys

logfile = sys.argv[0]
with open(logfile) as f: 
    for line in f: 
        if "CRON" not in line:  #Checking using the in keyword.
            continue
        print(line.strip())
        

#Here, we're using the "continue" keyword which tells our loop to go to the next element. So if the line doesn't contain a string that we're looking for, we'll skip it and go to the next line. 

#Once we know we're processing to write log line, we can use our knowledge of regular expressions to extract the username. We can do this in a bunch of different ways. 
 
#In this example, we'll use escape characters, capture groups, and the end of string anchor. Before we add the expression to our script, we'll construct it and test it out in an interpreter.

'''
The Regular expression mentioned is as the below.

import regularpattern - r"USER \((\w+)\)$"
'''

#Let's take a closer look at this expression. Since the username is found at the end log line, we use the dollar sign anchor to only match texts that is at the end of the line. 

#To find the username, we look for the word user followed by a string wrapped in parentheses as that's how these lines are structured. This means that we need to escape those parentheses with a backslash. 

#Since we want to extract the actual username, we use another couple of parentheses to create a capturing group. For the username itself, we're matching any alphanumeric characters by using backslash w plus. With that cleared out, let's test it out with a sample line.

'''
line = "Oct 21 16:04:32 computer.name CRON[29440]: USER (moron_user)"
result = re.search(pattern, line)
print(result[1])        #=====> moron_user
'''

#Looks like you've got a moron_user. On the plus side, it seems our regular expression works correctly. We can now use expression in our code. Let's add it to our script. The complete script is as at the below.

import re
import sys

logfile = sys.argv[0]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            # continue keyword tells the loop to go to the next element
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result)
        
        
#Example 01 - We're using the same syslog, and we want to display the date, time, and process id that's inside the square brackets. We can read each line of the syslog and pass the contents to the show_time_of_pid function. Fill in the gaps to extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.

import re
def show_time_of_pid(line):
  pattern = r'^(\w+ [0-9] [0-9]+:[0-9]+:[0-9]+) [\w\.]+ [\w=]+\[([0-9]+)\]'
  result = re.search(pattern, line)
  return "{} pid:{} ".format(result[1], result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440