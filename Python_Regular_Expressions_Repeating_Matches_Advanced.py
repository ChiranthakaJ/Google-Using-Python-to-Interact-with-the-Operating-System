#There are no of advanced features in 'Repetition Qualifiers'. Let's have a look at them in the below.

#Up to now, we've used the Star, Plus and question mark repetition qualifiers. What if we wanted a pattern that repeats a specific number of times? 

#This could happen if we're processing a line that we know has some specific data in a column, or we know that we want a string of a specific length. 

#In cases like those, we would manually write the same pattern as many times as we need it. But it would be hard to read and hard to maintain. And that's why Python also offers numeric repetition qualifiers. 

#These are written between curly brackets and can be one or two numbers specifying a range. For example, to match any string of exactly five letters, we can use an expression like this one.

import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))     #=====>  <re.Match object; span=(2, 7), match='ghost'>

#Remember, that the expression will match whichever part of the given string that fits the criteria. In this case, we're looking for letters that are repeated five times, and ghost has five letters, so it matched our pattern.

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))  #=====> <re.Match object; span=(2, 7), match='scary'>

#In this string, we actually have more matches for our search, but we only get the first one. Remember, what we can do to find more matches? That's right, use the findall() function, like this.

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) #=====> ['scary', 'ghost', 'appea']

#Now we have an extra match for the word that's actually longer. What if we wanted to match all the words that are exactly five letters long? We can do that using \b, which matches word limits at the beginning and end of the pattern, to indicate that we want full words, like this

print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")) #=====> ['scary', 'ghost']

#We said that we can also have two numbers in the range. For example, if we wanted to match a range of five to ten letters or numbers, we could use an expression like this one.

print(re.findall(r"\w{5,10}", "I really like strawberries"))    #=====> ['really', 'strawberri']

#These ranges can also be open ended. A number followed by a comma means at least that many repetitions with no upper boundary limited only by the maximum repetitions in the source text.

print(re.findall(r"\w{5,}", "I really like strawberries"))  #=====> ['really', 'strawberries']

#Okay, that looks good. Pulse check, hopefully, Python isn't spooking you and you're berry much enjoying learning it. Wow, what is it about teaching Python that makes me break out these cheesy jokes? I can't help myself. 

#Now, for our final example, a comma followed by a number means from zero up to that amount of repetitions. Let's check that one out.

print(re.findall(r"s\w{,20}", "I really like strawberries"))    #=====> ['strawberries']

#Here we look for a pattern that was an S followed by up to 20 alphanumeric characters. So we got a match for strawberries which starts with S, and is followed by 11 characters.

#Example 01 - The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.

import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []


