import os

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as f:
        f.write(comments)
    filesize = os.path.getsize(filename)
    return(filesize)

print(create_python_script("program.txt"))


import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass
  os.chdir("..")
  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))