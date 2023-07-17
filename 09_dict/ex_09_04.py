#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input("Enter file name: ")
fh = open(fname)

a_list = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        address = line.split()
        email = address[1]
#actualiza/suma/cuenta
        a_list[email] = a_list.get(email, 0) + 1
    else: continue

#largest key
largest = -1
smallest = None
for k,v in a_list.items() :
    if v > largest:
        largest = v
        smallest = k
print(smallest, largest)

#a veces lo más largo es más simple, no siempre.
