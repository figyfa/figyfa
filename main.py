import sqlite3

conn = sqlite3.connect('db.sqlite')

c = conn.cursor()

query = '''
SELECT count(*),name FROM album,artist WHERE album.artistid = artist.artistid GROUP BY Album.artistId;
'''

c.execute(query)

print(c.fetchall())

query = '''
SELECT name FROM track WHERE upper(name) LIKE '%LOVE%'
'''

c.execute(query)

print(c.fetchall())

query = '''
SELECT track.name FROM track INNER JOIN genre ON track.genreid = genre.genreid WHERE genre.name = 'Rock'
'''

c.execute(query)

print(c.fetchall())

query = '''
SELECT album.title,count(track.albumid) FROM track INNER JOIN album ON track.albumid = album.albumid GROUP BY album.title HAVING count(track.albumid) = (SELECT max(num_tracks) FROM (SELECT count(albumid) AS num_tracks FROM track GROUP BY albumid));
'''

c.execute(query)

print(c.fetchall())