import sqlite3

con = sqlite3.connect('temperature_cache.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE temperatures
                (query_time datetime, temperature real)''')
con.commit()
con.close()
