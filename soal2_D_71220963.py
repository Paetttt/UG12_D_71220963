print("~~~~ Table MATEMATIKA Nich ~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")

pilihan = input("Pilih model Matematika")
a = (input("Masukan model matematika yang diinginkan 1/2: "))
if pilihan == '1':
   print("Perkalian")
b = (input("Menampilkan table matematika dari angka: "))
if pilihan == '2':
   print("Pembagian")

for i in range(1, 11):
    if i == 8 :
        continue
    print(i, "x",i, "=", i*i)