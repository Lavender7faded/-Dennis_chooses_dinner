import sqlite3
import datetime

conn = sqlite3.connect('dinnerbot.db')              # creating database
cursor = conn.cursor()                              # creatin cursor object

def init_db_user_dinner():
    
    '''
    Creating table with nine column for chosen dishes from users
    '''

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_dinner (
            id                          INTEGER PRIMARY KEY,
            user_id                     INTEGER UNIQUE,
            date                        INTEGER,
            time                        INTEGER,
            user_first_name             STRING,
            user_surname                STRING,
            user_garnish                TEXT,
            user_entree                 TEXT,
            user_dinner_time            INTEGER
    )
    ''')
    conn.commit()

def init_db_user_dinner_tomorrow():
        
    '''
    Creating table with nine column for chosen tomorrow dishes from users
    '''

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_dinner_tomorrow (
            id                          INTEGER PRIMARY KEY,
            user_id                     INTEGER UNIQUE,
            date                        INTEGER,
            time                        INTEGER,
            user_first_name             STRING,
            user_surname                STRING,
            user_garnish_tomorrow       TEXT,
            user_entree_tomorrow        TEXT,
            user_dinner_time_tomorrow   INTEGER
    )
    ''')
    conn.commit()


def db_table_user_dinner(user_id: int, date: int, time: int, user_first_name: str, user_surname: str, user_garnish: str, user_entree: str, user_dinner_time: int):
    
    '''
    Adding date to table and saving it
    '''

    cursor.execute('''
    INSERT OR REPLACE INTO user_dinner (user_id, date, time, user_first_name, user_surname, user_garnish, user_entree, user_dinner_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, date, time, user_first_name, user_surname, user_garnish, user_entree, user_dinner_time))
    conn.commit()

def db_table_user_dinner_tomorrow(user_id: int, date: int, time: int, user_first_name: str, user_surname: str, user_garnish_tomorrow: str, user_entree_tomorrow: str, user_dinner_time_tomorrow: int):
	        
    '''
    Adding date to table and saving it
    '''

    cursor.execute('''
    INSERT OR REPLACE INTO user_dinner_tomorrow (user_id, date, time, user_first_name, user_surname, user_garnish_tomorrow,user_entree_tomorrow, user_dinner_time_tomorrow ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, date, time, user_first_name, user_surname, user_garnish_tomorrow, user_entree_tomorrow, user_dinner_time_tomorrow))
    conn.commit()


def select_user_dinner():

    '''
    Selecting user id and date from table user_dinner
    '''

    user_dinner = "SELECT user_id, date FROM user_dinner"
    return [x for x in conn.execute(user_dinner)]

def select_user_dinner_tomorrow():
    user_dinner_tomorrow = "SELECT user_id, date, user_garnish_tomorrow, user_entree_tomorrow, user_dinner_time_tomorrow FROM user_dinner_tomorrow"
    return [x for x in conn.execute(user_dinner_tomorrow)]


def select_all():

    '''
    Selecting data from table user_dinner
    '''

    all_users = "SELECT date, time, user_first_name, user_surname, user_garnish, user_entree, user_dinner_time FROM user_dinner"
    return [x for x in conn.execute(all_users)]

def select_all_tomorrow():
    
    '''
    Selecting data from table user_dinner_tomorrow
    '''

    all_users_tomorrow = "SELECT date, time, user_first_name, user_surname, user_garnish_tomorrow, user_entree_tomorrow, user_dinner_time_tomorrow FROM user_dinner_tomorrow"
    return [x for x in conn.execute(all_users_tomorrow)]

def the_users_without_dinner():

    '''
    Сreating a list of users who don't use the bot today and didn't planning dinner ahead yesterday
    '''

    users_list = []
    for id in select_user_dinner_tomorrow():
        for users in select_user_dinner():
            time_now = datetime.datetime.now()
            computer_date = time_now.strftime("%d-%m-%Y")
            if computer_date != users[1] and id[2] == None:
                users_list.append(users[0])
    return users_list
