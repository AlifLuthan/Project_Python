# Referensi : https://www.geeksforgeeks.org/os-module-python-examples/


import os
import sys
# apa fungsi dari module OS ? Module OS itu menyediakan Fungsi untuk Menghapus sebuah Direktori(Folder)
#selain Menghapus , module OS juga dapat mengubah dan Mengindentifikasi direktori(folder)

path = sys.argv[1] # Ditambahkan CLA agar Behavior lebih sama persis.
#path = input("Path File : ")# Input Path / Nama File yang ingin dihapus
if os.path.exists(path): # Jika didalam Path terdapat sebuah File
    os.remove(path) # Hapus File tersebut
    print("File Kamu Berhasil Terhapus : " , path) # Jika berhasil terhapus hasilnya Berhasil
else: # Jika Filenya Sudah Terhapus Sebelumnya , Hasil output seperti ini.
    print("Upss... File sudah terhapus sebelumnya : ", path) # Jika File Sebelumnya Sudah Terhapus
