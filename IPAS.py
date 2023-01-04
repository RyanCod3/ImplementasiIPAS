import pyfiglet
import os
import sys
import time
from termcolor import colored

os.system("clear")

def mengetik(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		# Kecepatan mengetik
		time.sleep(0.1)
		
mengetik(colored(">> Halo, selamat datang di program kami\n","green"))
mengetik(colored(">> Mohon maaf bila ada kekurangan dalam programnya.\n","green"))

def loding(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		# Kecepatan mengetik
		time.sleep(0.2)
loding(colored(">> Loding...","green"))

os.system("clear")

# Mencetak banner dengan teks "IPAS"
banner = pyfiglet.figlet_format("          IPAS")
print(banner)
print(colored("\t ~ Semoga Bisa Membantu ~ ","cyan"))

while True:
	print("\n>> Silahkan pilih rumus yang akan digunakan!\n")
	print("[1] Energi Kinetik")
	print("[2] Energi Potensial")
	print("[3] Hubungan Usaha Dengan Energi Kinetik")
	print("[4] Hubungan Usaha Dengan Energi Potensial")
	print("[5] Hukum Kekekalan Energi")
	print("[6] Kumpulan Program Konversi")
	print("[0] Keluar Program\n")
	pilih = int(input("Pilih Nomor: "))
	os.system("clear")
	if pilih == 3:
		mengetik(">>> Hubungan Usaha Dengan Energi Kinetik \n")
		print("Silahkan pilih akan menghitung apa!\n")
		print("[1] Menghitung Usaha(W)")
		print("[2] Menghitung Jarak(S)")
		print("[3] Menghitung Gaya (F)\n")
		p = int(input("Pilih Nomor: "))
		os.system("clear")
		
		if p == 1:
			mengetik(">>> Hubungan Usaha Dengan Energi Kinetik \n")
			mengetik(">> Menghitung Usaha(W) \n")
			m = float(input("Dik:  M: "))
			v1 = float(input("     V1: "))
			v2 = float(input("     V2: "))
			mengetik("Dit: W = ...?")
			mengetik("jwb: W = ½mv2² - ½mv1²")
			mengetik("     W = ½ x "+str(m)+" x ( "+str(v2)+" )² - ½ x "+str(m)+" x ( "+str(v1)+" )²")
			v22 = v2**2
			v12 = v1**2
			mengetik("     W = ½ x "+str(m)+" x ( "+str(v22)+" ) - ½ x "+str(m)+" x ( "+str(v12)+" )")
			ek2 = 1/2*m*(v22)
			ek1 = 1/2*m*(v12)
			mengetik("     W = "+str(ek2)+" - "+str(ek1))
			jumlah = ek2 - ek1
			mengetik("     W = "+str(jumlah)+" J\n")
			
		elif p == 2:
			mengetik(">>> Hubungan Usaha Dengan Energi Kinetik \n")
			mengetik(">> Menghitung Jarak(S)\n")
			m = float(input("Dik:  M: "))
			v1 = float(input("     V1: "))
			v2 = float(input("     V2: "))
			f = float(input("      F: "))
			mengetik("Dit: S = ...?")
			mengetik("jwb: S = ½mv2² - ½mv1² / f ")
			v22 = v2**2
			v12 = v1**2
			mengetik("     S = ½ x "+str(m)+" x ( "+str(v22)+" ) - ½ x "+str(m)+" x ( "+str(v12)+" ) / "+str(f))
			ek2 = 1/2*m*(v22)
			ek1 = 1/2*m*(v12)
			mengetik("     S = "+str(ek2)+" - "+str(ek1)+" / "+str(f))
			ek2_ek1 = ek2 - ek1 
			mengetik("     S = "+str(ek2_ek1)+" / "+str(f))
			jumlah = ek2_ek1 / f
			mengetik("     S = "+str(jumlah)+" M\n")
			
			
		elif p == 3:
			print(">>> Hubungan Usaha Dengan Energi Kinetik |\n")
			print(">> Menghitung Gaya(F)\n")
			m = float(input("Dik:  M: "))
			v1 = float(input("     V1: "))
			v2 = float(input("     V2: "))
			s = float(input("      S: "))
			print("Dit: F = ...?")
			print("jwb: F = ½mv2² - ½mv1² / s ")
			print("     F = ½",m,"x (",v2**2,") - ½ x",m,"x (",v1**2,")","/",s)
			print("     F =",1/2*m*(v2**2),"-",1/2*m*(v1**2),"/",s)
			print("     F =",1/2*m*(v2**2)-1/2*m*(v1**2),"/",s)
			print("     F =",(1/2*m*(v2**2)-1/2*m*(v1**2))/s,"N \n")
		 	   
		else:
		 	   mengetik(colored("Error : Inputkan angka yang benar...\n","red"))
 
	if pilih == 6:
		mengetik(">> Kumpulan Program Konversi")
		print("[1] Konversi km/jam ke m/s")
		print("[2] Konversi g ke kg\n")
		konver = int(input("Pilih Nomer: "))
		os.system("clear")
		if konver == 1:
			mengetik(">> Konversi km/jam ke m/s\n")
			km = float(input("Masukan nilai km/jam : "))
			hitung = km * 1000 / 3600
			
			mengetik("Jadi konversi "+str(km)+" km/jam ke m/s adalah  "+str(hitung)+" m/s")
		elif konver == 2:
			mengetik(">> Konversi g ke kg\n")
			g = float(input("Masukan Nilai g : "))
			kg = g / 1000
			mengetik("Jadi "+str(g)+" gram ke kilogram adalah "+str(kg)+" kg")
 			   
		else:
			mengetik(colored("Error : Inputkan angka yang benar...\n","red"))
		 	   
		 	   
	elif pilih == 1:
		mengetik(">> Energi Kinetik \n")
		mengetik("di mana: ")
		mengetik("• Ek adalah energi kinetik, satuan Joule (J) ")
		mengetik("• m adalah masa benda, satuan kilogram (kg)")
		mengetik("• v adalah kecepatan benda, satuan meter per detik (m/s)\n")
		mengetik("Silahkan konversikan terlebih dahulu jika ada yang harus di konversikan\n")
		m = float(input("Dik:  M: "))
		v = float(input("      V: "))
		mengetik("Dit: Ek = ...?")
		mengetik("Jwb: Ek = ½mv²")
		mengetik("        = ½ x "+str(m)+"kg x ("+str(v)+")² m/s")
		a = 1/2*m
		b = v**2
		mengetik(" 	= "+str(a)+"x ("+str(b)+")")
		c = a * b
		mengetik("        = "+str(c)+" J\n")
		speaker("Semoga bisa membantu")
		mengetik("Semoga bisa membantu")
	
		
	elif pilih == 2:
		mengetik(">> Energi Potensial\n")
		m = float(input("Dik:  M: "))
		g = float(input("      G: "))
		h = float(input("      H: "))
		mengetik("Dit: Ep = ...?")
		mengetik("Jwb: Ep = m.g.h")
		mengetik("        = "+str(m)+" x "+str(g)+" x "+str(h))
		ep = m*g*h
		mengetik("        = "+str(ep)+" J\n")
	    
	elif pilih == 4:
		mengetik(">> Hubungan Usaha Dengan Energi Potensial\n")
		m = float(input("Dik:  M: "))
		g = float(input("      G: "))
		h1 = float(input("     H1: "))
		h2 = float(input("     H2: "))
		mengetik("Dit: W = ...?")
		mengetik("Jwb: W = m.g.(h2-h1)")
		mengetik("     W = "+str(m)+" x "+str(g)+" x ( "+str(h2)+" - "+str(h1)+" )")
		mg = m*g
		h2_h1 = h2 - h1
		mengetik("     W = "+str(mg)+" x ( "+str(h2_h1)+" )")
		w = mg*h2_h1
		mengetik("     W = "+str(w)+" J\n")
	    
	elif pilih == 5:	
		mengetik(">> Hukum Kekekalan Energi\n")
		m = float(input("Dik:  M: "))
		g = float(input("      G: "))
		v1 = float(input("     V1: "))
		h1 = float(input("     H1: "))
		h2 = float(input("     H2: "))
		mengetik("Dit: V2 = ...?")
		mengetik("Jwb: EM1 = EM2")
		mengetik("     EP1 + EK1 = EP2 + EK2")
		mengetik("     mgh1 + ½mv1² = mgh2 + ½mv2²")
		mengetik("     "+str(m)+" x "+str(g)+" x "+str(h1)+" + ½ x "+str(m)+" x ("+str(v1)+")² = "+str(m)+" x "+str(g)+" x "+str(h2)+" + ½ x "+str(m)+" x v2²")
		mgh1 = m*g*h1
		mv1 = 1/2*m*v1**2
		mgh2 = m*g*h2
		m2 = 1/2*m
		mengetik("     "+str(mgh1)+" + "+str(mv1)+" = "+str(mgh2)+" + "+str(m2)+" v2²")
		mengetik("     "+str(mgh1)+" - "+str(mgh2)+" = "+str(m2)+" v2²")
		mgh1_mgh2 = m*g*h1 - m*g*h2
		mengetik("     "+str(mgh1_mgh2)+" / "+str(m2))
		a = m*g*h1 - m*g*h2
		b = 1/2*m
		c = a/b
		mengetik("     V2² = "+str(c))
		hasil = c**(1/2)
		mengetik("     V2  = "+str(hasil)+" m/s\n")

	elif pilih == 0:
		mengetik(colored("Terima kasih telah menggunakan programnya. Semoga hari Anda menyenangkan! \n ","green"))
		break
		
		
	else:
	    mengetik(colored("Error : Inputkan angka yang benar...\n","red"))
	    
	    
	    
			
