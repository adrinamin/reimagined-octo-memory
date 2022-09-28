import sqlite3


def getSqlVersion(cursor):
    query = 'select sqlite_version();'
    cursor.execute(query)
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))




def main():
    try:
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')

        getSqlVersion(cursor)

        cursor.execute("CREATE TABLE contactBook(id none, firstname text, lastname text, adress text, phonenumber text)")

        cursor.close()

    except sqlite3.Error as error:
        print('Error occured - ', error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')


if __name__=="__main__":
    main()