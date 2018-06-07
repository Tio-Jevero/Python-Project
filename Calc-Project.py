
'''
Author  : Najma Cresentio Jevero Dhiwangkara
Website : https://cyberharmony.com
Email   : invasion@cyber-wizard.com
Facebook: Empty Mind
Github  : https://github.com/fluster

'''
#This Version is For Linux
#Versi ini hanya untuk Linux

import os
import sys
import time

#warna-text
class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'



#intro
def intro() :
	os.system('clear')
	print(color.WARNING + "		==============================" + color.END)	
	print(color.RED + "		|----Welcome to This Tool----|    " + color.END)
	print(color.WARNING + "		==============================" + color.END)
	print(color.NOTICE + "	  Tool ini digunakan untuk perhitungan sederhana" + color.END)
	print("")
	print("")

	#menu/pilihan
	print(color.RED + '''[1]--Penjumlahan
[2]--Pengurangan
[3]--Perkalian
[4]--Pembagian''' + color.END)
	print("")
	print("")
	menu=raw_input(color.WARNING + "Masukan Nomor Menu Pilihan anda: " + color.END) 
	
	
	#Untuk Menu Penjumlahan
	def penjumlahan() :
		os.system('clear')
		print(color.WARNING + "		=======================================" + color.END)	
		print(color.RED + "		 Selamat Datang di Program Penjumlahan    " + color.END)
		print(color.WARNING + "		=======================================" + color.END)
		print("")
		print("")
		print("")
		aangka1=raw_input(color.WARNING + "Masukan Angka Pertama : " + color.END)
		aangka2=raw_input(color.WARNING + "Masukan Angka Kedua   : " + color.END)
		ahasil=int(aangka1)+int(aangka2)
		print("")
		print(color.RED + "------------------------------------------------" + color.END)
		print(color.WARNING + "	    	{} + {} = {}".format(aangka1,aangka2,ahasil) + color.END)		
		print(color.RED + "------------------------------------------------" + color.END)
		print("")
		print("")
		print(color.WARNING + "-Ketik 1 Untuk Mengulangi Program ini" + color.END)
		print(color.WARNING + "-Ketik 2 Untuk Kembali ke Menu Awal" + color.END)
		print("")
		asatudua=raw_input(color.WARNING + "Masukan Pilihan Anda: " + color.END)
		
		if asatudua == ('1'):
			penjumlahan()

		if asatudua == ('2'):
			intro()


	#Untuk Menu Pengurangan
	def pengurangan() :
		os.system('clear')
		print(color.WARNING + "		=======================================" + color.END)	
		print(color.RED + "		 Selamat Datang di Program Pengurangan    " + color.END)
		print(color.WARNING + "		=======================================" + color.END)
		print("")
		print("")
		print("")
		bangka1=raw_input(color.WARNING + "Masukan Angka Pertama : " + color.END)
		bangka2=raw_input(color.WARNING + "Masukan Angka Kedua   : " + color.END)
		bhasil=int(bangka1)-int(bangka2)
		print("")
		print(color.RED + "------------------------------------------------" + color.END)
		print(color.WARNING + "	    	{} - {} = {}".format(bangka1,bangka2,bhasil) + color.END)		
		print(color.RED + "------------------------------------------------" + color.END)
		print("")
		print("")
		print(color.WARNING + "-Ketik 1 Untuk Mengulangi Program ini" + color.END)
		print(color.WARNING + "-Ketik 2 Untuk Kembali ke Menu Awal" + color.END)
		print("")
		bsatudua=raw_input(color.WARNING + "Masukan Pilihan Anda: " + color.END)
		
		if bsatudua == ('1'):
			pengurangan()

		if bsatudua == ('2'):
			intro()



	#Untuk Menu Perkalian
	def perkalian() :
		os.system('clear')
		print(color.WARNING + "		=======================================" + color.END)	
		print(color.RED + "		 Selamat Datang di Program Perkalian    " + color.END)
		print(color.WARNING + "		=======================================" + color.END)
		print("")
		print("")
		print("")
		cangka1=raw_input(color.WARNING + "Masukan Angka Pertama : " + color.END)
		cangka2=raw_input(color.WARNING + "Masukan Angka Kedua   : " + color.END)
		chasil=int(cangka1)*int(cangka2)
		print("")
		print(color.RED + "------------------------------------------------" + color.END)
		print(color.WARNING + "	    	{} * {} = {}".format(cangka1,cangka2,chasil) + color.END)		
		print(color.RED + "------------------------------------------------" + color.END)
		print("")
		print("")
		print(color.WARNING + "-Ketik 1 Untuk Mengulangi Program ini" + color.END)
		print(color.WARNING + "-Ketik 2 Untuk Kembali ke Menu Awal" + color.END)
		print("")
		csatudua=raw_input(color.WARNING + "Masukan Pilihan Anda: " + color.END)
		
		if csatudua == ('1'):
			perkalian()

		if csatudua == ('2'):
			intro()

	#Untuk Menu Pembagian
	def pembagian() :
		os.system('clear')
		print(color.WARNING + "		=======================================" + color.END)	
		print(color.RED + "		 Selamat Datang di Program Pembagian    " + color.END)
		print(color.WARNING + "		=======================================" + color.END)
		print("")
		print("")
		print("")
		dangka1=raw_input(color.WARNING + "Masukan Angka Pertama : " + color.END)
		dangka2=raw_input(color.WARNING + "Masukan Angka Kedua   : " + color.END)
		dhasil=int(dangka1)/int(dangka2)
		print("")
		print(color.RED + "------------------------------------------------" + color.END)
		print(color.WARNING + "	    	{} / {} = {}".format(dangka1,dangka2,dhasil) + color.END)		
		print(color.RED + "------------------------------------------------" + color.END)
		print("")
		print("")
		print(color.WARNING + "-Ketik 1 Untuk Mengulangi Program ini" + color.END)
		print(color.WARNING + "-Ketik 2 Untuk Kembali ke Menu Awal" + color.END)
		print("")
		dsatudua=raw_input(color.WARNING + "Masukan Pilihan Anda: " + color.END)
		
		if dsatudua == ('1'):
			pembagian()

		if dsatudua == ('2'):
			intro()




	#pemilihan Nomor
	if menu == ('1'):
		penjumlahan()
	if menu == ('2'):
		pengurangan()
	if menu == ('3'):
		perkalian()
	if menu == ('4'):
		pembagian()
	else :
		print(color.RED + "Maaf, Nomor Yang Anda Masukan Tidak Ada Dalam Pilihan" + color.END)
		time.sleep(1.5)
		intro()
		
		

intro()


#---- SAlah-Menu Penjumlahan
#if menu == 1:
#    os.system('cls')
#    print("==============================")
#    print("Ini adalah Program Penjumlahan")
#    print("==============================")
#    print ("")
    
#    angka1=raw_input("Masukan Angka Pertama: ")
#    angka2=raw_input("Masukan Angka Kedua: ")
#    hasil=int(angka1)+int(angka2)
    
#    print("Hasilnya adalah: ", int(hasil))
#    print("")
#    print("")
#    satudua=raw_input("Ketik 1 untuk Mengulang Program ini dan Ketik 2 Untuk Kembali ke Menu awal: ")
