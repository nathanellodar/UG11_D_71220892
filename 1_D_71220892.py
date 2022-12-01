print("Halo selamat datang di bioskop!")
print("Dimana kamu ingin menonton?")

def jam():
    print("Mau nonton jam berapa:")
    
    print("1. 12.35")
    print("2. 14.45")
    print("3. 16.55")
    print("4. 19.05")

    pjam=(int(input("masukkan angka pilihan anda:")))
    if pjam==1:
        print("oke berhasil!, silahkan dinikmati di jam", 12.35)
    elif pjam==2:
        print("oke berhasil!, silahkan dinikmati di jam", 14.45)
    elif pjam==3:
        print("oke berhasil!, silahkan dinikmati di jam", 16.55)
    elif pjam==4:
        print("oke berhasil!, silahkan dinikmati di jam", 19.05)

def layar():
    print("Mau nonton layar bioskop apa:")
    print("1. Reguler")
    print("2. Dolby almos")
    print("3. Premiere")
    playar=(int(input("Pilih nomor tipe layar:")))
    if playar<=3:
        jam()
    else:
        print("Pilihan tidak tersedia")
def film():
    print("Mau nonton film apa nih? Ada film:")
    print("1. Frozen")
    print("2. Keramat")
    print("3. KKN di Desa Penari")
    pfilm=(int(input("pilih nomor film:")))
    if pfilm<=3:
        layar()
    else:
        print("Pilihan tidak tersedia")

print("1. XXI Empire")
print("2. XXI Amplaz")
print("3. XXI JCM")

t=int(input("masukan pilihanmu:"))
if t<=3:
    film()
else:
    print("Tidak ada")
