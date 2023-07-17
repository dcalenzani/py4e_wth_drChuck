import json
import psycopg2

#Connect to de postgres DB
conn = psycopg2.connect("dbname = postgres user=daniboi password=c4l3nz4n1$743")
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.execute('''
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Member;

CREATE TABLE Course (
    id  SERIAL PRIMARY KEY,
    title   TEXT UNIQUE
);

CREATE TABLE Users (
    id  SERIAL PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id  INTEGER,
    role    INTEGER,
    PRIMARY KEY (user_id, course_id)
);

''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    #print((name, title))

    cur.execute('''INSERT INTO Users (name)
        VALUES ( %s ) 
        ON CONFLICT (name) 
        DO NOTHING;''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = %s ', (name, ))
    user_id = cur.fetchone()[0]
    
    cur.execute('''INSERT INTO Course (title)
        VALUES ( %s ) ON CONFLICT (title) DO UPDATE SET''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = %s ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT INTO Member (user_id, course_id, role)
        VALUES ( %s, %s, %s) ON CONFLICT(user_id, course_id, role) REPLACE''', ( user_id, course_id, role ) )
    cur.execute('SELECT id FROM Course')
    conn.commit()

