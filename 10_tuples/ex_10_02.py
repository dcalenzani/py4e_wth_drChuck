#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
fname = input("Enter file name: ")
fh = open('mbox_short.txt')
ay = dict()
lst = list()
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        hours = line[5]
        hour = hours.split(':')
        count = hour[0]
        ay[count] = ay.get(count, 0) + 1
    else:
        continue
for k, v in sorted(ay.items()):
    print (k, v)
