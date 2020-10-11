#In our earlier examples, we saw how we can read and write CSV files, and we use list as datatype on the Python side. This works when we know what the fields are going to be, but it can be pretty cumbersome when we have a lot of columns, and we need to remember which is which. 

#Imagine if your lists of employees not only had name, phone number and role but also start date, username, office location, department, preferred pronouns and so on. It would soon get hard to keep track of which column corresponds to which position in the row. 

#For cases like this, it's common for CSVs to include the names of the columns as a first line in the file, like in this example; this CSV file list a bunch of internally developed programs used at the company including the latest version, the current development status and the number of people using it.

#Check out how the first line of the file includes the names of each of the fields. We can profit from this additional information by using DictReader, a slightly different reader that's also provided by the CSV module. 

#This reader turns each row of the data in a CSV file into a dictionary. We can then access the data by using the column names instead of the position in the row. 

#Let's see how that looks. So here we're opening the file and creating a DictReader to process our CSV data, then when going through the rows we can access information in each row using the keys just like we would when accessing data in the dictionary. 

#Let's try the below snippet as well.

import csv

with open("Software.csv") as software: 
    reader = csv.DictReader(software)
    for row in reader: 
        print(("{} has {} users").format(row["name"], row["users"]))
        
'''
MailTree has 324 users
CalDoor has 22 users
Chatty has 21 users
'''

#Two important things to call out here. One, the order of the fields in the file doesn't matter. We can just use the name of the field instead, and two, chatty chicken is still an alpha, so only it has four users but you know the name like that, it's going to be a hit.

#So we can use DictWriter in a similar way to generate a CSV file from the contents of a list of dictionaries. This means that each element in the list will be a row in the file, and the values of each field will come out of each of the dictionaries.

#For this to work, we'll also need to pass a list of the keys that we want to be stored in the file when creating the writer. Let's see this in action. 

#First we need a list of dictionaries with the data that we want to store. For this example, we want to store data about the users in our company and the departments that they work in. So here we have our list of dictionaries and each contain the keys, name, username and department. 

#We first define the list of keys that we want to write to the file, then we open the file for writing. Next we created the DictWriter passing the keys that we had identified before, and then we call two different methods on the writer. 

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
         {"name": "Lio Nelson", "username": "lion", "department": "User Experiance Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

keys = ["name", "username", "department"]

#We now want to write this HTML file and the code will look like this.

with open("by_department.csv", "w") as by_department: 
    writer = csv.DictWriter(by_department, fieldnames=keys) #Next we created the DictWriter passing the keys that we had identified before, and then we call two different methods on the writer. 
    
    writer.writeheader() #The right header method will create the first line of the CSV based on keys that we passed, and the right rows method will turn the list of dictionaries into lines in that file.
    writer.writerows(users)
    
#At the end a file named by_department.csv created in the same folder with the Python script.
    
'''
name,username,department

Sol Mansi,solm,IT infrastructure

Lio Nelson,lion,User Experiance Research

Charlie Grey,greyc,Development
'''

#Example 01 - We're working with a list of flowers and some information about each one. The create_file function writes this information to a CSV file. The contents_of_file function reads this file into records and returns the information in a nicely formatted block. Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file 
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    f = csv.DictReader(file)
    # Process each item of the dictionary
    for row in f:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

'''
a pink carnation is annual
a yellow daffodil is perennial
a blue iris is perennial
a red poinsettia is perennial
a yellow sunflower is annual
'''

#Example 02 - Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary. How do you skip over the header record with the field names?

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as f:
    # Read the rows of the file
    rows = csv.reader(f)
    headers = next(rows)
    # Process each row
    for row in rows:
      name, color, ty = row
      # Format the return string for data rows only
      return_string += "a {} {} is {}\n".format(color, name, ty)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

'''
a pink carnation is annual
a yellow daffodil is perennial
a blue iris is perennial
a red poinsettia is perennial
a yellow sunflower is annual
'''