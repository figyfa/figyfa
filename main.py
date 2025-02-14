import sqlite3

conn = sqlite3.connect('db.sqlite')

c = conn.cursor()

query = '''
SELECT count(firstname),country FROM customer GROUP BY country;
'''

c.execute(query)

print(c.fetchall())

