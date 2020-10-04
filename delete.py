import connect

print("masukan yang mau dihapus?")
nama = input()

cursor = connect.mysql.cursor()
sql = "DELETE FROM users WHERE nama = %s"
val = (nama,)
cursor.execute(sql, val)
connect.mysql.commit()

print(cursor.rowcount, "data terhapus!")