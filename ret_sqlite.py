#!/usr/bin/python
import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    # for row in rows:
    #     print row
    cols = [ desc[0] for desc in cur.description ]
    df = pd.DataFrame(rows, columns=cols)
    print df