## 1.Mencari Bilangan Terbesar dari 3 Variabel
Program sederhana untuk menentukan bilangan terbesar dari tiga angka yang diinputkan pengguna
## Deskripsi Program Program ini akan:
1. Meminta user memasukkan 3 bilangan berbeda
2. Membandingkan ketiga bilangan tersebut
3. Menentukan bilangan mana yang terbesar
4. Menampilkan hasilnya ke layar
## Flowchart Program
![image](c:\Users\user\Downloads\Gambar 1.jpeg)
## Kode Program
```Python
a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))

if a > b:
    if a > c:
        print("A adalah terbesar")
        terbesar = a
    else:
        print("C adalah terbesar")
        terbesar = c
else:
    if b > c:
        print("B adalah terbesar")
        terbesar = b
    else:
        print("C adalah terbesar")
        terbesar = c

print(f"Bilangan terbesar adalah: {terbesar}")
```
```Python
## Contoh Output Program
Masukkan bilangan A: 10
Masukkan bilangan B: 9
Masukkan bilangan C: 30
C adalah terbesar
Bilangan terbesar adalah: 30
## Cara Kerja
Menerima input 3 bilangan (A, B, C) dari user Melakukan pengecekan dengan urutan: Apakah A > B? Jika ya: cek apakah A > C? Jika ya: A adalah terbesar Jika tidak: C adalah terbesar Jika tidak: cek apakah B > C? Jika ya: B adalah terbesar Jika tidak: C adalah terbesar Menampilkan bilangan terbesar yang ditemukan
```

## 2.Program Mencari Bilangan Terbesar Dari N Bilangan
Program sederhana untuk mencari nilai terbesar dari sekumpulan bilangan yang dimasukkan oleh pengguna menggunakan loop while True dan break statement.
## Deskripsi Program
Program ini akan:
1. Menggunakan while True untuk perulangan
2. Menggunakan break statement untuk menghentikan program
3. Membandingkan setiap input dengan nilai maksimum yang tersimpan
4. Menampilkan bilangan terbesar yang ditemukan
## Flowchart Program
![image](c:\Users\user\Downloads\Gambar 2.jpeg)
## Kode Program
```Python
bilangan_max = 0

while True:
    bilangan = int(input("Masukan bilangan: "))
    if bilangan == 0:
        break
    if bilangan > bilangan_max:
        bilangan_max = bilangan
print(f"Bilangan paling gede: {bilangan_max}")
```
```Python
## Contoh Output Program
Masukan bilangan: 7
Masukan bilangan: 10
Masukan bilangan: 11
Masukan bilangan: 0
Bilangan paling gede: 11
## Cara Kerja
Program menginisialisasi variabel max dengan nilai 0 Program memulai loop tak terbatas dengan while True Di dalam loop:

Program meminta user memasukkan bilangan Jika user memasukkan 0, program akan keluar dari loop dengan break Jika bilangan yang dimasukkan lebih besar dari nilai maximum saat ini, nilai maximum diperbarui

Setelah keluar dari loop, program menampilkan bilangan terbesar
```
