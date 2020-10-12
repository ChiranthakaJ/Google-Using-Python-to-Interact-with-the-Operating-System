#As we called it out before, we use the re module to apply regular expressions in Python. This module includes a bunch of different functions that can help manipulate strings. Let's see how we can use this module for some basic matching.

import re 
result = re.search(r"aza", "plaza")

#We call the search function on the re module, and told it to use the pattern aza on the string plaza. We then stored the return value of that function in the result variable. The r at the beginning of the pattern indicates that this is a rawstring. 

#This means that Python interpreter shouldn't try to interpret any special characters, and instead, should just pass the string to the function as is. In this example, there are no special characters. The rawstring and the normal string are exactly the same, but it's a good idea to always use rawstrings for regular expressions in Python. 

print(result)     #=====> <re.Match object; span=(2, 5), match='aza'>

#Our result is a match object. The output we get when calling print already shows some interesting information, like the position in the string that matched ,and what the actual matching string was. Let's try this out again with different word.

result = re.search(r"aza", "bazaar")
print(result)     #=====> <re.Match object; span=(1, 4), match='aza'>

#In this case, we can see that the span attribute is different. That's because the match sub-string is in a different position inside the string. The match sub-string is still same though, because we're matching with a plane string. No special syntax yet.

#What do you think will happen if we pass a string that doesn't match the expression? Let's try and find out.

result = re.search(r"aza", "maze")
print(result)    #=====> None

# If the expression doesn't match the string that we pass, we get none as a result. Remember, none is a special value that Python uses that show that there's none actual value there.

#Let's practice the special characters that we've seen up until now with a few examples.

print(re.search(r"^x", "xenon"))      #=====> <re.Match object; span=(0, 1), match='x'>

#We can see that it matched at the beginning of the line on our X as we expected. 

#What happens if we use a dot which can match any character?

print(re.search(r"p.ng", "penguin"))  #=====> <re.Match object; span=(0, 4), match='peng'>

#Now we're using p.ng as a search pattern. It matches the word penguin that we're passing. In the match object ,we see the matching string is peng.

#Let's try it out with a couple other strings.

print(re.search(r"p.ng", "sponge"))   #=====> <re.Match object; span=(1, 5), match='pong'>

#Nice. Here we can see the match attribute always has a value of the actual sub string that match the search pattern. The span attribute, indicates the range where the sub string can be found in the string we passed. 

#We can also pass additional options to the search function. For example, if we want our match to be case insensitive, we can do this by passing the re.IGNORECASE option.

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))   #=====> <re.Match object; span=(0, 4), match='Pang'>

#Example 01 - Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.

import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

'''
True
False
True
'''
