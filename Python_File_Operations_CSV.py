#Data comes in a bunch of different formats besides text. And you may need to deal with some of these in your scripts. Formats give data structure. 

# And remember that computers love structure and precision. To be able to process a data set, it helps to know ahead of time how that data set will be arranged. 

#If you can expect data to be represented in a certain way, it's easier to extract meaning from it.

#Let's look at a very simple example. If we have a file that contains one line per machine and details the users are logged into that machine, then when we read the file we know how to parse it to get the information that we want. 

#Parsing a file means analyzing its content to correctly structure the data. We use a bunch of different file formats to structure, store, and transport data.

#CSV stands for Comma Separated Values. CSV is a pretty simple format. These files are stored in plaintext. And each line in a CSV file generally represents a single data record. 

#Each field in that record is separated by a comma, with the contents of the field stored between the commas. For example, if we are storing information about employees at our company, we might store the data like this. The file is csv.txt

'''
Sabrina Green,802-867-5309,System Admin
Eli Jones,684-348-1127,IT Specialist
Melody Daniels,846-687-7436,Programmer
Charlie Rivera,698-746-3357,Web Developer
'''

#Looking at this example, the line that starts with Sabrina is a data record. And the name Sabrina Green represents a name field followed by a phone number field and a role field. 

#Python standard library includes a module which lets us read, create and manipulate CSV files. 

#So, we'll be using the CSV module. And to do that, we'll need to import it like we've been doing with the other modules.

import csv 

#Now, before we can parse a CSV file, we need to open the file the same way as before.
f = open("csv_file.txt")

#And now we can parse this file using the CSV module. 
csv_f = csv.reader(f)
#Okay, that has given us an instance of the CSV reader class. We can now iterate through its contents and access information that it parsed.

#Now, the row variable hold each row in the CSV file. This variable is a list with each field in the CSV corresponding to one element in the list. We know from the before that the first field is a name, the second one, the phone number, and the third, the role. So we can unpack the values so that we can use variables to refer to them.
for row in csv_f: 
    name, phone, role = row
    
    
    #Remember that for this to work we need to have the exact same amount of variables on the left side of the equal sign as the length of the sequence on the right side. Now that we've unpacked these values, let's print them to the screen.
    print("Name: {}, Phone:{}, Role:{}".format(name, phone, role))
    
'''
Name: Sabrina Green, Phone:802-867-5309, Role:System Admin
Name: Eli Jones, Phone:684-348-1127, Role:IT Specialist
Name: Melody Daniels, Phone:846-687-7436, Role:Programmer
Name: Charlie Rivera, Phone:698-746-3357, Role:Web Developer
'''
#As we mentioned, we unpack the row so that we don't have to use indexes to access each element in that list. For example, we could have used row[0] to access the name of the employee. This is valid but it can be hard to follow when reading a lot of code. Unpacking the list into name variables makes the code easier to understand later on. And before we forget, let's close this file now that we're done with it.

#Similarly, we can use the writer function to generate contents to a file. This can be really helpful if you process some data in your script and you must store it in a file. 

#Maybe you want to import it into a spreadsheet or use it later on in your script. We'll start by storing the data that we want to write into a list.

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

#We've created a list of lists. This is the data that we want to store in the CSV file, representing the names of the machines in our network and their IP addresses. 

#All right, with that data ready to be written, let's open the file in write mode. We'll use the with block that we saw before so we don't forget to close the file.

with open("hosts.csv", "w") as hosts.csv: 
    writer = csv.writer(hosts.csv) 
    writer.writerows(hosts)

#The writer variable is now an instance of a CSV writer class. There are two functions that we can use: write row, which we'll write one row at a time; and write rows, which we'll write all of them together.

#Let's see the content of the file outside Python. I use here Windows PowerShell. 
#The command is Get_Content D:\MyDev\projects\Python\Google-IT-Automation-Scripts-Python\Google-Using-Python-to-Interact-with-the-Operating-System\csv_file.txt
