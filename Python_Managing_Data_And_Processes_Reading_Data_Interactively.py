#We've talked before about reading and writing files. Using files to store information and then processing that data over a script is a great way to build automation. 
 
#But sometimes we need to interact with the user and ask them for certain pieces of information that just can't be stored in a file. 

#To do this Python provides a function called input. This function allows us to prompt the user for a certain value that we can then use for our scripts. Let's see what that looks like.

#--------------------------------------------------------------------------
#Content of the hello.py script
#--------------------------------------------------------------------------
# Input function allows for prompt the user for a certain value which can be used in scripts
name = input("Please enter your name: ")
print("Hello, " + name)

#Here we have a script called hello.py. It's a very simple script, it asks the user for their name, and then prints the greeting that uses that name. Let's execute the script to see it in action.

#Enter your name and see the result by your self.

#Hi computer, the input function always returns a string. If we want the data that we're reading to be a different data type like a number or a date, then we need to convert the string to a format that we want. Let's look at a different example.

#Please refer the code in the seconds.py script.

#--------------------------------------------------------------------------
#Content of the seconds.py script
#--------------------------------------------------------------------------
#!/usr/bin/enb python3

def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds.".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")

print("Good bye!")

#This script does a bunch of things, so let's go over it piece by piece. First, we define a function that converts into seconds the number of hours, minutes, and seconds. 

#The actual program starts by printing a welcome message and then entering a while loop. See how we first initialized the cont variable that we'll use to check whether the user wants to continue or not? 

#In the body of the while loop, we ask the user to provide the number of hours, minutes, and seconds for the conversion. 

#As our two seconds function requires integers, we're converting the value returned by the input function using the int function. With those three values, we then call the function and print the result. 

#After that we ask the user whether they want to do another conversion or not. Let's try to script out and see what happens.

#Great, our code seems to be working properly. We entered three numbers and it did the right conversion. It's now asking us if we want to continue or not. I think we have the time to answer, don't you? Let's say, yes.

#This time, we said that we didn't want to continue, so the program finished and exited. And with that, we've seen how we can interactively ask the user for input. 

#We're only a few minutes and seconds into this module and you've already learned a new concept. Just imagine how much more you'll learn by the end of this module. 

#Interactively asking the user for input might not always be the best approach for a problem we're trying to solve. But it's a great tool that you've just added to your IT toolbox.

