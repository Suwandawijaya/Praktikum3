print("Program Python Hitung Luas dan Keliling Lingkaran")


pi    = 22/7
jari   = float(input("Masukan Jari-jarinya : "))
luas   = pi*(jari*jari)
keliling   = 2*pi*jari

print("\n-----------------Hasilnya-----------------")
print("Luas Lingkaran =","{:.2f}".format(luas)) 
print("Keliling Lingkaran =","{:.2f}".format(keliling))