#What are 'Regular Expressions' and why ae they regular?

#A regular expression, also known as regex or regexp, is essentially a search query for text that's expressed by string pattern. When you run a search against a particular piece of text, anything that matches a regular expression pattern you specified, is returned as a result of the search. 

#Regular expressions let you answer the questions like what are all the four-letter words in a file? Or how many different error types are there in this error log? In other words, regular expressions allow us to search a text for strings matching a specific pattern. 

#For example, if I have a file that lists NFS mounts and options and I want to pull only the server name, I can write a regular expression that strips each line of the excess data and returns only a list of the information I need. 

#Any other ideas? Instead, we could use a regular expression to extract the process ID in a more robust fashion. For that, we're going to import the RE module, which lets us use the search function to find regular expressions inside strings.

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])        #=====> 12345

#This regular expression will work no matter where our process ID shows up or how long or short the line is. As long as there's a single sequence of numbers in the string marked by square brackets, this regex will extract those numbers for us. If the regular expressions stored in the regex variable looks like gibberish at this point, don't worry, that's expected.

#In our last example, we used a pretty complex regular expression from a Python program to look for a process ID. This is just one example of something we might want to do when processing texts from our Python scripts. We can also use regular expressions with a bunch of command line tools. 

#Grep command in linux, Select-String in Windows PowerShell & The findstr command in Windows Command Line are examples of regular expressions related commands in OS oriented scripting languages.

# The simplest of all matchings is just to search to see if the string is present. Remember, that grep works by printing out any line that matches the query that we pass it. So for a simplest query of passing a plain old string, grep will print any lines containing that string in the file that we give it. 

#Let's try this out using grep to find words inside the /usr/share/dict/words.txt file, which is a file that some spell-checking programs use to verify if the word exists or not.

'''
Below are Linux, PowerShell and Command Line commands that work similarly.

grep thon /usr/share/dict/word.txt

Select-String thon D:\MyDev\projects\Python\Google-IT-Automation-Scripts-Python\Google-Using-Python-to-Interact-with-the-Operating-System\words.txt

findstr thon D:\MyDev\projects\Python\Google-IT-Automation-Scripts-Python\Google-Using-Python-to-Interact-with-the-Operating-System\words.txt

'''

#So when we call grep with thon as a pattern to match on and we pass our list of words as a file, we see that it matches with a bunch of different words. These words, all contain the string thon somewhere inside of them, which is why they appear in our results.

#We also see that the output is highlighted for us, showing us the matching part of the line in a different color. This added visual indicator is something that grep does for us so that we can easily see where the match occurred.

#It's worth calling out that the string we're passing in grep is case sensitive.

# If we wanted to match a string regardless of case, we will have to pass the -i parameter to the grep command

'''
grep -i python /usr/share/dict/words.txt
'''

#So we now know that any basic string is already a regular expression which will match a line that contains that string. To get the most out of regular expressions, we need to learn more of their syntax, which can be as complicated as it is powerful.

#In particular, we have to know the reserved characters that give extra meaning to the patterns that we create. It's these characters that allow us to do more advanced matching than just checking for a literal string. For example, a dot matches any character.

#This means that if we include a dot in our expression, that dot is a wildcard that can be replaced by any other character in the results.

'''
grep l.rts /usr/share/dict/words.txt 
'''

'''
Result
================================
alerts
blurts
flirts
'''

#Check out how for each of those words, the dot in our pattern was substituted by different letter.

#Other easy examples of special characters that we can use in a regular expressions are the caret(^), or circumflex and the dollar sign($) anchor characters.

#The circumflex indicates the beginning and the dollar sign indicates the end of the line. 

'''
grep ^fruit /usr/share/dict/words.txt
'''

#For example, to look for all the words that start with a string fruit, we would write grep circumflex fruit in our file.

#We'll use grep to find all the words that end with cat by writing grep cat dollar sign into our file.

'''
grep cat$ /usr/share/dict/words.txt
'''

#One thing to remember is that the circumflex and the dollar sign specifically match the start and end of the line, not a string. 

#Take a log file for example, where each line contains a lot of different words. We can use a circumflex to check if a line begins with a pattern or use a dollar sign and check if it ends with a pattern, but our patterns will match only if the line fits that criteria, not the contained words.




