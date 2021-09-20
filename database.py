import datetime
import sqlite3

conn = sqlite3.connect('dinnerbot.db')
cursor = conn.cursor()

def init_db_user_dinner():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_dinner (
            id                          INTEGER PRIMARY KEY,
            data                        INTEGER,
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
            data                        INTEGER,
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

def db_table_user_dinner(data: int, time: int, user_id: int, user_first_name: str, user_surname: str, user_garnish: str, user_entree: str, 
                    user_dinner_time: int):
	cursor.execute('''INSERT INTO user_dinner (data, time, user_id, user_first_name, user_surname, user_garnish, user_entree, 
                    user_dinner_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                    (data, time, user_id, user_first_name, user_surname, user_garnish, user_entree, 
                    user_dinner_time))
	conn.commit()

def db_table_user_dinner_tomorrow(data: int, time: int, user_id: int, user_first_name: str, user_surname: str, user_garnish_tomorrow: str, user_entree_tomorrow: str, user_dinner_time_tomorrow: int):
	cursor.execute('''INSERT INTO user_dinner_tomorrow (data, time, user_id, user_first_name, user_surname, user_garnish_tomorrow,
                    user_entree_tomorrow, user_dinner_time_tomorrow ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                    (data, time, user_id, user_first_name, user_surname, user_garnish_tomorrow, user_entree_tomorrow, user_dinner_time_tomorrow))
	conn.commit()

def db_table_users_id(user_id: int):
	cursor.execute('INSERT INTO users_id (user_id) VALUES (?)', (user_id, ))
	conn.commit()


def select_users_id():
    user_id = "SELECT user_id FROM users_id"
    return [x[0] for x in conn.execute(user_id)]

def select_user_dinner():
    user_dinner = "SELECT data, user_id FROM user_dinner"
    return [x for x in conn.execute(user_dinner)]

def select_user_dinner_tomorrow():
    user_dinner_tomorrow = "SELECT user_garnish_tomorrow, user_entree_tomorrow, user_dinner_time_tomorrow FROM user_dinner_tomorrow"
    return [x for x in conn.execute(user_dinner_tomorrow)]

# def select_user_dinner():
#     cursor.execute("SELECT user_id, user_garnish, user_entree, user_dinner_time FROM user_dinner")
#     dinner = cursor.fetchall()
#     for i in dinner:
#         print(i)


def users_id_reminder():
    time_now = datetime.datetime.now()

    computer_time = time_now.strftime("%d-%m-%Y")
    ids = []
    for users in select_user_dinner():
        if computer_time != users[0]:
            for id in select_users_id():
                if id == users[1]:
                    ids.append(id)
    return ids
print(users_id_reminder())

# for id in set(users_id_reminder()):
#     print(id)    
            

print(select_user_dinner_tomorrow())