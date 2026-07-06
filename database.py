import sqlite3

# database connection
conn = sqlite3.connect("Database.db")

# cursor
c = conn.cursor()

# meal table
c.execute("""
CREATE TABLE IF NOT EXISTS meal(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    DATE TEXT,
    MEAL TEXT,
    CALORIES INTEGER
)
""")

# activity table
c.execute("""
CREATE TABLE IF NOT EXISTS activity(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    type TEXT,
    calories REAL
)
""")

# weight table
c.execute("""
CREATE TABLE IF NOT EXISTS weight(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    weight REAL
)
""")

c.execute("""
DROP TABLE user_info""")


# user info table
c.execute("""
CREATE TABLE IF NOT EXISTS user_info(
    name TEXT,
    age INTEGER,
    sex TEXT,
    weight REAL,
    height REAL,
    bmi REAL
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS summary(
date TEXT PRIMARY KEY,
surplus REAL
        )""")




c.execute("""
CREATE TABLE IF NOT EXISTS weight_history(
    date TEXT PRIMARY KEY,
    weight REAL
)
""")


# save changes
conn.commit()

