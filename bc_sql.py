import re
import mysql.connector


barcode_db = mysql.connector.connect(
    host = "34.80.39.159",
    user = "root",
    passwd = "team6isbest",
    )
# print(barcode_db)
cursor = barcode_db.cursor()

sql_id = "SELECT id FROM `Fiteat`.`Barcode`;"
sql_name = "SELECT food_name FROM `Fiteat`.`Barcode`;"

def food_id():
    try: 
        cursor.execute(sql_id)
        results = cursor.fetchall()
        for row in results:
            #print(row)
            return row
    except:
        print("ID not available")

def food_name():
    try: 
        cursor.execute(sql_name)
        results = cursor.fetchall()
        for row in results:
            #print(row)
            return row
    except:
        print("Food not available")

#food_name()
#food_id()
    