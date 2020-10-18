#So far we've looked at how to match one specific character, a group of characters or even any character. 

#For repeating matched we use 'Repetition Qualifiers'.

#Now we're going check out how to match these characters several times. 

#So we wanted to find the longest word in the string, or we wanted to find the host names in a log file by checking for a bunch of alphanumeric characters between brackets. 

#We can do this using another interesting RegEx concept, repeated matches. It's quite common to see expressions that include a dot followed by a star. 

# This means that it matches any character repeated as many times as possible including zero. Lets see some examples below.

import re

print(re.search(r"Py.*n", "Pygmalion"))     #=====> <re.Match object; span=(0, 9), match='Pygmalion'>

#In plain English, you could read this RegEx as match pi followed by any number of other characters followed by n. But with our dot star combination we expanded the range of the match to the whole word. 

#See how the dot takes a different value for each letter? Let's try a different string, 'Python programming'.

print(re.search(r"Py.*n", "Python Programming"))    #=====> <re.Match object; span=(0, 17), match='Python Programmin'>

#You might not have been expecting that. Remember, the Star takes as many characters as possible. 

#In programming terms, we say that this behavior is greedy. It's possible to modify the repetition qualifiers to make them less greedy. 

#But we won't get into that now. To learn more about that, check out the next reading. But back to our example. 

#While our pattern could have matched the word Python, it expanded all the way until the last n in the string. 

#If we only wanted our patterns match letters, we should have used the character class instead like this.

print(re.search(r"Py[a-z]*n", "Python Programming"))    #======> <re.Match object; span=(0, 6), match='Python'>

#Remember how we said that zero times is also a possibility? That will let the string 'Pyn' also match our pattern. 

print(re.search(r"Py[a-z]*n", "Pyn"))       #=====> <re.Match object; span=(0, 3), match='Pyn'>

#As we called out earlier, implementations of regular expressions aren't always the same. 

#Repetition qualifiers are one way they differ. Some implementations like the one used by grep only include the store qualifier that we just discussed.

#You can do a lot with just a star qualifier. So that's usually good enough. 

#Other implementations like the one used by Python or by the Egrep command include two additional repetition qualifiers plus and question mark, that can help us construct more complex expressions.

#Let's check that out. The plus character matches one or more occurrences of the character that comes before it. So we had the pattern O plus L plus. Let's check it against a few words.

print(re.search(r"o+l+", "goldfish"))       #=====> <re.Match object; span=(1, 3), match='ol'>

#In this case, there was one occurrence of each. In the match pattern shows us the shortest possible matching string. Here, there were two of each.

print(re.search(r"o+l+", "woolly"))     #=====> <re.Match object; span=(1, 5), match='ooll'>

#Again, we can see the match is a whole string that matches the condition. 
 
#Let's try something that doesn't match.

print(re.search(r"o+l+", "boil"))       #=====> None


#Example 01 - The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False.

import re
def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

#The question mark symbol is yet another multiplier. It means either zero or one occurrence of the character before it. Let's see how it works in the below.

print(re.search(r"p?each", "To each their own"))        #=====> <re.Match object; span=(3, 7), match='each'>

#The P wasn't present but with the question mark we marked it as optional. So we still got a match. Let's see what happens when the P is present.

print(re.search(r"p?each", "I like peaches"))       #=====> <re.Match object; span=(7, 12), match='peach'>

#Great the P was president and so match included it. 







