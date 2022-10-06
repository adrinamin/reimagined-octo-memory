import sqlite3
import uuid


class Contact:
    def __init__(self, firstname, lastname, address, phonenumber):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phonenumber = phonenumber


def getSqlVersion(cursor):
    query = 'select sqlite_version();'
    cursor.execute(query)
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))


def createContactBookTable(cursor):
    cursor.execute("DROP TABLE IF EXISTS contactBook")
    cursor.execute("CREATE TABLE contactBook(id none, firstname text, lastname text, address text, phonenumber text)")


def readFromTable(cursor):
    print("Data Inserted in the table: ")
    contactBooks=cursor.execute("SELECT * FROM contactBook")
    for row in contactBooks:
        print(row)


def createContact():
    print("please insert contact information:")
    print("firstname: ")
    firstname = input()
    print("lastname: ")
    lastname = input()
    print("address: ")
    address = input()
    print("phone number")
    phoneNumber = input()
    return Contact(firstname, lastname, address, phoneNumber)

def main():
    try:
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')

        getSqlVersion(cursor)
        createContactBookTable(cursor)

        contact = createContact()
        insertCommand = "INSERT INTO contactBook VALUES ('{}', '{}', '{}', '{}', '{}')".format(str(uuid.uuid4()), contact.firstname, contact.lastname, contact.address, contact.phonenumber)
        
        cursor.execute(insertCommand)

        readFromTable(cursor)

        # Commit your changes in the database    
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print('Error occured - ', error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')


if __name__=="__main__":
    main()