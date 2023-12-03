import sqlite3

# назва файлу БД
DB_NAME = "database.db"


def create_connection():
    # створення підключення
    try:
        sqlite_connection = sqlite3.connect(DB_NAME)
        return sqlite_connection
    except Exception as e:
        print(f"create_connection error: {e}")
        return None


def create_new_user(id, fullname, username, age, location):
    # створення нового користувача в БД
    connection = create_connection()
    if connection is None:
        return None
    try:
        cursor = connection.cursor()
        sql_query = f'INSERT INTO users(id,fullname,username,age,location) values({id},"{fullname}","{username}",{age},"{location}" )'
        cursor.execute(sql_query)
        connection.commit()
    except Exception as e:
        print(f"create_new_user error: {e}")
    finally:
        if connection:
            connection.close()


def user_exist(user_id):
    #чи існує користувач в БД
    connection = create_connection()
    if connection is None:
        return None
    try:
        cursor = connection.cursor()
        sql_query = f'select count(*) from users where id = {user_id}'
        cursor.execute(sql_query)
        total_rows = cursor.fetchone()[0]
        if total_rows >0:
            return True
        else:
            return False
    except Exception as e:
        print(f"user_exist error: {e}")
        return None
    finally:
        if connection:
            connection.close()


def get_user_by_id(user_id):
    # отримання інформації про користувача з БД за його айді
    connection = create_connection()
    if connection is None:
        return None
    try:
        cursor = connection.cursor()
        sql_query = f'SELECT * FROM users WHERE id = {user_id}'
        cursor.execute(sql_query)
        user_data = cursor.fetchone()

        return user_data

    except Exception as e:
        print(f"get_user_by_id error: {e}")
        return None

    finally:
        if connection:
            connection.close()


def get_users_by_location(location):
    # отримання користувачів з БД за їхньою локацією
    connection = create_connection()

    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        sql_query = f'SELECT * FROM users WHERE location = "{location}"'
        cursor.execute(sql_query)
        users_data = cursor.fetchall()
        return users_data

    except Exception as e:
        print(f"get_users_by_location error: {e}")
        return None

    finally:
        if connection:
            connection.close()


def create_users_table():
    # Створення таблиці "users" в БД
    connection = create_connection()

    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        sql_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER NOT NULL UNIQUE,
                fullname TEXT NOT NULL,
                username TEXT NOT NULL,
                age INTEGER NOT NULL,
                location TEXT NOT NULL
            )
        '''
        cursor.execute(sql_query)
        connection.commit()
        print("Table 'users' created successfully.")

    except Exception as e:
        print(f"create_users_table error: {e}")

    finally:
        if connection:
            connection.close()


# Виклик функції для створення таблиці "users"
#create_users_table()

#create_new_user(435345,"Maxim Kozenko","@kozenko",25,"Kyiv")
#create_new_user(435346,"Maxim Bulba","@kozenko",25,"Kyiv")
#create_new_user(435348,"Maxim Qyer","@kozenko",25,"Svitlovodsk")

#print(user_exist(435345))
#user_info = get_user_by_id(435345)
#users_in_location = get_users_by_location("Kyiv")
