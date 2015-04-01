#!/usr/bin/python
import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

with con:
    cur = con.cursor()
    cur.execute("""SELECT state, AVG(average_high) AS mean_high FROM cities
                    INNER JOIN weather on name = city
                    GROUP BY state
                    HAVING mean_high > 62
                    ORDER BY mean_high DESC""")
    rows = cur.fetchall()
    # for row in rows:
    #     print row
    cols = [ desc[0] for desc in cur.description ]
    df = pd.DataFrame(rows, columns=cols)
    print df