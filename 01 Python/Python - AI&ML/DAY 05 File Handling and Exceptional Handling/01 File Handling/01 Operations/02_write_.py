f = open("DAY 05 File Handling and Exceptional Handling/01 File Handling/01 Operations/demo_Write.txt","w")
f.write("This is first line written using write() method.\n")
f.close()

f = open("DAY 05 File Handling and Exceptional Handling/01 File Handling/01 Operations/demo.txt","w")
f.write("If we try to write in existing written file using 'w' mode, it will overwrite the existing content.\n")
f.close()