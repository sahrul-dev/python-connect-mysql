import connect

print("Masukan nama kamu")
nama = input()
print("Masukan email kamu")
email = input()

cursor = connect.mysql.cursor()
sql = "INSERT INTO users (nama,email) VALUES ($s, $s)"
val = (nama, email)
connect.mysql.commit()

print("Dat berhasil di masukan..")
