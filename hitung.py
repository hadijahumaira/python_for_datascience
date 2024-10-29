# Meminta input dari pengguna
gaji_per_jam = float(input("Masukkan gaji per jam: "))
jam_per_minggu = int(input("Masukkan jumlah jam kerja per minggu: "))
minggu_bekerja = 5  # Lama liburan yang akan diisi dengan bekerja adalah 5 minggu
pajak = 0.14          # Pajak 14%
pengeluaran_baju_aksesoris = 0.1  # 10% untuk baju dan aksesoris
pengeluaran_alat_tulis = 0.01     # 1% untuk alat tulis
persentase_sedekah = 0.25         # 25% untuk sedekah
persentase_anak_yatim = 0.3       # 30% dari sedekah untuk anak yatim

# 1. Pendapatan Budi sebelum pajak
pendapatan_sebelum_pajak = gaji_per_jam * jam_per_minggu * minggu_bekerja

# 2. Kurangkan pajak dari pendapatan awal
jumlah_pajak = pendapatan_sebelum_pajak * pajak
pendapatan_setelah_pajak = pendapatan_sebelum_pajak - jumlah_pajak

# 3. Jumlah uang untuk baju dan aksesoris
uang_baju_aksesoris = pendapatan_setelah_pajak * pengeluaran_baju_aksesoris

# 4. Jumlah uang untuk alat tulis
uang_alat_tulis = pendapatan_setelah_pajak * pengeluaran_alat_tulis

# 5. Jumlah uang untuk sedekah
sisa_setelah_belanja = pendapatan_setelah_pajak - uang_baju_aksesoris - uang_alat_tulis
uang_sedekah = sisa_setelah_belanja * persentase_sedekah

# 6. Jumlah uang untuk anak yatim
uang_anak_yatim = uang_sedekah * persentase_anak_yatim

# 7. Jumlah uang untuk kaum dhuafa
uang_kaum_dhuafa = uang_sedekah * (1 - persentase_anak_yatim)

# Output hasil dengan format pemisah ribuan
print("1. Pendapatan Budi sebelum pajak: Rp", "{:,.0f}".format(pendapatan_sebelum_pajak).replace(",", "."))
print("2. Pendapatan Budi setelah pajak: Rp", "{:,.0f}".format(pendapatan_setelah_pajak).replace(",", "."))
print("3. Uang untuk baju dan aksesoris: Rp", "{:,.0f}".format(uang_baju_aksesoris).replace(",", "."))
print("4. Uang untuk alat tulis: Rp", "{:,.0f}".format(uang_alat_tulis).replace(",", "."))
print("5. Jumlah uang untuk sedekah: Rp", "{:,.0f}".format(uang_sedekah).replace(",", "."))
print("6. Jumlah uang untuk anak yatim: Rp", "{:,.0f}".format(uang_anak_yatim).replace(",", "."))
print("7. Jumlah uang untuk kaum dhuafa: Rp", "{:,.0f}".format(uang_kaum_dhuafa).replace(",", "."))
