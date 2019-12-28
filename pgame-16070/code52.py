# latihan code 5.2 : Tuple 

# Buat variabel dan memberikan elemen 
buah=('Durian', 'Mangga', 'Rambutan', 'Mangga')
 
# print jumlah element Tuple 
print("Jumlah Element :", len(buah))
 
# tambah element yang sama 
#buah.append('Mangga')
 
# hitung element “Mangga” → hasil 2 
print("Jumlah Buah Mangga:", buah.count("Mangga"))
 
# buat tuple dalam tuple 
buah=('Durian', 'Mangga', 'Rambutan', 'Mangga','Salak', 
('Nangka', 'Apel'))
 
# print tuple buah posisi ke [-1][0] => "Nangka" 
print("Bauah [-1][0] :", buah[-1][0])
 
# Mengubah element tuple 
x_buah = list(buah) 
x_buah[0] = "Melon" 
Buah = tuple(x_buah)
 
# Print hasil yang diubah : element [0] => "Melon" 
print("Tuple :", buah)