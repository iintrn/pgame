# latihan code 5.1 : List (lanjutan)

#  buah=["Durian","Mangga","Rambutan] # List
buah=("Durian","Mangga","Rambutan") # Tuple

print(buah)
print(type(buah)) # print tipe data buah

#buah.append("Melon")
#print(buah)

buah=("Durian","Mangga","Rambutan",("Nangka","Apel"))
print("tuple didalam tuple : ", buah)

# Ubah Elemen tuple
x_buah=list(buah)	# ubah tuble ke list
x_buah[0]="Melon"	# ubah elemen [0]
buah = tuple(x_buah)	# ubah kembali ke tuple

print("Buah setelah diubah element [0] : ", buah)