#Up to now, we've used the search function to check if a string matched a certain pattern. But the only thing we've done with the result is print. Printing is useful when we want to see if a string matches a certain pattern. 

#But most of the time, we want to take the information that we matched and use it for something else. 

#For example, we may want to extract the hostname or a process ID from a log line and use that value for another operation. For that we need to use a concept of regular expressions called capturing groups. Capturing groups are portions of the pattern that are enclosed in parentheses. 

#Let's say that we have a list of people's full names. These names are stored as last name, comma, first name. We want to turn this around and create a string that starts with the first name followed by the last name. We can do this using a regular expression with capturing groups. 

#Let's see how this works. First we'll create a matching pattern that matches a group of letters followed by a comma, a space, and then another group of letters. To capture our groups, we'll put each group of letters between parentheses like this.

import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)       #=====> <re.Match object; span=(0, 13), match='Lovelace, Ada'>

#Great, we have a match. Remember that \w will match letters, numbers, and underscores. The match object has more attributes and methods than the ones shown by print, so we are going to start using them now. 

#Let's look at the output of the groups method.
print(result.groups())      #=====> ('Lovelace', 'Ada')

#Because we defined two separate groups, the group method returns a tuple of two elements. We can also use indexing to access these groups. The first element contains the text matched by the entire regular expression. 

#Each successive element contains the data that was matched by every subsequent match group. So let's look at the element at index 0.

print(result[0])        #=====> Lovelace, Ada

#That's the whole string. Now, the following index is correspond to each of the captured groups. Let's check this out.

print(result[1])        #=====> Lovelace

print(result[2])        #=====> Ada

#So we can construct the name that we want by using these indexes.

print("{} {}".format(result[2], result[1]))     #=====> Ada Lovelace

    
#Okay, so now that we've got this more or less working, let's put this into a function that would do the rearranging for us. We'll start by defining a function called rearrange_name, that receives a name by parameter.

def rearrange_name(name):
    
    #Now, we'll search string with the same pattern that we saw before.
    result = re.search(r"^(\w*), (\w*)$", name)
    
    #If the result is none, it means it didn't match the format that we were expecting. So in that case, it would just return the name as it is.
    if result is None: 
        
        #Okay, if we're here then our pattern matched and our result variable will have two capture groups. One for the characters before the comma and another for the characters after the comma.
        return name
    
    #Let's return the rearrange version of that string.
    
    return "{} {}".format(result[2], result[1])

#Nice, we've defined our function, let's test it out with a few names. Please note that in here we have to use the print() in order to see the result in the Python console. Otherwise we won't be able to see the result. If we use PyCharm/Windows CMD/Microsoft Powershell or similar CLI console tool, we don't want to use the print().

print(rearrange_name("Lovelace, Ada"))      #=====> Ada Lovelace

print(rearrange_name("Ritchie, Dennis"))    #=====> Dennis Ritchie

#Cool, this seems to be working. But what if we give it something a little bit more challenging?

print(rearrange_name("Hopper, Grace M."))

#Now, the regular expression didn't match because we used the \w character, which only matches letters. And so it didn't recognize the middle initial as part of the given name. Can you figure out how to fix it? 

#Example 01 - Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames.

import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w.*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

'''
John F. Kennedy
'''

#What we need to do here is add the extra characters that we want to allow in the names. In this example we'd want to add spaces and dots. For other names we can also include dashes. So after updating our pattern, this is what our function would look like.

import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Hopper, Grace M.")
print(name)

'''
Grace M. Hopper
'''

#So as you can see, by adding extra characters between square brackets we rearranged a name that was a little more complex. I bet you can come up with some more examples for using capturing groups. 

