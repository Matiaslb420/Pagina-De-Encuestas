import sqlite3
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
#cur.execute('DELETE FROM inicio_encuesta')
#cur.execute('DELETE FROM inicio_puntajes')
cur.execute('select * from inicio_encuesta')
print(cur.fetchall())
cur.execute('SELECT * FROM inicio_puntajes')
print(cur.fetchall())
con.commit()
con.close()