import sqlite3
import functions
conn = sqlite3.connect(
    "Database.db",
    check_same_thread=False
)

c = conn.cursor()

# -----------------------------
# USER INFO
# -----------------------------

c.execute("SELECT * FROM user_info")
user = c.fetchone()
name, age, sex, weight, height, bmi = user


