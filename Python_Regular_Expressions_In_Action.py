#Armed with all this knowledge, we can start combining these special characters to create patterns to match the text that we want. 

#For example, say you had a list of all the countries in the world and you want to check which of those names start and end in a. 

#What will the pattern look like? Maybe something like this, A.*a. Let's try that one out.

import re

print(re.search(r"A.*a", "Argentina"))      #=====> <re.Match object; span=(0, 9), match='Argentina'>

#Awesome. Seems like that works. Let's try it with different country. Azerbaijan.

print(re.search(r"A.*a", "Azerbaijan"))     #=====> <re.Match object; span=(0, 9), match='Azerbaija'>

#Surprising maybe, this happened because we didn't specify that we wanted our patterns match the whole string. So while Azerbaijan doesn't finish with A, it does have an A in its name. So it matches our pattern. 

#We need to make our patterns stricter by adding the beginning of a line and end of a line characters.

print(re.search(r"^A.*a$", "Azerbaijan"))   #=====> None

#By adding a dollar sign to our pattern, we've made it clear that we only want to match lines that begin and end with the letter a. So Azerbaijan doesn't match anymore. 

#Let's check that it still works for a country that should match like Australia.

print(re.search(r"^A.*a$", "Australia"))    #=====> <re.Match object; span=(0, 9), match='Australia'>

#Using regular expressions, we can also construct a pattern that would validate if the string is a valid variable name in Python. 
 
#Do you remember what the rules were? It can contain any number of letters numbers or underscores, but it can't start with a number. 

#So what do you think the validating pattern would look like?

#We said it needs to start with a letter. So we'll start with circumflex to indicate that we wanted to start from the beginning, and now a character class with all lowercase and uppercase letters plus the underscore.

#The rest of the variable can have as many numbers letters or underscores that we want. So we needed another character class this time containing numbers with a star at the end.

#Okay, we're almost done. You definitely deserve a star at the end of this. One last thing, we want this to be the end of the string that we're matching. Otherwise, we could match something that could be a variable, but that also contains additional stuff after it. So we finish up with a dollar sign.

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable_name"))     #=====> <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>

#That's right, we can use underscores anywhere in the string, that's a valid variable name. It matches our validation pattern because we included underscores in it. 

#Let's try something a little different.

print(re.search(pattern, "this isn't a valid variable name"))   #=====> None

#Once we use a space, it stops being a valid variable name. It doesn't matter pattern because spaces aren't included in the possible characters. Let's check out a variable with a number.

print(re.search(pattern, "my_variable1"))   #=====> <re.Match object; span=(0, 12), match='my_variable1'>

#Sure enough, we can use numbers inside the variable name. Our pattern includes all numbers as part of the variable, but what have we start with a number.

print(re.search(pattern, "2my_variable1"))   #=====> None

#The variable the number at the beginning isn't a valid variable name. In our pattern doesn't match it because the first of two character classes doesn't include numbers. 


#Example 01 - Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.

import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z]*(\s[a-z]+)*[\.!\?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


#Example 02 - The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.

import re
def check_web_address(text):
  pattern = r"^\S+\.[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


#Example 03 - The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?

import re
def check_time(text):
  pattern = r"^[1-9][0-2]?:[0-5][0-9] ?[am|pm|AM|PM]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


#Example 04 - The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function:

import re
def contains_acronym(text):
  pattern = r"\([A-Z1-9][a-zA-Z1-9]*\)" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


#Example 05 - Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, and cannot be at the start of the text.

import re
def check_zip_code (text):
  result = re.search(r"[ ]\d{5}|[ ]\d{5}-\d{4}", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False