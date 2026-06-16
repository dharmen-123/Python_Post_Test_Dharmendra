# Q5. Create a File Reader System: (5 Marks)
# • Ask user to enter a filename
# • Try to open and read the file
# • If file not found fi print 'File does not exist!'
# • If file is empty fi print 'File is empty!'
# • If success fi print total number of lines in file
# • Add finally block fi print 'Operation complete!

fname=input("Enter the file name : ")

file=open(fname,'x')
print("File Create successfully")

file=open(fname,'r')
if (not file):
    print("File does not exist")

elif file.empty:
    print("File is empty")



