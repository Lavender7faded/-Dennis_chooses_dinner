import sqlite3

conn = sqlite3.connect('dinnerbot.db')
cursor = conn.cursor()

def init_db_user_dinner():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_dinner (
            id                          INTEGER PRIMARY KEY,
            time                        INTEGER,
            user_id                     INTEGER,
            user_first_name             STRING,
            user_surname                STRING,
            user_garnish                TEXT,
            user_entree                 TEXT,
            user_dinner_time            INTEGER
    )
    ''')
    conn.commit()

def init_db_user_dinner_tomorrow():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_dinner_tomorrow (
            id                          INTEGER PRIMARY KEY,
            time                        INTEGER,
            user_id                     INTEGER,
            user_first_name             STRING,
            user_surname                STRING,
            user_garnish_tomorrow       TEXT,
            user_entree_tomorrow        TEXT,
            user_dinner_time_tomorrow   INTEGER
    )
    ''')
    conn.commit()

def init_db_users_id():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users_id (
            id                  INTEGER PRIMARY KEY,
            user_id             INTEGER UNIQUE
    )
    ''')
    conn.commit()

def db_table_user_dinner(time: int, user_id: int, user_first_name: str, user_surname: str, user_garnish: str, user_entree: str, 
                    user_dinner_time: int):
	cursor.execute('''INSERT INTO user_dinner (time, user_id, user_first_name, user_surname, user_garnish, user_entree, 
                    user_dinner_time) VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                    (time, user_id, user_first_name, user_surname, user_garnish, user_entree, 
                    user_dinner_time))
	conn.commit()

def db_table_user_dinner_tomorrow(time: int, user_id: int, user_first_name: str, user_surname: str, user_garnish_tomorrow: str, user_entree_tomorrow: str, user_dinner_time_tomorrow: int):
	cursor.execute('''INSERT INTO user_dinner_tomorrow (time, user_id, user_first_name, user_surname, user_garnish_tomorrow, user_entree_tomorrow, user_dinner_time_tomorrow ) VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                    (time, user_id, user_first_name, user_surname, user_garnish_tomorrow, user_entree_tomorrow, user_dinner_time_tomorrow))
	conn.commit()

def db_table_users_id(user_id: int):
	cursor.execute('INSERT INTO users_id (user_id) VALUES (?)', (user_id, ))
	conn.commit()

cursor.execute("SELECT user_id FROM users_id")
user_id = cursor.fetchall()
users = []
i = 0 
while i != len(user_id):
    users_id = user_id[i][0]
    users.append(users_id)
    i += 1
print(users)