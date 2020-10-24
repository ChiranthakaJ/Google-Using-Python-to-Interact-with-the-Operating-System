#We've now seen a couple ways of getting information into and out of our scripts. We know how to read and write to files and accept input from the keyword and print it to the screen, too. 

#But what exactly is going on behind the scenes when we do this? How does a Python program connect to both the screen and the keyboard? Well, it uses I/O streams. I/O streams are the basic mechanism for performing input and output operations in your programs. 

#You can think of these streams as pathways between your programs and their input sources like a keyboard, or output, like the screen. I/O streams aren't just available for Python programs. When we run a system command on our terminal, I/O streams are also being used to connect that command to the terminal input and output. 

#This way, we can see the results of the command or enter data interactively if that's how the program works. We call these streams because the data keeps flowing. A program can read input and generate output as long as it needs to achieve its goal. Okay, what do these streams mean in practice? 

#Most operating systems supply three different I/O streams by default each with a different purpose. The standard input stream commonly referred to as STDIN is a channel between a program and a source of input. Usually in the form of text data from the keyboard. 

#When we use the input function to accept user input in a Python script we're using the STDIN stream. 

#The standard output stream or STDOUT is a pathway between a program and a target of output, like a display. STDOUT generally takes the form of text displayed in a terminal. As that play when we use the print function to write information to the screen. 

#The last type of pre-made I/O stream is called standard error, or STDERR. Standard error displays output like standard out, but is used specifically as a channel to show error messages and diagnostics from the program. It's usually printed to the screen. If you've ever run some Python code and receive an error, then that error message was probably printed using standard error stream. Let's see this consolidated in an example.

#Our script here has three lines, each line is interacting with different stream. In the first one, we read from standard input, in the second one, we write to standard output. In the last one, we generate an error by concatenating a string to an integer. This error will be printed to standard error, let's try it out.

#So we first read some data through standard input and then printed it through standard output. Python then printed a type error because we tried to do something weird. 

data = input("This will come from STDIN: ")
print("Now we will write it to STDOUT: " + data)

#Before executing the example from here onwards, we have to uncomment the commented statement below.

#print("Now we generate an error to STDERR: "+ data + 1) 
#This statement generated an error. To display it, the default error stream STDERR used.

#As we called out earlier, these I/O streams aren't restricted to just Python programs. For example, we've been using the cat system command to display the contents of a file. When we do that, those contents are printed to the terminal using standard output like this.

#And when one of these commands generates an error, that error is displayed to standard error. For example, if we use an unsupported flag with the ls system command, which normally shows the content of directories, we get an error.

#I know, it looks like standard output and standard error are the same here. That's because they both get displayed to the screen but they're actually pretty different. We'll look at exactly how they're different later in the course. 

#We'll keep coming across these streams in our Python programs. So you start to become more familiar with them and later on in the course, we'll even learn how we can redirect them to other files and other processes. 

#The key takeaway for you to remember at this point is that I/O streams are ways for programs to get and receive information. In the next couple of videos, we'll take a look at other ways that we can provide information to our programs, environment variables, and command-line arguments.

