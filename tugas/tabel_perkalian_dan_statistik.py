print("Tabel Perkalian dan Statistik")

n = int(input("n: "))
while n <= 0:
    print("Nilai n harus berupa bilangan bulat positif (> 0). Silakan coba lagi.")
    n = int(input("n: "))
total_semua = 0
count_genap = 0
print("\nTabel Perkalian:")
for i in range(1, n + 1):
    total_baris = 0
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4d}", end=" ")
        total_baris += hasil
        total_semua += hasil
        if hasil % 2 == 0:
            count_genap += 1
    print(f"| Total Baris {i}: {total_baris}")
print("\nStatistik:")
print(f"Total seluruh hasil perkalian : {total_semua}")
print(f"Banyak hasil perkalian genap  : {count_genap}")