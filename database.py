#!/usr/bin/python
import sqlite3 as lite
import pandas as pd

month = raw_input("Enter a month: ")

con = lite.connect('getting_started.db')

cities = (
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'),
    ('Washington', 'DC'),
    ('Houston', 'TX'),
    ('Las Vegas', 'NV'),
    ('Atlanta', 'GA')
)

weather = (
    ('New York City', 2013, 'July', 'January', 62),
    ('Boston', 2013, 'July', 'January', 59),
    ('Chicago', 2013, 'July', 'January', 59),
    ('Miami', 2013, 'August', 'January', 84),
    ('Dallas', 2013, 'July', 'January', 77),
    ('Seattle', 2013, 'July', 'January', 61),
    ('Portland', 2013, 'July', 'December', 63),
    ('San Francisco', 2013, 'September', 'December', 64),
    ('Los Angeles', 2013, 'September', 'December', 75),
    ('Washington', 2013, 'July', 'January', 12),
    ('Houston', 2013, 'July', 'January', 34),
    ('Las Vegas', 2013, 'July', 'December', 99),
    ('Atlanta', 2013, 'July', 'January', 1),
)

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")

    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")

    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

    cur.execute("""SELECT name, state FROM cities
                    INNER JOIN weather on name = city
                    WHERE warm_month = '{0}'
                    GROUP BY state
                    ORDER BY average_high DESC""".format(month))
                    # HAVING mean_high > 62
    rows = [ ', '.join(list(i)) for i in cur.fetchall() ]
    print 'The cities that are warmest in {0} are: '.format(month) + ', '.join(rows)
    # for row in rows:
        # print ', '.join(row)
    # cols = [ desc[0] for desc in cur.description ]
    # df = pd.DataFrame(rows, columns=cols)
    # print df