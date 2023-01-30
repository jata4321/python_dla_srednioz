import sqlite3

con = sqlite3.connect('./data/tutorial.db')

cur = con.cursor()

cur.execute('CREATE TABLE if NOT EXISTS movie(title, year, score, my_score)')


def insert_data():
    cur.execute("""INSERT INTO movie VALUES
                ("Jak rozpętałem drugą wojnę",1967, 8.6, 9),
                ("And Now for Something Completely Different", 1971, 7.5, 8)
                """)
    con.commit()


def insert_many_data():
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9, 8),
        ("Monty Python's The Meaning of Life", 1983, 7.5, 5),
        ("Monty Python's Life of Brian", 1979, 8.0, 9),
    ]
    cur.executemany('INSERT INTO movie VALUES(?,?,?,?)', data)
    cur.connection.commit()


def delete_from_db():
    cur.execute("DELETE from movie WHERE year > 1979")
    cur.connection.commit()


# insert_data()
# cur.execute("DROP TABLE movie")
res = cur.execute(
    "SELECT year, title, score, my_score FROM movie WHERE year > 1980 ORDER by year")

[print(film) for film in res.fetchall()]
print(cur.connection.total_changes)

cur.connection.close()
