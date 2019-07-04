#!/usr/bin/env python
import re
import urllib
from headers import *
from vulnz import *

print ga.green+'''

                  _____ _   _ __  __    _    _   _
                 |_   _| | | |  \/  |  / \  | \ | |
                   | | | | | | |\/| | / _ \ |  \| |
                   | | | |_| | |  | |/ ___ \| |\  |
                   |_|  \___/|_|  |_/_/   \_\_| \_|

        ##############################################################
        #|  Tools Ini Adalah Tools Security Scanner                  #
        #|  By Tuman                                                 #
        #|  Tools Ini Supports Remote Code/Command Execution XSS     #
        #|  dan SQL Injection.                                       #
	#|  Thanks To @Naruto-Kun @Notthing @Fauzan @Tayo @Mr.Z33    #
	#|            @Mr.Ozzak @Thereshome @Xclown                  #
        ##############################################################
        '''+ga.end

def urls_or_list():
	url_or_list = raw_input(" [!] Apakah Tuman Gans?: ")
	if url_or_list == "woiya jelas":

	 	 url = raw_input(" [!] Masukkan URL: ")
		 #if not url.startswith("http://"):
		     #Thanks to N.P.T Team
                     #print ga.red+'''\n URL SALAH ASU CONTOH : \"http://\" \n'''+ga.end
                     #exit()
		 if "?" in url:
		 	rce_func(url)
		 	xss_func(url)
		 	error_based_sqli_func(url)
		 else:
			print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" URL Tidak Valid Asu"+ga.end			
			print ga.red +" [Warning] Masukkan URL Lengkap Kayak Gini Goblok  http://site.com/page.php?id=value \n"+ ga.end
			exit()

urls_or_list()



