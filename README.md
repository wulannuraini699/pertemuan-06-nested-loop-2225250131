# Pertemuan 06 Nested Loop Python
Nama: Wulan Nur'aini
NIM: 2225250131
Kelas: 3E
## Tujuan
1. Memahami konsep dasar dan penggunaan *nested loop* (perulangan bersarang) dalam bahasa Python.
2. Membentuk pola tabel perkalian berukuran $n \times n$.
3. Menggunakan variabel akumulator untuk menghitung total baris dan total keseluruhan.
4. Menggunakan variabel pencacah (*counter*) untuk menghitung banyaknya hasil perkalian genap.

## Cara Menjalankan
'''bash
python3 tugas/tabel_perkalian_dan_statistik.py
## Algoritma Tugas 3
Dalam penyelesaian program tabel_perkalian_dan_statistik.py, komponen nested loop dan variabel pembantu berfungsi sebagai berikut:
Loop Luar (for i in range(1, n + 1)): Berperan untuk mengontrol dan mengeksekusi perulangan setiap baris dari baris ke-1 hingga baris ke-$n$. Loop luar juga menginisialisasi ulang nilai akumulator total_baris = 0 sebelum perulangan kolom dimulai serta menampilkan hasil total baris di akhir setiap baris.
Loop Dalam (for j in range(1, n + 1)): Berperan untuk mengontrol perulangan setiap kolom dari kolom ke-1 hingga kolom ke-$n$. Loop dalam menghitung nilai perkalian hasil = i * j, menampilkan nilainya ke layar secara teratur, serta menambahkan nilainya ke variabel akumulator.
Akumulator (total_baris & total_semua):
  total_baris: Menjumlahkan seluruh nilai perkalian dalam satu baris tertentu ($i$).
  total_semua: Menakumulasikan seluruh hasil perkalian dari awal hingga akhir ($n \times n$).
Counter (count_genap): Menghitung frekuensi atau jumlah perkalian yang menghasilkan bilangan genap dengan memeriksa kondisi hasil % 2 == 0.
## Hasil Pengujian
Tabel Hasil Pengujian Latihan 1 
| Input | Keluaran Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :---: |
| Default ($i=1..3, j=1..4$) | Menampilkan 12 pasang indeks (1 1 sampai 3 4) dan `Banyak pasangan = 12` | `1 1`<br>`1 2`<br>`1 3`<br>`1 4`<br>`2 1`<br>`2 2`<br>`2 3`<br>`2 4`<br>`3 1`<br>`3 2`<br>`3 3`<br>`3 4`<br>`Banyak pasangan = 12` | Sesuai |

Tabel Hasil Pengujian Latihan 2 
| Input ($n$) | Keluaran Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :---: |
| `1` | `*` | `*` | Sesuai |
| `3` | `- * * * *` | `- * * * *` | Sesuai |
| `5` | `- * * * * * * * * * * * * *` | `- * * * * * * * * * * * * *` | Sesuai |

Tabel Hasil Pengujian Latihan 3 
| Input | Keluaran Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :---: |
| Default (4 Baris) | `Jumlah baris 1 = 6`<br>`Jumlah baris 2 = 12`<br>`Jumlah baris 3 = 18`<br>`Jumlah baris 4 = 24` | `Jumlah baris 1 = 6`<br>`Jumlah baris 2 = 12`<br>`Jumlah baris 3 = 18`<br>`Jumlah baris 4 = 24` | Sesuai |

Tabel Hasil Pengujian Latihan 4 
| Input ($n$) | Keluaran Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :---: |
| `2` | `Banyak pasangan = 1` | `Banyak pasangan = 1` | Sesuai |
| `3` | `Banyak pasangan = 3` | `Banyak pasangan = 3` | Sesuai |
| `5` | `Banyak pasangan = 10` | `Banyak pasangan = 10` | Sesuai |

Tabel Hasil Pengujian Tugas 
| Input ($n$) | Hasil Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :---: |
| `1` | **Tabel:**<br>`   1 \| Total Baris 1: 1`<br><br>**Statistik:**<br>Total seluruh hasil perkalian : `1`<br>Banyak hasil perkalian genap  : `0` | **Tabel:**<br>`   1 \| Total Baris 1: 1`<br><br>**Statistik:**<br>Total seluruh hasil perkalian : `1`<br>Banyak hasil perkalian genap  : `0` | Sesuai |
| `2` | **Tabel:**<br>`   1    2 \| Total Baris 1: 3`<br>`   2    4 \| Total Baris 2: 6`<br><br>**Statistik:**<br>Total seluruh hasil perkalian : `9`<br>Banyak hasil perkalian genap  : `3` | **Tabel:**<br>`   1    2 \| Total Baris 1: 3`<br>`   2    4 \| Total Baris 2: 6`<br><br>**Statistik:**<br>Total seluruh hasil perkalian : `9`<br>Banyak hasil perkalian genap  : `3` | Sesuai |
| `3` | **Tabel:**<br>`   1    2    3 \| Total Baris 1: 6`<br>`   2    4    6 \| Total Baris 2: 12`<br>`   3    6    9 \| Total Baris 3: 18`<br><br>**Statistik:**<br>Total seluruh hasil perkalian : `36`<br>Banyak hasil perkalian genap  : `5` | **Tabel:**<br>`   1    2    3 \| Total Baris 1: 6`<br>`   2    4    6 \| Total Baris 2: 12`<br>`   3    6    9 \| Total Baris 3: 18`<br><br>**Statistik:**<br>Total seluruh hasil perkalian : `36`<br>Banyak hasil perkalian genap  : `5` | Sesuai |

## Analisis Efisiensi
Loop luar (for i) mengeksekusi sebanyak $n$ kali (untuk baris 1 sampai $n$).
Pada setiap 1 kali eksekusi loop luar, loop dalam (for j) berjalan sebanyak $n$ kali (untuk kolom 1 sampai $n$).
Secara total, operasi di dalam loop dalam (perkalian, pencetakan, akumulasi, dan pengecekan genap) dieksekusi sebanyak $n \times n = n^2$ kali. Kompleksitas waktu (time complexity) dari algoritma ini adalah $O(n^2)$.

## Refleksi
Kesalahan yang Ditemukan: Lupa melakukan reset/inisialisasi ulang variabel total_baris = 0 di dalam loop luar sebelum loop dalam dieksekusi.
Dampak Kesalahan: Nilai total_baris terus terakumulasi dari baris-baris sebelumnya, sehingga jumlah baris ke-2, ke-3, dst. menjadi tidak akurat (terlalu besar).
Cara Memperbaiki: Memindahkan penetapan nilai total_baris = 0 ke dalam loop luar (for i in range(1, n + 1)), persis sebelum loop dalam (for j) dimulai. Hal ini memastikan total_baris selalu dimulai dari angka 0 pada setiap baris baru.
