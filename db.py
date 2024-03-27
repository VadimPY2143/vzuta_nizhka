import sqlite3



try:
    sqlite_connection = sqlite3.connect("vzuta.db")
    sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS shoes(
                                    id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    price INTEGER,
                                    description TEXT,
                                    type TEXT,
                                    photo1 TEXT,
                                    photo2 TEXT,
                                    photo3 TEXT,
                                    photo4 TEXT,
                                    photo5 TEXT,
                                    photo6 TEXT,
                                    photo7 TEXT); '''
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('Table ORDERS Created')
    cursor.close()

except sqlite3.Error as error:
    print('Error: ', error)

finally:
    if sqlite_connection:
        sqlite_connection.commit()
        print('DB disconnected')



def add_test_item(name,price,description,type,photo1,photo2,photo3,photo4,photo5,photo6,photo7):
    sqlite_connection = sqlite3.connect("vzuta.db")
    cursor = sqlite_connection.cursor()
    cursor.execute(
        "INSERT INTO shoes (name,price,description,type,photo1,photo2,photo3,photo4,photo5,photo6,photo7) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (name,price,description,type,photo1,photo2,photo3,photo4,photo5,photo6,photo7))
    sqlite_connection.commit()
    sqlite_connection.close()


add_test_item("Кросівки", 800, "Новинка кросівки", "Кросівки", 'https://i.im.ge/2024/03/24/WQljZf.img-8766-1.jpeg','','','','','','')
print('SUCCESSFULLY ADDED')