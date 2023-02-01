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
mengetik(colored(">> Halo, selamat datang di program kami","green"))
mengetik(colored(">> Selamat menggunakan!","green"))

os.system("clear")

# Mencetak banner dengan teks "IPAS"

pilihan = "y"
while  pilihan == "y":
	banner = pyfiglet.figlet_format("          IPAS")
	print(banner)
	print(colored("\t ~ Semoga Bisa Membantu ~ ","cyan"))
	print("\n>> Silahkan pilih rumus yang akan digunakan!\n")
	print("[1] Energi Kinetik")
	print("[2] Energi Potensial")
	print("[3] Hubungan Usaha Dengan Energi Kinetik")
	print("[4] Hubungan Usaha Dengan Energi Potensial")
	print("[5] Hukum Kekekalan Energi")
	print("[6] Kalor")
	print("[7] Program Konversi Temperatur")
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
		mengetik(">> Kalor\n")
		print("[1] Rumus Kalor Jenis")
		print("[2] Azas Black\n")
		kalor = int(input("Pilih Nomer: "))
		os.system("clear")

		if kalor == 1:
			mengetik(">> Menentukan Kalor Jenis")
			print(colored('''
Rumus Kalor Jenis Q = m . c . 𝚫T

Dengan

Q   : Kalor (J)
m   : Massa benda (kg)
c   : Kalor jenis (J/kg°C)
∆T  : Perubahan suhu (°C)
			''',"green"))
			m = float(input("Dik : m = "))
			q = float(input("    : Q = "))
			t1 = float(input("    :∆T = T1 = "))
			t2 = float(input("          T2 = "))
			mengetik("Dit : c =...?")
			mengetik("Jwb : c = Q/m.∆T")
			mengetik("      c = "+ str(q)+" J / "+str(m)+" kg × "+str(t2-t1)+" °C")
			t2t1 = t2-t1
			mengetik("      c = "+str(q)+" J / "+str(m*t2t1)+" °C")
			mtt = m*t2t1
			mengetik("      c = "+str(q/mtt)+" J/kg°c\n")
			lan = input("Apakah anda ingin menentukan kapasitas kalornya y/n = ")
			os.system("clear")
			if lan == "y":
				mengetik(">> Menetukan Kapasitas Kalor")
				print(colored('''
Untuk menghitung kapasitas kalor kita gunakan rumus 

C = m . c
''',"green"))
				m = float(input("Dik : m = "))
				c = float(input("    : c = "))
				mengetik("Dit : C = ...?")
				mengetik("Jwb : C = m . c")
				mengetik("      C = "+str(m)+" kg x "+str(c)+" J/kg°C")
				mengetik("      C = "+str(m*c)+" J/°C\n")
				pilihan = input(" Apakah anda ingin menggunakan rumus yang lainnya y/n = ")
				os.system("clear")
			
		elif kalor == 2:
			mengetik(">> Azas Black\n")
			m1 = float(input("Dik : m1 = "))
			t1 = float(input("      T1 = "))
			t2 = float(input("      T2 = "))
			tc = float(input("      Tc = "))
			c1 = float(input("      c1 = "))
			c2 = float(input("      c2 = "))
			mengetik("\nDit : m2 = ...?\n")
			mengetik("Jwb : Qlepas = Qterima")
			mengetik("      m2c2∆T2 = m1c1∆T1")
			mengetik("      m2 x "+str(c2)+" x (T2 - Tc) = "+ str(m1)+" x "+str(c1)+" x (Tc - T1)")
			mengetik("      m2 x "+str(c2)+" x ("+str(t2)+" - "+str(tc)+") = "+str(m1)+" x "+str(c1)+" x ("+str(tc)+" - ("+str(t1)+"))")
			mengetik("      m2 x "+str(c2*(t2-tc))+" = "+str(m1*c1*(tc-t1)))
			has1 = c2*(t2-tc)
			has2 = m1*c1*(tc-(t1))
			mengetik("      m2 = "+str(has2/has1)+"\n")
			mengetik(colored("Semoga bisa membantu!","green"))
			pilihan = input(colored("\nApakah anda ingin menggunakan \nrumus yang lainnya y/n = ","green"))
			os.system("clear")

			
		else:
			mengetik(colored("Error : Inputkan angka yang benar...\n","red"))

	elif pilih == 1:
		mengetik(">> Energi Kinetik ")
		print(colored('''
Rumus energi kinetik Ek = 1/2 m.v2

Keterangan:
		
Ek = Energi kinetik (J)
m = Massa benda (kg)
v = Kecepatan atau laju benda (m/s)
		
		''',"green"))
		m = float(input("Dik:  M = "))
		v = float(input("      V =  "))
		mengetik("Dit: Ek = ...?")
		mengetik("Jwb: Ek = ½mv²")
		mengetik("        = ½ x "+str(m)+" kg x ("+str(v)+")² m/s")
		a = 1/2*m
		b = v**2
		mengetik(" 	= "+str(a)+" x ("+str(b)+")")
		c = a * b
		mengetik("        = "+str(c)+" J\n")
		mengetik(colored("Semoga bisa membantu!","green"))
		pilihan = input("\nApakah anda ingin menggunakan rumus yang lainnya y/n = ")
		os.system("clear")
	
		
	elif pilih == 2:
		mengetik(">> Energi Potensial")
		print(colored('''
Rumus energi potensial EP = m . g . h

Keterangan:
		
EP = Energi potensial (J)
m = Massa benda (kg)
h = Ketinggian benda (m)
g = Gravitasi (m/s²)

		''',"green"))

		m = float(input("Dik:  M = "))
		g = float(input("      G = "))
		h = float(input("      H = "))
		mengetik("Dit: Ep = ...?")
		mengetik("Jwb: Ep = m.g.h")
		mengetik("        = "+str(m)+" kg x "+str(g)+" m/s² x "+str(h)+" m")
		ep = m*g*h
		mengetik("        = "+str(ep)+" J\n")
		mengetik("Semoga bisa membantu!\n")
		pilihan = input(" Apakah anda ingin menggunakan rumus yang lainnya y/n = ")
		os.system("clear")
	    	    
	elif pilih == 4:
		mengetik(">> Hubungan Usaha Dengan Energi Potensial\n")
		m = float(input("Dik:  M = "))
		g = float(input("      G = "))
		h1 = float(input("     H1 = "))
		h2 = float(input("     H2 = "))
		mengetik("Dit: W = ...?")
		mengetik("Jwb: W = m.g.(h2-h1)")
		mengetik("     W = "+str(m)+" x "+str(g)+" x ( "+str(h2)+" - "+str(h1)+" )")
		mg = m*g
		h2_h1 = h2 - h1
		mengetik("     W = "+str(mg)+" x ( "+str(h2_h1)+" )")
		w = mg*h2_h1
		mengetik("     W = "+str(w)+" J\n")
		mengetik("Semoga bisa membantu!\n")
		pilihan = input(" Apakah anda ingin menggunakan rumus yang lainnya y/n = ")
		os.system("clear")
	    
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
		mengetik("     V2² = √"+str(c))
		hasil = c**(1/2)
		mengetik("     V2  = "+str(hasil)+" m/s\n")
		mengetik("Semoga bisa membantu!\n")
		pilihan = input(" Apakah anda ingin menggunakan rumus yang lainnya y/n = ")
		os.system("clear")
		
	if pilih == 7 :
		print("PROGRAM KONVERSI TEMPERATUR\n")
		print("[1] Suhu dalam celcius")
		print("[2] Suhu dalam kelvin")
		print("[3] Suhu dalam fahrenheit")
		print("[4] Suhu dalam reamur\n")
		konversi = int(input("Pilih Nomer: "))
		if konversi == 1 :
			celcius = float(input("\nMasukan suhu dalam celcius = "))
			print("")
			print(colored("Suhu dalam kelvin","green"))
			kelvin = 273 + celcius
			print(celcius,"°C =",kelvin,"°K")
			print("T °K = 273 + T °C")
			print("     = 273 + ",celcius)
			print("     =",kelvin,"°K \n")
			
			print(colored("Suhu dalam fahrenheit","green"))
			fahrenheit = (9/5 * celcius) + 32
			print(celcius,"°C =",fahrenheit,"°F")
			print("T °F = (9/5 * T °C) + 32")
			print("     = (9/5 *",celcius,") + 32")
			fah = (9/5 * celcius)
			print("     =",fah,"+ 32")
			print("     =",fahrenheit,"°F\n")
			
			print(colored("Suhu dalam reamur ","green"))
			reamur = 4/5 * celcius
			print(celcius,"°C =",reamur,"°R")
			print("T °R = 4/5 * T °C")
			print("     = 4/5 *",celcius)
			print("     =",reamur,"°R")

			pilihan = input(colored("\nApakah anda ingin menggunakan \nrumus yang lainnya y/n = ","green"))
			os.system("clear")

			
		elif konversi == 2 :
			  kelvin = float(input("\nMasukan suhu dalam kelvin = "))
			  print("")
			  celcius = kelvin - 273
			  print(kelvin,"°K =",celcius,"C")
			  print("T °C = T °K - 273")
			  print("     =",kelvin,"- 273")
			  print("     =",celcius,"°K \n")
			   
			  fahrenheit = (9/5 * celcius) + 32
			  print(celcius,"°C =",fahrenheit,"°F")
			  print("T °F = (9/5 * T °C) + 32")
			  print("     = (9/5 *",celcius,") + 32")
			  fah = 9/5 * celcius
			  print("     = ",fah,"+ 32")
			  print("     =",fahrenheit,"°F\n")
			  
			  reamur = 4/5 * celcius
			  print(celcius,"°C =",reamur,"°R")
			  print("T °R = 4/5 * T °C")
			  print("     = 4/5 *",celcius)
			  print("     =",reamur,"°R")
			  pilihan = input(colored("\nApakah anda ingin menggunakan \nrumus yang lainnya y/n = ","green"))
			  os.system("clear")

	
		elif konversi == 3 :
		    fahrenheit = float(input("\nMasukan suhu dalam fahrenheit = "))
		    print("")
		    celcius = 5/9 * (fahrenheit - 32)
		    print(fahrenheit,"°F =",celcius,"°C")
		    print("T °C = 5/9 * (T °F - 32)")
		    print("     = 5/9 * (",fahrenheit,"- 32)")
		    fah = fahrenheit - 32
		    print("     = 5/9 *",fah)
		    print("     =",celcius,"°C \n")
		
		    kelvin = 273 + celcius
		    print(celcius,"°C =",kelvin,"°K")
		    print("T °K = 273 + T °C")
		    print("     = 273 +",celcius)
		    print("     =",kelvin,"°K \n")
		
		    reamur = 4/5 * celcius
		    print(celcius,"°C =",reamur,"°R")
		    print("T °R = 4/5 * T °C")
		    print("     = 4/5 *",celcius)
		    print("     =",reamur,"°R")
		    pilihan = input(colored("\nApakah anda ingin menggunakan \nrumus yang lainnya y/n = ","green"))
		    os.system("clear")

	
		elif konversi == 4 :
		        reamur = float(input("\nMasukan suhu dalam reamur = "))
		        print("")
		        celcius = 5/4 * reamur
		        print(reamur,"°R =",celcius,"°C")
		        print("T °C = 5/4 * T °R")
		        print("     = 5/4 *",reamur)
		        print("     =",celcius,"°C \n")
		
		        kelvin = 273 + celcius
		        print(celcius,"°C =",kelvin,"°K")
		        print("T °K = 272 + T °C")
		        print("     = 273 +",celcius)
		        print("     =",kelvin,"°K\n")
		
		        fahrenheit = (9/5 * celcius) + 32
		        print(celcius,"°C =",fahrenheit,"°F")
		        print("T °F = (9/5 * T °C) + 32")
		        print("     = (9/5 *",celcius,") + 32")
		        fah = 9/5 * celcius
		        print("     =",fah,"+ 32")
		        print("     =",fahrenheit,"°F")
		        pilihan = input(colored("\nApakah anda ingin menggunakan \nrumus yang lainnya y/n = ","green"))
		        os.system("clear")


		else:
			mengetik(colored("Error : Inputkan angka yang benar...\n","red"))

	elif pilih == 0:
		mengetik(colored("Terima kasih telah menggunakan programnya. Semoga hari Anda menyenangkan! \n ","green"))
		break
		
		
	else:
	    mengetik(colored("Error : Inputkan angka yang benar...\n","red"))
	    
	    
	    
			
