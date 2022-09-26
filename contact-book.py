import sqlite3

def initializeDB():
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    query = 'select sqlite_version();'
    cursor.execute(query)

    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))
    cursor.close()



def main():
    try:
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')

        query = 'select sqlite_version();'
        cursor.execute(query)

        result = cursor.fetchall()
        print('SQLite Version is {}'.format(result))
        cursor.close()

    except sqlite3.Error as error:
        print('Error occured - ', error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')


if __name__=="__main__":
    main()