# -*- coding: utf-8 -*-

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
from selenium import webdriver
import urllib2, ssl , os 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
#from __future__ import print_function
import os
import sys
import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from lxml import html as lh
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#///////////////////////////////////////////////////////////////
global binary
global driver

#def f13():
binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary)
wait = WebDriverWait(driver, 20)


#query= "Server%3A+Apache-Coyote%2F1.1+Tomcat-5.5"
xpath= "//*[@type='submit']"

global num_lines
def logo():

	os.system("clear")
	print ("""
                      ███████╗ █████╗  ██████╗  ██████╗  ██████╗  ██╗
                      ╚══███╔╝██╔══██╗██╔════╝ ██╔═████╗██╔════╝ ███║
                        ███╔╝ ███████║██║  ███╗██║██╔██║██║  ███╗╚██║
                       ███╔╝  ██╔══██║██║   ██║████╔╝██║██║   ██║ ██║
                      ███████╗██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝ ██║
                      ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝  ╚═╝
                                                       """.center(20,'*'))
def banner():
	 print("")
	 print("")
	 print  bcolors.BOLD + bcolors.OKBLUE + "  [+]  SEARCH WORD      : "+bcolors.OKGREEN+var_key+ bcolors.ENDC
	 print  bcolors.BOLD + bcolors.OKBLUE + "  [+]  START PAGE       : "+bcolors.OKGREEN+str(var_page)+ bcolors.ENDC
	 print  bcolors.BOLD + bcolors.OKBLUE + "  [+]  SEARCH Country   : "+bcolors.OKGREEN+var_country+ bcolors.ENDC+bcolors.BOLD +""+bcolors.OKBLUE
	 sys.stdout.flush()

def centerify(text, width=-1):
  lines = text.split('\n')
  width = max(map(len, lines)) if width == -1 else width
  return '\n'.join(line.center(width) for line in lines)

def starting():
	
	try:
		global var_key
		var_key = sys.argv[1]
	except:
		t1=bcolors.BOLD +bcolors.FAIL+"\t\t\t\tYou Must Set Word To Search !!"+bcolors.WARNING+bcolors.BOLD +"\n \t\t\tExemple :"+bcolors.OKGREEN +" python "+sys.argv[0] +" rancher us 1\n"
		print (centerify(t1.center( 50 )))
		exit(1)
	try:
		global var_country
		var_country1 = sys.argv[2]
		var_country=var_country1.upper()

	except:
		t2=bcolors.BOLD +bcolors.FAIL+"\t\t\t\tYou Must Set Country !!"+bcolors.WARNING+bcolors.BOLD +"\n \t\t\tExemple :"+bcolors.OKGREEN +" python "+sys.argv[0] +" Wrod_search us 1\n"
		print  t2.center(20,'*')
		exit(1)
	try:
		global var_page
		var_page = sys.argv[3]
	except:
		var_page = int(1) 
		#print  var_page

	if not len(sys.argv[2])  == 2 :
		t3=bcolors.BOLD +bcolors.FAIL+"\t\t\t\tCountry Must be just 2 letters !!"+bcolors.WARNING+bcolors.BOLD +"\n \t\t\tExemple :"+bcolors.OKGREEN +" US = united stat , CA = canada\n"
	 	print  t3.center(20,'*')
	 	sys.exit (1)

	if len(sys.argv[1])  < 4 :
		t4= "\t\t\tWord Must Be greater than 4 letters\n "
	 	print  t4.center(20,'*')
	 	sys.exit (1)

	banner()
	global i
	global output_file
	i=int(var_page)
	#timestr = time.strftime("%Y%m%d-%H%M%S")
	timestr = time.strftime("%Y%m%d")
	output_file = "shodan-"+var_country+"-"+var_key+"-"+timestr+".txt"
	f= open(output_file,"w+")
	num_lines = sum(1 for line in open(output_file))
	


	#sys.stdout.write('Installing XXX... ')
	#print ("Starting Mozilla-Firefox")

def fire_up():
	#print "Starting Mozilla-Firefox",
	sys.stdout.write('  [+]  Start Browser    : ')
	sys.stdout.flush()
	#global binary
	#binary = FirefoxBinary('/opt/firefox/firefox-bin')

	try:

		#global driver
		#driver = webdriver.Firefox(firefox_binary=binary)
		#wait = WebDriverWait(driver, 190)
		print bcolors.OKGREEN+"OK"+bcolors.BOLD +""+bcolors.OKBLUE
		#driver.get("https://account.shodan.io/login")
	except:
		print bcolors.FAIL+"Fialed"
	#print  bcolors.BOLD +""+bcolors.OKBLUE+bcolors.BOLD +""+bcolors.OKBLUE
	#sys.stdout.write('  [+]  Try To Login   : ')
	#sys.stdout.flush()
	#try:
	#	driver.get("https://account.shodan.io/login")
	#	print bcolors.OKGREEN+"OK"+bcolors.BOLD +""+bcolors.OKBLUE
	#except:
	#	print bcolors.FAIL+"Fialed"+bcolors.BOLD +""+bcolors.OKBLUE
		
def check_exists_by_xpath(xpath):
	
    try:
    	driver.set_window_size(0, 0)
    	sys.stdout.write('  [+]  Check SHODAN     : ')
    	sys.stdout.flush()
    	driver.get("https://account.shodan.io/login")
        driver.find_element_by_xpath(xpath)
        print bcolors.OKGREEN+bcolors.BOLD+"OK"+bcolors.BOLD +bcolors.OKBLUE
    except NoSuchElementException:
    	print bcolors.OKGREEN+bcolors.BOLD+"Failed"+bcolors.BOLD +bcolors.OKBLUE
    	exit(0)
        #return False
    #return True

def submit_page():
    try:
        sys.stdout.write('  [+]  SUBMIT To Shodan : ')
        sys.stdout.flush()
        #print  bcolors.BOLD + bcolors.OKGREEN + "  [+]  SUBMIT "+ bcolors.ENDC
        username = driver.find_element_by_name('username')
        username.send_keys('zacr0w')
        password = driver.find_element_by_name('password')
        password.send_keys('agoon007')
        login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()
        time.sleep(3)
        print  bcolors.BOLD + bcolors.OKGREEN + "SUBMIT DONE "+ bcolors.ENDC
        
    except:
        print  bcolors.BOLD + bcolors.OKBLUE + "  [+]  SUBMIT FIELED "+ bcolors.ENDC
def check_login():

    try:

        sys.stdout.write('  [+]  Check Login      : ')
        sys.stdout.flush()
        search =  driver.find_element_by_name('login_submit')
        print  bcolors.BOLD + bcolors.OKGREEN + "PAGE OK"+bcolors.BOLD +bcolors.OKBLUE
        submit_page()
            # search =  driver.find_element_by_name('login_submit')
            # print bcolors.OKGREEN+bcolors.BOLD+"  [+]  PLEASE WAIT LOGIN"+ bcolors.ENDC        
    except:
        print bcolors.OKGREEN+bcolors.BOLD+"  [+]  NO8 CAPTCHA"+bcolors.BOLD +""+bcolors.OKBLUE
        pass

def search_query():

    try:
        #var_key_enc= urllib.quote_plus(var_key)
        print  bcolors.BOLD + bcolors.OKBLUE + "  [+]  SEARCH           : "+bcolors.OKGREEN+bcolors.BOLD+str(var_key)+" "+var_country+" "+var_page+bcolors.ENDC+bcolors.BOLD+ bcolors.OKBLUE 
        query="https://www.shodan.io/search?query="+var_key+"+country%3A%22"+var_country+"%22&page="+var_page  
        driver.get(query)
        time.sleep(3)
        #print "gggggggggggggggggggggggggg"
        resultat_total()

    except NoSuchElementException:
            print  bcolors.BOLD + bcolors.OKBLUE + " SEARCH ERROR "


def resultat_total():
	try:
		sys.stdout.write('  [+]  Results Total    :')
		sys.stdout.flush()
		SpecialPrice =driver.find_element_by_class_name('bignumber').text
		print bcolors.BOLD + bcolors.OKGREEN + (SpecialPrice)+ bcolors.ENDC

	except NoSuchElementException:
		print  bcolors.BOLD + bcolors.OKGREEN + " SEARCH ERROR "+bcolors.BOLD + bcolors.OKBLUE
		err()
		#exit(0)


def err():
	try:
		sys.stdout.write('  [+]  Check ERROR !!   : ')
		sys.stdout.flush()
		#time.sleep (3)
		ERR1 =driver.find_element_by_class_name('alert-info').text
		print bcolors.BOLD + bcolors.OKGREEN + (ERR1)+ bcolors.ENDC
	except NoSuchElementException:
		print "UNKNOWN ERROR"


	
def check_next():
	global i

	try:
		
		
		print bcolors.BOLD + '  [+]  Page Number !!!' + bcolors.OKGREEN + bcolors.BOLD+ ' [ ' + str(i) + ' ]' + bcolors.ENDC
		#sys.stdout.write('   [+]  Page Number !!! [ ' + str(var_page) + ' ] ')
		#sys.stdout.flush()
		i+= 1
		check_next2()
	except NoSuchElementException:
		return False
	return True

def check_next2():
	try:
		scrape_results(driver)
	        time.sleep(1)
	        sa_results()
	        time.sleep(1)
	        check_next_btn()
	        time.sleep(1)
	except NoSuchElementException:
		return False
		



def scrape_results(driver):
    # Xpath will find a subnode of h3, a[@href] specifies that we only want <a> nodes with
    #print bcolors.OKGREEN+bcolors.BOLD+"  [+]  PARSSING"+ bcolors.ENDC
    links = driver.find_elements_by_xpath("//*[@class='ip']/a[@href]")
    results = []
    for link in links:
        url = link.get_attribute('href')
        title_url = (url)
        results.append(title_url)          
    return results

def sa_results():
    print bcolors.BOLD + bcolors.FAIL + '  [+]  Parssing Urls !!!'+ bcolors.ENDC
    #print bcolors.BOLD + '  [+]  Page Number !!!' + bcolors.OKGREEN + bcolors.BOLD+ ' [ ' + str(i) + ' ]' + bcolors.ENDC
    all_results = []
    titles_urls = scrape_results(driver)
    for title in titles_urls:
        all_results.append(title)
    bad = ['www.shodan.io', 'def']
    for bbad in all_results:
        url = bbad
        for item in bad:
          if item in bbad:
               all_results.remove(bbad)   
    for result in all_results:
        url = result
        print '       [+]',url
        with open(output_file, 'a') as f:
             f.write(url + '\n')
    print bcolors.BOLD + bcolors.FAIL + '  [+]  Parssing Urls Done !!!'+ bcolors.BOLD + bcolors.OKBLUE 


def check_next_btn():

	sys.stdout.write('  [+]  Check Next      : ')
	sys.stdout.flush()
	try:
		driver.find_element_by_link_text('Next')
		print bcolors.OKGREEN+bcolors.BOLD+"NEXT FOUND "+ bcolors.ENDC
		driver.find_element_by_link_text('Next').click()
		time.sleep(3)
		check_next()


	except NoSuchElementException:
		print bcolors.OKGREEN+bcolors.BOLD+"END OF SEARCH"+ bcolors.ENDC
		rapport()
		#print_loop3()
		pass
		
		

def rapport():
	logo()
	count = len(open(output_file).readlines(  ))
	print  bcolors.BOLD + bcolors.OKBLUE +"  [+]  SEARCH   For  : "+bcolors.OKGREEN+bcolors.BOLD+str(var_key)+" "+var_country+" "+var_page+bcolors.ENDC
	print bcolors.BOLD + bcolors.OKBLUE + '  [+]  Results Found : '+bcolors.OKGREEN+bcolors.BOLD+str(count)+ bcolors.BOLD + bcolors.OKBLUE
	print bcolors.BOLD + bcolors.OKBLUE + '  [+]  output file   : '+bcolors.OKGREEN+bcolors.BOLD+output_file+ bcolors.BOLD + bcolors.OKBLUE
        #driver.close()
	#resultat_loop_1()
	eex()

        

###########################################################
###########################################################


def resultat_loop_1():
	#testsite_array = []
	print "ddddddddddddddddddd"
	global ccc
	ccc=0
	with open(output_file) as my_file:
		#my_file.split('\n')
		for line in my_file:
			#testsite_array.append(line)
			test_resultat(line)
			ccc+=1
###########################################################
###########################################################
###########################################################



def test_resultat(inputo):
	#link = "https://130.207.85.217/"
	link = inputo
	request = urllib2.Request(link)
	web_contenent = urllib2.urlopen(request, context=ssl._create_unverified_context())
	myfile = web_contenent.read()
	#sys.stdout.write(link)
	
	if 'containers' in myfile:
		#sys.stdout.write("[ "+str(num_lines)+' / '+str(ccc)+"  ] "+link)
		sys.stdout.write('link')
		sys.stdout.flush()
		#print link," OK"
	#else:
		#print (link+' No ')

###########################################################
def print_loop3():
	with open(output_file) as my_file:
		for line, name in enumerate(my_file, start=1):
			try:
				request = urllib2.Request(name)
				web_contenent = urllib2.urlopen(request, context=ssl._create_unverified_context())
				recived = web_contenent.read()
				if 'containers' in recived:
					print ' [', str(num_lines)+' /',line ,'] ',name.rstrip('\n')
			except:
				pass
def eex():
	print bcolors.BOLD + bcolors.FAIL+ " \n\n\t\t         EXITING .... "
	driver.close()
	exit(1)




def ma():
	try:
		logo()
		try:
			#f13()
			starting()
			#f13()
			pass
		except:
			print bcolors.BOLD + bcolors.WARNING+ "Starting Error "
			print bcolors.BOLD + bcolors.WARNING+ " \n\n\t\t Check Y0UR Starting  "
		try:
			fire_up()
		except:
			print bcolors.BOLD + bcolors.WARNING+ "Firefox Error "
			print bcolors.BOLD + bcolors.WARNING+ " \n\n\t\t Check Y0UR Firefox"
		
		try:
			check_exists_by_xpath(xpath)
			pass
		except :
			print bcolors.BOLD + bcolors.WARNING+ "Network Connetion Error "
			print bcolors.BOLD + bcolors.WARNING+ " \n\n\t\t Check Y0UR 2  Connetion "
			eex()
		try:
			check_login()
		except:
			print bcolors.BOLD + bcolors.WARNING+ " Network Connetion Error "
			print bcolors.BOLD + bcolors.WARNING+ " Login  Error "
			eex()
		try:
			search_query()
			pass
			check_next()
		except:
			print bcolors.BOLD + bcolors.WARNING+ " search_query() "
			print bcolors.BOLD + bcolors.WARNING+ " search_query() "
			eex()
	except:
		print bcolors.BOLD + bcolors.WARNING+ ""
   
    




ma()
#try:
#	check_exists_by_xpath(xpath)
#	try:
#		connextion_check()
#	except :
#		print bcolors.BOLD + bcolors.WARNING+ " \t\t Check Y0UR  check_login "
#except :
#	print bcolors.BOLD + bcolors.WARNING+ " Network Connetion Error "
#	print bcolors.BOLD + bcolors.WARNING+ " \t\t Check Y0UR  Connetion "

#	driver.close()
#	exit(0)
def connextion_check():
	print "c1"
	try:
		check_login()
		pass
	except :
		print bcolors.BOLD + bcolors.WARNING+ " \t\t Check Y0UR  check_login "


#search_query()
#check_next()
#resultat_loop_1()
