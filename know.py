"""
Gimana cara filter data ya?

Haikal ingin mencoba filter isi data array yang diberikan oleh temannya, yaitu array yang berisi angka-angka
tantangan yang diberikan oleh temannya adalah hanya berisi nilai ganjil.
bantu Haikal untuk menyelesaikan tantangan tersebut.

Contoh
Input:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

Output:
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""
arr = range(1, 100)
#lanjutkan code dibawah ini

# Membuat array dari 1 hingga 20
arr = list(range(1, 21))

# Memfilter hanya angka ganjil
ganjil = [num for num in arr if num % 2 != 0]

print(ganjil)


