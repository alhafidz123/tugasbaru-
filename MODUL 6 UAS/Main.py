# Input data pelanggan
nama_pelanggan = input("Masukkan nama pelanggan: ")
status_member = input("Apakah pelanggan memiliki kartu member? (ya/tidak): ")
total_belanja = float(input("Masukkan total belanja: "))

# Tentukan potongan berdasarkan status member dan total belanja
if status_member.lower() == "ya":
    if total_belanja >= 500000:
        potongan = 0.1
    elif total_belanja >= 100000:
        potongan = 0.02 # Asumsikan potongan sebelumnya sudah ditentukan
    else:
        potongan = 0.03
else:
    if total_belanja >= 100000:
        potongan = 0.03
    else:
        potongan = 0

# Hitung diskon dan total belanja setelah potongan
diskon_rupiah = total_belanja * potongan
total_belanja_setelah_potongan = total_belanja - diskon_rupiah

# Tampilkan hasil
print("Nama Pelanggan:", nama_pelanggan)
print("Status Member:", status_member)
print("Total Belanja Sebelum Potongan:", total_belanja)
print("Diskon (dalam Persen):", potongan * 100, "%")
print("Diskon (dalam Rupiah):", diskon_rupiah)
print("Total Belanja Setelah Potongan:", total_belanja_setelah_potongan)