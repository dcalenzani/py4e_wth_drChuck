'''
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
Use words.txt as the file name
'''
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print(fname, 'not a proper file name\nTRY AGAIN PLEASE')
    exit()
fr = fh.read()
fs = fr.rstrip()
fu = fs.upper()
print(fu)
#took me a while, I was trying to loop with 'continue' but should have used 'If'. I did it closer to the excercise and still had some issues on the use of 'read()'
