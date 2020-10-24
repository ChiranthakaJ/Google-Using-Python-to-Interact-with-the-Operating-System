#Now, we're going to submerge ourselves in subprocesses. 

#Up to now, we've been using Python to interact with the operating system through baked in functionality. For example, we've used file objects to read the contents of files. Use the SAQ tool module to check if the disk is full. 

#And use a sys module to process standard input, get parameters, or generate an exit code. But what if we needed to run a system program from a Python script? Say, for example, that as part of a Python script, we needed to send ICMP packets to a host to check if it's responding. 

#We could try to look for an external module that provides this functionality. Or we can just run the ping command, which will send packets for us. Sometimes it's easier or faster to use a system command as part of our Python script to accomplish a task, or use some functionality that doesn't exist in the Python modules, neither built in or external. 

#For these cases, Python provides a way to execute system commands in our scripts, using functions provided by the subprocess module. Let's check out an example. First, we'll import a subprocess module, and then we'll call the date command, which shows the current date using the subprocess.run function.

import subprocess 
subprocess.run["date"]

#The run function returns an object of the CompletedProcess type. This object includes information related to the execution of the command. From the information that got printed we can see that the returncode of the command was 0. 

#To run the external command a secondary environment is created for the child process or subprocess where the command is executed. While the parent process, which is our script, is waiting on the subprocess to finish, it's blocked, which means that the parent can't do any work until the child finishes. 

#And I bet a lot of parents out there saying, I know that's right. After the external command completes its work, the child process exits and the flow of control returns to the parent. 

#Then the script can continue with normal execution. Let's see this in action by calling the sleep command, which waits for a number of seconds that we tell it before returning.

#You may have noticed that while the sleep command was running, the interpreter was blocked and we couldn't interact with it. That's exactly what we mean about the parent process being blocked until the child process is done. 

#Check out how we call the command. The run function receives a list that starts with the name of the command that we want to call, followed by any other parameters that we want to pass to that command. So any elements following the program name are the command-line arguments for it. 
 
#In this case, we're requesting sleep to wait for two seconds. In the last two examples, the commands executed successfully, and so the returncode inside the completed process instance was 0. Let's check out an example where the exit status isn't 0. If we call LS with a file name that doesn't exist, LS will print an error and return an exit status different than 0. 

#This will be stored in the return code attribute of the completed process instance, and we can access that value in our code

#We can see that the command failed and the returncode stored was 2, letting us know that there was an error. We could use this information in the script to do something different in case the failure. 

#Using the run function like this is useful if we just want to run a command and only care about whether or not it was successful. The output of the command will be printed to the screen, which means that our script has no control over it. 

#This can be handy for system commands that either don't have useful output like cp, chmod, sleep, and many others, or when we don't care about processing the output any further. In other words, when it's just fine to have the output, print it to the screen. 

#For example, if we're writing a script that's changing the permissions of a bunch of files in a tree of directories, we don't care about the output of the chmod command. We only want to know if it was successful or not. 

#If instead, we want to capture the output of an external command and then operate with the results, we need a different strategy. We'll dive into that in the next video. I'll see you there.