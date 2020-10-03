print('Siapa nama kamu?')
nama =  input()

print("umur kamu ?")
umur = input()

f = open(nama + '.txt', 'w+')
f.write(nama+'\n'+umur)
f.close

print('\n')
print('Terima kasih telah mengisi data..')
 


