import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#here we list

#parse the email line
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):continue
    #here well get the domain
    lineone = line.split()
    email = lineone[1]
    dlist = email.split('@')
    domain = dlist[1]
    #email into table i guess, will have to separate the update
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))
conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()