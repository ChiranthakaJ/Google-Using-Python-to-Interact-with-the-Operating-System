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