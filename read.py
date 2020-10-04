import connect

cursor = connect.mysql.cursor()

sql = "SELECT * FROM users"
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print(row)
