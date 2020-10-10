#Example 01 - Iterating through the file content line by line and printing line by line.

with open("Python_File_Sample_V2.txt") as file: 
    for line in file: 
        print(line)
        
#Example 02 - Iterating through the file content line by line and printing line by line. Also this removes the line spacing that has one after another. Remember to compare the result with the previous content.

with open("Python_File_Sample_V2.txt") as file: 
    for line in file: 
        print(line.strip())
        
#Example 03 - Converting the content to uppercase.

with open("Python_File_Sample_V2.txt") as file: 
    for line in file: 
        print(line.strip().upper())
        
#Example 04 - Passing the content to a list.

file = open("Python_File_Sample_V1.txt")
lines = file.readlines()
file.close() 

#Even after closing the file, you can still use the lines variable because you haven't cleared it. So still lines variable contains the list of lines of the openned file.

#Now sorting the content and print it.

lines.sort() 

print(lines)
