from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep 
import os
import re
import urllib
from selenium.webdriver.common.keys import Keys
from Dialog_Error import *
from Dialog_Notification import *
from Dialog_Search import *

# ----------------------------------------------------------------- FASE 1 ----------------------------------------------------------------- #
def kamui(usr, pwd, url, filename, instancia):
	#chrome_options = webdriver.ChromeOptions()
	#chrome_options.add_argument("--headless")

	if os.path.isdir('IDs') == False:
		os.mkdir(str(os.getcwd()+'/IDs'))

	def verify(url):
		regx_verify = r"(^[0-9]{4,20})"
		matcher = re.search(regx_verify, url)
		if matcher != None:
			print(matcher.group())
			return True
		else:
			print('======= IS A NAME ! =======')
			return False

	isnumber = verify(url)

	driver = webdriver.Chrome(executable_path=(str(os.getcwd())+"/chromedriver")) # , chrome_options=chrome_options
	driver.get('https://www.facebook.com/') 
	sleep(1)
	try:
		try:
			print('Trying connection... (METHOD = ID)')
			driver.find_element_by_id('email').send_keys(usr)
			sleep(0.4)
			driver.find_element_by_id('pass').send_keys(pwd)
			sleep(0.6)
			driver.find_element_by_id('loginbutton').click()
		except Exception:
			print('Trying connection... (METHOD = XPATH+ID)')
		try:
			driver.find_element_by_xpath('//*[@id="email"]').send_keys(usr)
			sleep(0.7)
			driver.find_element_by_xpath('//*[@id="pass"]').send_keys(pwd)
			sleep(0.4)
			driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
		except Exception:
			print('Trying connection... (METHOD = XPATH+NAME)')
		try:
			driver.find_element_by_xpath('//*[@name="email"]').send_keys(usr)
			sleep(0.7)
			driver.find_element_by_xpath('//*[@name="pass"]').send_keys(pwd)
			sleep(0.4)
			driver.find_element_by_xpath('//*[@name="login"]').click()
		except Exception:
			pass
	except Exception:
		driver.close()
		instancia.dialogError('[!] Connection failed: The connection methods have failed, you can try again.')
	# ----------------------------------------------------------------- FASE 2 ----------------------------------------------------------------- #
	def catch_html(links, codes, names): # Download HTML
		try:
			driver.get(links)
			content_element = driver.find_element_by_class_name(codes) # Nombre de la clase padre (en el ejemplo, la clase padre ABSOLUTA de un fb)
			content_html = content_element.get_attribute("innerHTML") # Conseguimos la info luego de que el contenido es generado por JavaScript
			soup = BeautifulSoup(content_html, "html.parser")
			p_tags = soup.find_all("div") # Tag of the son (Ej: <a/> ) to find.		
			if os.path.isdir('IDs/'+str(url)) == False: # Start process of HTML Downloading...
				os.mkdir(str(os.getcwd()+'/IDs/'+str(url)))
			for p in p_tags:
				file_ = open(str(os.getcwd()+'/IDs/'+str(url)+'/')+names, "a+")
				file_.write(str(p))
				file_.close()
		except Exception:
			instancia.dialogError('[!] System error: Error downloading the HTML: {}.'.format(names))

# ----------------------------------------------------------------- FASE 2.5 ----------------------------------------------------------------- #
	href = []
	links = []
	if os.path.isdir('Searcher') == False:
		os.mkdir('Searcher')

	#driver.find_element_by_xpath('//input[@role="search"]').click()	
	driver.find_element_by_xpath('//input[@placeholder="Buscar"]').send_keys(url)
	driver.find_element_by_xpath('//button[@data-testid="facebar_search_button"]').send_keys(Keys.ENTER)
	sleep(4)
	result = driver.find_element_by_xpath('//div[@class="_6rbb"]').text
	images = driver.find_elements_by_xpath('//img[@class="_6xu4 _6xu5 img"]')
	profiles = driver.find_elements_by_xpath('//div[@class="_6v_0 _4ik4 _4ik5"]/a')
	print(result,'\n')
	for i, image in enumerate(images):
		src = image.get_attribute('src')
		urllib.request.urlretrieve(src, "Searcher/perfil_{}.jpg".format(i))
		print(src,'\n')
	for profile in profiles:
		href.append(profile.get_attribute('href'))
		print(href,'\n')

	return result, href
	instancia.search(result, href)

	links.append(open('link.txt', 'r').read())
	print('====================Funciona')