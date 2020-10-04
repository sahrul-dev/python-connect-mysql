import connect

print("Masukan nama kamu")
nama = input()
print("Masukan email kamu")
email = input()

cursor = connect.mysql.cursor()
sql = "INSERT INTO users (nama, email) VALUES (%s , %s)"
val = (nama, email)
cursor.execute(sql, val)
connect.mysql.commit()

print("Data berhasil di masukan...")
