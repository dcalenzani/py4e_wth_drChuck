'''
5.1 Write a program that prompts a user for integer numbers repeteadly until the user enters 'done'. Once 'done' is entered, print out the total sum of the numbers inserted, the total of numbers inserted and the average number. 
'''
num = 0
tot = 0.0
while True:
        sval = input('Enter a number:')
        if sval == 'done':
            break
        try:
            fval = int(sval)
        except:
            print('invalid input')
            continue
        print(fval)
        num = num + 1
        tot = tot + fval

print ('ALL DONE MY FRIEND')
print (tot, num, tot/num)