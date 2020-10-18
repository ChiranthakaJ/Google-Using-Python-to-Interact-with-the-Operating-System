#p to now we've been using two functions from the RE module: search() and findall(). There are actually a few more functions that can be really handy depending on what we're trying to do. One of these functions is called split(). 

#It works similarly to the split function that we used before with strings. But instead of taking a string as a separator, you can take any regular expression as a separator. 

#For example we may want to split a piece of text into separate sentences. To do that we need to check not only for the dots but also for question marks or exclamation marks since they're also valid sentence endings. It's something like this.
import re 

print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

'''
['One sentence', ' Another one', ' And the last one', '']
'''

#Check out how we are not escaping the characters that we wrote inside the square brackets. 

#That's because anything that's inside the square brackets is taking for the literal character and not for its special meaning. 

#Also see how the notation marks aren't present in the resulting list.

#If we want our split list to include the elements that we're using to split the values we can use capturing parentheses like this.

print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

'''
['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']
'''

#This gave us both the sentences and notation marks as elements of a list. 

#Another interesting function provided by the RE module is called sub(). It's used for creating new strings by substituting all or part of them for a different string, similar to the replace() string method but using regular expressions for both the matching and the replacing. 

#Let's see this in an example. So we had some logs in our system that included e-mail addresses of users and we wanted to anonymize the data by removing all the addresses. We could do that by using an expression.

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))

'''
Received an email for [REDACTED]
'''

#The expression that we're using for identifying email addresses has two parts: the part before that at sign and the part after it. 

#Check out the part that comes before the at sign. We include the alphanumeric characters represented by backslash w which includes letters, numbers, and the underscore sign as well as a dot, percentage sign, plus, and dash. 

#After the at sign, we only allow the alphanumeric characters dot and dash. This will match all email addresses as well as some strings that aren't really valid email addresses like an address with two dots. 

#In this scenario we want to be better safe than sorry. So we're going to redact anything that looks like an address. If we wanted to validate that the address is an actual email we would need to be a lot stricter.

#We just use a regular expression for searching in a plain string for replacing. Let's now look at an example using sub where we use regular expressions for the replacing. 

#For that, we'll go back to our code that switched the order of names of people and use sub to create the new string.

print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))   #=====> Ada Lovelace

#So once again we'd use parentheses to create capturing groups. In the first parameter, we've got an expression that contains the two groups that we want to match: one before the comma and one after the comma. 

#We want to use a second parameter to replace the matching string. We use backslash two to indicate the second captured group followed by a space and backslash one to indicate the first captured group. 

#When referring to captured groups, a backslash followed by a number indicates the corresponding captured group. This is a general notation for regular expressions, and it's used by many tools that support regexes, not just Python. 

#We can also use them to match patterns that repeat themselves which use capturing groups as back references. We won't look into them here, but if you want to learn more, you'll find a bunch more info about them online. 

#We want to split a piece of text by either the word "a" or "the", as implemented in the following code. What is the resulting split list?

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

'''
['One sentence. Ano', 'r one? And ', ' l', 'st one!']
'''

#With that, we've wrapped up our overview of the power of regular expressions in Python. There were some things that we didn't get to cover, but our aim is to give you a foundation to build on. We hope that you've got a pretty good picture of the many things that we can do with regexes, and we encourage you to keep learning about them on your own. 

#Now as we've said, regular expressions aren't easy, but they're incredibly useful, so well worth the effort to master. To help you do this, we've got a practice quiz up next before you can jump into the next lab.

#Example 01 - We're working with a CSV file, which contains employee information. Each record has a name field, followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers, and needs to be modified to the international format, with "+1-" in front of the phone number. Fill in the regular expression, using groups, to use the transform_record function to do that.

import re
def transform_record(record):
  new_record = re.sub(r",(\d{3})",r",+1-\1",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

'''
Sabrina Green,+1-802-867-5309,System Administrator
Eli Jones,+1-684-3481127,IT specialist
Melody Daniels,+1-846-687-7436,Programmer
Charlie Rivera,+1-698-746-3357,Web Developer
'''

#Example 02 - The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.

import re
def multi_vowel_words(text):
  pattern = r"(\w+[a,e,i,o,u]{3,}\w+)"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

'''
['beautiful']
['Obviously', 'queen', 'courageous', 'gracious']
['rambunctious', 'quietly', 'delicious']
['queue']
[]
'''

#Example 03 - The transform_comments function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function:

import re
def transform_comments(line_of_code):
  result = re.sub(r"[\#]{1,}", "//",line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

'''
// Start of program
  number = 0   // Initialize the variable
  number += 1   // Increment the variable
  return(number)
'''

#Example 04 - The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to complete this function.

import re
def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b",r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

'''
My number is (212) 345-9999.
Please call (888) 555-1234
123-123-12345
Phone number of Buckingham Palace is +44 303 123 7300
'''