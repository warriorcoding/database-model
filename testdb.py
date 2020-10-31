import psycopg2

connection = psycopg2.connect('dbname=postgres user=postgres password=1234')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')
cursor.execute('''
CREATE TABLE table2 (
id INTEGER PRIMARY KEY,
completed BOOLEAN NOT NULL DEFAULT False
);
''')
#list comprehensive
cursor.execute('INSERT INTO table2 (id, completed) values(%s, %s);', (1, True))
#dictionanry
SQL = 'INSERT INTO table2 (id, completed) values(%(id)s, %(completed)s);'
data = {'id':2, 'completed': False}
cursor.execute(SQL, data)

#print out the query result
cursor.execute('SELECT * from table2;')
result = cursor.fetchall()
print(result)
#after fetch all, if you want to fetch one, there will be nothing left to be fetched

connection.commit()

cursor.close()
connection.close()