import mysql.connector

def db_values():
    mydb = mysql.connector.connect(
        host="sampreet.mysql.database.azure.com",
        user="username",
        password="",
        database="sampreet_1010"
    )
    mycursor = mydb.cursor()
    query = f"Select * from sampreet.9090.product_pricing limit 5;"

    mycursor.execute(query)
    records = mycursor.fetchall()
    columns = mycursor.description
    column_names = []

    for col in columns:
        column_names.append(col[0])
    data = []
    for rec in records:
        each_row = zip(column_names, rec)
        data.append(dict(each_row))

    mycursor.close()
    mydb.close()
    return data