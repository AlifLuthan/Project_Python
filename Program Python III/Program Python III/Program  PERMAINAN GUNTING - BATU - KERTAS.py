#PROGRAM PERMAINAN GUNTING - BATU - KERTAS
#PROGRAM PERMAINAN 1 VS 1

balik = 'y'
while (balik == 'y'):
        print("PERMAINAN SUIT!")
        print("Pilihlah Pilihan Berikut Untuk Bermain : ")#memilih GBK dan bertarunglah!!
        print("1. Gunting") #PILIHAN SUIT
        print("2. Batu") #PILIHAN SUIT
        print("3. Kertas") #PILIHAN SUIT
        print("Ketentuannya !!!")#peraturan
        print("Dalam permainan Gunting-Batu-Kertas, Gunting mengalahkan Kertas, Kertas mengalahkan Batu,")
        print("dan Batu mengalahkan Gunting. Jika pilihan kedua pemain sama, maka hasil akhirnya adalah seri.")

        p1=input("Masukan Pilihan : ")#masukan pilihan p1(PLAYER1)
        p2=input("Masukan Pilihan : ")#masukan pilihan p2(PLAYER2)
        print()
        if p1 == "gunting":
            if p2 == "gunting":
                print("SERI!!!")#JIKA GUNTING MELAWAN GUNTING ARTINYA SERI
            if p2 == "batu":
                print("KALAH!!!")#JIKA MELAWAN BATU MAKA AKAN KALAH
            if p2 == "kertas":
                print("MENANG!!!")#JIKA LAWANNYA KERTAS MAKA MENANG
        if p1 == "batu":
            if p2 == "batu":
                print("SERI!!!")#JIKA LAWANNYA BATU MAKA HASILNYA SERI
            if p2 == "kertas":
                print("KALAH!!!")#JIKA LAWANNYA KERTAS MAKA HASILNYA KALAH
            if p2 == "gunting":
                print("MENANG!!!")#JIKA LAWANNYA GUNTING MAKA HASILNYA MENANG
        if p1 == "kertas":
            if p2 == "kertas":
                print("SERI!!!")#JIKA LAWANNYA KERTAS MAKA HASILNYA SERI
            if p2 == "batu":
                print("MENANG!!!")#JIKA LAWANNYA BATU MAKA HASILNYA MENANG
            if p2 == "gunting":
                print("KALAH!!!")#JIKA LAWANNYA GUNTING MAKA HASILNYA KALAH
            
        print("=========================================================")
        balik = input("Apakah ingin melanjutkan program (y/n)? ")
        print("=========================================================")

# Program Ini Bertujuan Untuk Have fun
# Bermain dalam Program Gunting Batu Kertas
# Semua Rentetan Program Diatas Sudah Jelas
# Boleh dikembangkan apabila " ingin "