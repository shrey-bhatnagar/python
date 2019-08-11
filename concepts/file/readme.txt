
Mode	Description
'r'	This is the default mode. It Opens file for reading.
'w'	This Mode Opens file for writing. 
	If file does not exist, it creates a new file.
	If file exists it truncates the file.
'x'	Creates a new file. If file already exists, the operation fails.
'a'	Open file in append mode. 
	If file does not exist, it creates a new file.
't'	This is the default mode. It opens in text mode.
'b'	This opens in binary mode.
'+'	This will open a file for reading and writing (updating)


Summary
* Python allows you to read, write and delete files
* Use the function open("filename","w+") to create a file. The + tells the python compiler to create a file if it does not exist
* To append data to an existing file use the command open("Filename", "a")
* Use the read function to read the ENTIRE contents of a file
* Use the readlines function to read the content of the file one by one.
