"""
Index yang tersusun rapih

ada array yang berisi ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B'].
guru meminta agar tulisan C saja yang ditampilkan ke dalam layar.
penuhi permintaan guru tersebut.

Contoh
Input:
['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

Output:
C C
"""
tech = ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

# lanjutkan code dibawah ini
tech = ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

# Loop melalui setiap elemen dalam array dan mencetak yang bernilai 'C'
for char in tech:
    if char == 'C':
        print(char, end=' ')