#In the last video, we wrote a script that processed a log file and extracted the names of each user who had started a cron job in the machine that we were investigating. 

#This can be really helpful but there's more information that we might need. To improve our output, it would be a good idea to have a count of how many times each username appears in our log. Can you think of what we can use to do that? If you guess a dictionary, then you're right. 

#As we've seen in earlier examples, dictionaries are great structure to use when we want to count appearances of strings. We'll store the user name as a keys of a dictionary and we'll use the value to count the number of times that each user name appears in the file. 

#To do this in fewer lines, we'll use the get method that we saw earlier in another video. Let's try it out in the interpreter before adding it to our code. First, we'll create an empty dictionary using curly brackets.

usernames = {}

#Then we'll set the variable name as good user, for example.

name = "good_user"

#And now, we'll set the value associated with the key as one more than the current value, and we'll use the get method to get the current value, like this.

usernames[name] = usernames.get(name, 0) + 1

#Again, we're taking the current value in the dictionary by passing a default value of zero, so that when the key is in present in the dictionary, we had a default value. We then add one and set it as a new value associated with that key. Let's check out the current contents of the dictionary.

#print(usernames)        #=====> {'good_user': 1}

#Great, and what happens if we do the same operation again?
usernames[name] = usernames.get(name, 0) + 1
#print(usernames)        #=====> {'good_user': 2}

#Fantastic. We see that this operation works successfully both when the key is already in the dictionary and when it isn't. Now, let's add this to our script. We'll need to initialize the empty dictionary at the beginning of our code. 

import re
import sys

logfile = sys.argv[0]
username = {} 
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            # continue keyword tells the loop to go to the next element
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        
        ##And before we add any values to the dictionary, we want to check that we actually got a match to our regular expression. Do you remember how we can do that? We can check if the result variable is none. We'll use that same technique as before, and use the continue keyword if the result is none.
        
        if result is None: 
            continue
        
        #print(result)       #=====> NoneType
    
        #Okay, we can now add the values to the dictionary as we process the file instead of printing them. To do that, we'll define a name variable that will store the captured group. And then we'll use that one as a key for our dictionary.
    
        
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
        #print(result) 
        
#And finally, let's print the results in dictionary once we're done going through the file.
#print(usernames)      

#The complete solution is as the below.

import re
import sys

logfile = sys.argv[0]
username = {} 
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None: 
            continue
        name = result[2]
        usernames[name] = usernames.get(name, 0) + 1

print(usernames)      #=====> {'good_user': 2}

#Cool, our script now allows us to very quickly see who's been starting cron jobs in the server and at what frequency. Now we can use the information to investigate the issue more deeply. It's pretty cool to see how all these different ways of managing data and processes come together in a real world example, isn't it? Nice job. 

