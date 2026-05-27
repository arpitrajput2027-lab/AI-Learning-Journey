# Different types of file modes in Python
# 'r' - Read mode: Default mode. Opens a file for reading. Raises an error if the file does not exist.
# 'w' - Write mode: Opens a file for writing. Creates a new file if
#       the file does not exist or truncates the file if it exists.
# 'a' - Append mode: Opens a file for appending. Creates a new file
#       if the file does not exist.
# 'x' - Exclusive creation mode: Creates a new file. Raises an error
#       if the file already exists. and writing at the end of the file.
# 'b' - Binary mode: Used to handle binary files (e.g., images, videos).
# 't' - Text mode: Default mode. Used to handle text files.
# '+' - Update mode: Opens a file for both reading and writing.

# You can combine these modes, e.g., 'rb' for reading a binary file,
# 'w+' for writing and reading, etc.
# Example usage:

f = open("example.txt", "w+")  # Open a file for both writing and reading
f.write("Hello, World!\n")      # Write to the file

data = f.read()
print(data)    # Read from the file but will print nothing as the pointer is at the end after writing
f.close()
