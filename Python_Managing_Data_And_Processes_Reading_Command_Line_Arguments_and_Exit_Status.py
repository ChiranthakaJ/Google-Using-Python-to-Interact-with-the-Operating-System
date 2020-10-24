#Up to now. We've seen how different programs can read from and write to standard IO streams and how the show environment can influence execution of a program. Yet another common way of providing information to our programs is through command line arguments. 

#These are parameters that are passed to a program when it started. It's a super common practice to make our scripts receive certain values by command line arguments. It allows a code of the script to be generic while also letting us run it automatically without requiring any interactive user input. 

#This means that these arguments are really useful for system administration tasks. That's because we can specify the information that we want our program to use before it even starts. This lets us create more and more automation and you can't argue with that. 

#Although you could argue my humor isn't really that humorous. What can I say I'm a better coder than I am a comedian. Anyway, we can access these values using the argv in the sys module. Let's check this out by executing a very simple script that just prints this value. First, let's use our friendly cat command to look at what the script does.

import sys
print(sys.argv)

'''
#Empty
'''

#As you can see, our script just imports the sys module and prints the sys.argv list. Now, let's see what happens when we call the program.

#In this case, we called the script without any parameters. The list contains one single element. The name of the program that we just executed. Let's try passing a few parameters.

#Now, we see that each of the parameters that we pass is included as a separate element in the list and last up we have the concept of exit status or return code, which provides another source of information between the shell and the programs that get executed inside of it. 

#The exit status is a value returned by a program to the shell. In all Unix-like operating systems, the exit status of the process is zero when the process succeeds and different than zero if it fails. 

#The actual number returned gives additional info on what kind of error the program encountered. Knowing if a command finish successfully or not is helpful information which can be used by a program that's calling a command. 

#For example, it can use the information to retry the command. If it failed. To check the exit status of a program, we can use a special variable that lets us see what the exit status of the last executed command was. 

#The variable is the question mark variable. So to see the contents we use dollar sign question mark. Let's try this out using the WC command, which counts the number of lines words and characters in a file. First, we'll pass it our variables up Py Script and check the exit value.

#So here we first ran the WC command and it printed the values of lines, words and characters for our Python script. Then we printed the contents dollar sign question mark variable, and we can see that the exit value was zero. That's because WC ran successfully.

#Here WC couldn't run for the file that we pass because it doesn't exist. The command printed an error and when printing the contents of the dollar sign question mark variable, we see that it finished with an exit value of one. 

#So that's with system commands, but what about Python scripts? When a Python script finishes successfully, it exits with an exit value of zero. When it finishes with an error like type error or value error, it exits with a different value than zero. We can make it exit with whatever value is relevant. Let's check out an example of this.

import os 
import sys 

filename=sys.argv[1]
 
if not os.path.exists(filename): 
    with open(filename, "w") as f: 
        f.write("New file created\n")

else: 
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

#This script receives a file name as a command line argument. It first checks whether the file name exist or not. When the file doesn't exist, it creates it by writing a line to it. 

#When the file exist, our script print an error message and exits with an exit value of one. To try this out let's first execute the script and pass a file that doesn't exist.

#Nice looks like that was successful. Check out how it exited with the exit code zero even though we didn't specify this in the code. That's because that's the default behavior. Let's look at the contents of the file to make sure it's got what it should. Okay and what do you think will happen if we now run the command again?

#You guessed it. We get an error because the file already exists and so we get an exit code of one. So we've now seen how we can pass command line arguments to our Python programs and how we can make our programs tell us whether they've finished successfully or not. 

#These are both important tools that we'll use when creating automation. We'll use command line parameters to tell our programs what we want them to do without having to interact with them and we'll use exit values to know if our command succeeded or failed and then log failures and automatically retry the commands if we need to. 

#Well, we've definitely learned a lot over these last few videos. Chances are it got a little tricky at some points but you're doing an awesome job not letting these complex concepts stop you. Since you made it this far, you're bound to master all the ways that we can make our code interact with our shell environment. As always, take your time to review and then head on over to the quiz to put your new knowledge to practice.