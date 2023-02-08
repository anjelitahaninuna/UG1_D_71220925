
harga = int(input("Masukkan harga:"))
total = 0 
total+= harga
while True :
    
    lanjut = str(input("Apakah anda membeli barang lagi?[yes/no]:"))
        
    if lanjut=="yes":
        harga = int(input("Masukkan harga:"))
        total+=  harga
        #harga= int(input("\nharga barang:"))
        print("total belanja", total)

    elif lanjut =="no":
        #total+= harga
        print("total belanja:", total)
        break
    else:
        print("Invalid")
        break
        
    