import psycopg2

connection = psycopg2.connect('dbname=postgres user=postgres password=1234')

cursor = connection.cursor()


cursor.execute('DROP TABLE IF EXISTS todos;')
cursor.execute('''
CREATE TABLE todos (
id INTEGER PRIMARY KEY,
completed BOOLEAN NOT NULL DEFAULT False
);
''')
cursor.execute('INSERT INTO todos (id, description) values(%s, %s);', (1, 'thing1'))
cursor.execute('INSERT INTO todos (id, description) values(%s, %s);', (2, 'thing2'))
#print out the query result
cursor.execute('SELECT * from todos;')
result = cursor.fetchall()
print(result)
#after fetch all, if you want to fetch one, there will be nothing left to be fetched

connection.commit()

cursor.close()
connection.close()