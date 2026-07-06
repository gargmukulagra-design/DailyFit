import sqlite3
from datetime import date
import variables

# today's date
day = date.today()


# BMI category
def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"

# user info function
def takeinfo(n, a, s, w, h):
    conn = sqlite3.connect("Database.db")
    c= conn.cursor()

    bmi = w / ((h / 100) ** 2)

    c.execute("""
    INSERT INTO user_info
    (name, age, sex, weight, height, bmi)
    VALUES(?,?,?,?,?,?)
    """, (n, a, s, w, h, bmi))

    conn.commit()

# meal function
def AddMeal(m, cal):
    conn = sqlite3.connect("Database.db")
    c= conn.cursor()

    c.execute("""
    INSERT INTO meal(DATE, MEAL, CALORIES)
    VALUES(?,?,?)
    """, (day, m, cal))

    conn.commit()

# activity function
def AddActivity(t, cal):

    conn = sqlite3.connect("Database.db")
    c= conn.cursor()

    c.execute("""
    INSERT INTO activity(date, type, calories)
    VALUES(?,?,?)
    """, (day, t, cal))

    conn.commit()

def recommended_calories(
        maintenance,
        bmi
    ):

        if bmi < 18.5:

            # gain weight
            return maintenance + 300

        elif bmi < 25:

            # maintain
            return maintenance

        elif bmi < 30:

            # moderate deficit
            return maintenance - 300

        else:

            # stronger deficit
            return maintenance - 500
        

def eaten_cal(day):
    conn = sqlite3.connect("Database.db")
    c= conn.cursor()

    c.execute("""
    SELECT SUM(CALORIES)
    FROM meal
    WHERE DATE = ?
    """, (day,))
    return c.fetchone()[0]

def burnt_cal(day):
        conn = sqlite3.connect("Database.db")
        c= conn.cursor()

        c.execute("""
            SELECT SUM(calories)
            FROM activity
            WHERE date = ? 
            """,(day,))
        return c.fetchone()[0]

def add_surplus(day):
    conn = sqlite3.connect("Database.db")
    c= conn.cursor()

    maintenance_cal= 10*variables.weight + 6.25*variables.height - 5*variables.age + burnt_cal(day) + 5
    calories_required = recommended_calories(maintenance_cal,variables.bmi)
    total_Calories_eaten = eaten_cal(day)
    surplus = total_Calories_eaten-calories_required
    c.execute("""
            INSERT OR REPLACE INTO summary
            VALUES(? ,?)
                    """,(day,surplus))
    conn.commit()
    conn.close()


def add_weight(day,weight):
     conn = sqlite3.connect("Database.db")
     c= conn.cursor()

     c.execute("""
    INSERT OR REPLACE INTO weight_history
    VALUES(?,?)
        """,(day,weight))
     
     conn.commit()
     conn.close()