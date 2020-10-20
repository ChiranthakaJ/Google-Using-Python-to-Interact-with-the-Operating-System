#We've seen by now how we can use a dot in our regular expressions as a special character that can match any character. In the regex world, this is known as a wildcard because it can match more than one character. 

#Using a dot is the broadest possible wildcard because it matches absolutely any character. But what if we wanted something stricter, like checking if an answer given by a user contains a valid character, or finding all the usernames in a CSV file that start with a vowel? 

#We have to restrict our wildcards to a range of characters to do this. For this task we use another feature of regexes called character classes. Character classes are written inside square brackets and let us list the characters we want to match inside of those brackets. 

#For example, say we want to match the word Python but allow for both lowercase or uppercase p. We could do it like this.
import re

print(re.search(r"[Pp]ython", "Python"))        #=====> <re.Match object; span=(0, 6), match='Python'>

#Inside the square brackets, we can also define a range of characters using a dash. For example, we could use lowercase a to lowercase z to state any lowercase letter. 

# So if we wanted to look for the string way preceded by any letter, we could write the expression like this one.

print(re.search(r"[a-z]way", "The end of the highway"))     #=====> <re.Match object; span=(18, 22), match='hway'>

#The character class defined was matched by the letter H. Let's try a different string.

print(re.search(r"[a-z]way", "What a way to go"))   #=====> None

#In this case, we didn't get a match. That's because the string way is preceded by a space and that doesn't match the range that we defined. 

#We can define more ranges like upper case A to upper case Z for all upper case letters or 0 to 9 for all digits. We can combine as many ranges and symbols as we want, like this.

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))      #=====> <re.Match object; span=(0, 6), match='cloudy'>

print(re.search("cloud[a-zA-Z0-9]", "cloud9"))      #=====> <re.Match object; span=(0, 6), match='cloud9'>

#So as you can see, we can match anything that's defined between the square brackets. It's pretty cool, right? 

#Example 01 - Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.

import re
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
 
 
#Well, this is super useful. 

#Sometimes we may want to match any characters that aren't in a group. To do that, we use a circumflex inside the square brackets. 

#For example, let's create a search pattern that looks for any characters that's not a letter.

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))     #=====> <re.Match object; span=(4, 5), match=' '>

#Here, our pattern matched the first space in the sentence. What if we also add a space to the list of characters that we don't want to match?

print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))   #=====> <re.Match object; span=(29, 30), match='.'>

#You might have guessed this. Because we added a space inside the character class, our example now matched the final dot in the sentence, which isn't in the list of characters to exclude. 

#If we want to match either one expression or another, we can use the pipe symbol to do that. 

#This lets us list alternative options that can get matched. For example, we could have an expression that matches either the word cat or the word dog, like this.

print(re.search(r"cat|dog", "I like dogs."))        #=====> <re.Match object; span=(7, 10), match='dog'>

#So since the string contains the sub string dog, the search function could find it. Let's try an example with cat.

print(re.search(r"cat|dog", "I like cats."))        #=====> <re.Match object; span=(7, 10), match='cat'>

#In this string, we actually have two possible matches for our search. 

print(re.search(r"cat|dog", "I like cats and dogs."))  #=====> <re.Match object; span=(7, 10), match='cat'>

#But we only get the first one. That's the way the search function works. If we want to get all possible matches, we can do that using the findall function, which is also provided by the re module, like this.

print(re.findall(r"cat|dog", "I like cats and dogs."))  #=====> ['cat', 'dog']

#So with findall, we don't need to choose between cats and dogs. 






