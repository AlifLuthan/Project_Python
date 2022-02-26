# Referensi : https://careerkarma.com/blog/python-delete-file/
# Referensi : https://www.w3schools.com/python/python_file_remove.asp
# Referensi : https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder-in-python
# Referensi : https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/
# Referensi : https://www.geeksforgeeks.org/os-module-python-examples/


import os
# apa fungsi dari module OS ? Module OS itu menyediakan Fungsi untuk Menghapus sebuah Direktori(Folder)
#selain Menghapus , module OS juga dapat mengubah dan Mengindentifikasi direktori(folder)

path = input("Path File : ")# Input Path / Nama File yang ingin dihapus
if os.path.exists(path): # Jika didalam Path terdapat sebuah File
    os.remove(path) # Hapus File tersebut
    print("File Kamu Berhasil Terhapus : " , path) # Jika berhasil terhapus hasilnya Berhasil
else: # Jika Filenya Sudah Terhapus Sebelumnya , Hasil output seperti ini.
    print("Upss... File sudah terhapus sebelumnya : ", path) # Jika File Sebelumnya Sudah Terhapus