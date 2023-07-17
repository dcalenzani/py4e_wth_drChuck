'''
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
'''
uinput = input('Enter file name: ')
avg = 0
cou = 0
try:
    fh = open(uinput)
except:
    print(uinput, 'not a proper file name\nTRY AGAIN PLEASE')
    exit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    cou = cou + 1
    slice = line.find(':')
    textfloat = float(line[slice+1:])
    avg = (avg + textfloat)
print('Average spam confidence:', avg/cou)
