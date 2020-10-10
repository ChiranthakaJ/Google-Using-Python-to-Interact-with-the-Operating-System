#Example 02 - File openning using the 'with' keyword.

#Once you open a file using the open() method, after the file operations you have to close it indefinitely. Otherwise other programs may not be able to use the same file. So that we have keep remember to close it using the close() method.

#To overcome this in Python we can have a different approach using the 'with' keyword.

with open("Python_File_Sample_V2.txt") as file: #This path is a relative path, which doesn't want to say the drive location and the root folder the file in. This is more accurate and error free method.
    
    print(file.read())
    
#With this approach, at the end of the execution the file will automatically closed.