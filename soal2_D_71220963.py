print("~~~~ Table MATEMATIKA Nich ~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")

pilihan = ("Pilih model Matematika")
a = (input("Masukan model matematika yang diinginkan 1/2: "))
if pilihan == '1':
   print("Perkalian")
elif pilihan == '2':
    print("Pembagian")
else:
    print("Pilihan tidak tersedia jangan ngasal:)")

a = int(input("Menampilkan table matematika dari angka: "))

for i in range(1, 11):
    hasil = a * i
    print(a, "x",i, "=", hasil)

for i in range(1, 11):
    hasil = a * i
    print(a, "/",i, "=", hasil)