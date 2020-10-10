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

import csv 
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f: 
    name, phone, role = row
    print("Name: {}, Phone:{}, Role:{}".format(name, phone, role))
    
'''
Name: Sabrina Green, Phone:802-867-5309, Role:System Admin
Name: Eli Jones, Phone:684-348-1127, Role:IT Specialist
Name: Melody Daniels, Phone:846-687-7436, Role:Programmer
Name: Charlie Rivera, Phone:698-746-3357, Role:Web Developer
'''

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
