#!usr/bin/env python

import os
import py_compile
os.system("apt-get insatall figlet")
os.system("clear")
os.system("figlet Derleme Araci")
print("""	
		Derleme Aracina Hosgeldiniz..!
						""")
derle=raw_input("Program Ismini Giriniz : ")
py_compile.compile(derle)
