import connect

print("Update Identitas di id berapa?")
urut = input()
print("Update Nama : ")
nama = input()
print("Update Email : ")
email = input()
cursor = connect.mysql.cursor()
sql = "UPDATE users SET nama = %s, email = %s WHERE id = %s"
val = (nama, email, urut)
cursor.execute(sql, val)
connect.mysql.commit()

print("data deretan", urut, "telah diupdate!")