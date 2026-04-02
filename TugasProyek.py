total_hari = int(input("Masukkan jumlah hari proyek: "))

# Menghitung tahun
tahun = total_hari // 365
sisa_hari = total_hari % 365

# Menghitung bulan
bulan = sisa_hari // 30
hari = sisa_hari % 30

# Menampilkan hasil
print(f"Hasil konversi: {tahun} Tahun, {bulan} Bulan, {hari} Hari")
