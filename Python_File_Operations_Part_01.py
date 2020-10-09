#Example 01 - File openning and reading the content. Once done that closing.

#open() method is used to open a file in Python. Once you open the file the content will be available and the content needs to be assign to a variable in order to read. In here 'file' is the variable that holds the content once the file openned. 
file = open("Python_File_Sample_V1.txt")   

#readline() method used to read the content line by line. If this method executes one time, then the file buffer move to the next line.
print(file.readline())  #This will show the first line of the file.
print(file.readline())  #This will show the second line of the file.

#Once you execute the readline() method, the file buffer will ignore the previously read lines.

#After executing the readline() method, if you execute the read() method the content of the file will read from the point where the readline() method stopped reading.
print(file.read()) 

