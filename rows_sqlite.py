#!/usr/bin/python

import sqlite3 as lite

con = lite.connect('getting_started.db')

# Inserting rows by passing values directly to `execute()`
with con:
    cur = con.cursor()
    # cur.execute("INSERT INTO cities(name, state) VALUES ('Washington', 'DC'), ('Houston', 'TX')")
    cur.execute("INSERT INTO weather(city,year,warm_month,cold_month) VALUES('Washington', 2013, 'July', 'January')")
    cur.execute("INSERT INTO weather(city,year,warm_month,cold_month) VALUES('Houston', 2013, 'July', 'January')")