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
def izanami(usr, pwd, url, filename, instancia):
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
		except Exception as err:
			print(err)

# ----------------------------------------------------------------- FASE 2.5 ----------------------------------------------------------------- #
	href = []
	links = []
	texts_results = []
	if os.path.isdir('Searcher') == False:
		os.mkdir('Searcher')
	if isnumber == True:
		links.append("https://www.facebook.com/profile.php?id="+url)
	else:
		#driver.find_element_by_xpath('//input[@role="search"]').click()	
		driver.find_element_by_xpath('//input[@placeholder="Buscar"]').send_keys(url)
		driver.find_element_by_xpath('//button[@data-testid="facebar_search_button"]').send_keys(Keys.ENTER)
		sleep(4)
		results = driver.find_elements_by_xpath('//div[@class="_6v_9"]')
		images = driver.find_elements_by_xpath('//img[@class="_6xu4 _6xu5 img"]')
		profiles = driver.find_elements_by_xpath('//div[@class="_6v_0 _4ik4 _4ik5"]/a')

		for result in results:
			print(result.text,'\n')
			text_result = result.text
			texts_results.append(text_result)
		for i, image in enumerate(images):
			src = image.get_attribute('src')
			urllib.request.urlretrieve(src, "Searcher/perfil_{}.jpg".format(i))
			print(src,'\n')

		for profile in profiles:
			href.append(profile.get_attribute('href'))
			print(href,'\n')

		instancia.search(texts_results, href)

		links.append(open('link.txt', 'r').read())
		print('====================Funciona')
		

# ============================================================================================================================================== #


	codes = ["_4lh.timelineLayout.noFooter.fbx._-kb._605a.j_1_vx5xcrw.chrome.webkit.x1.Locale_es_LA","_4lh.timelineLayout.noFooter.fbx._-kb._605a.j_1_vx5xcrw.chrome.webkit.x1.Locale_es_LA.cores-gte4.hasAXNavMenubar._19_u","_4lh.timelineLayout.noFooter.fbx._-kb._605a.j_1_vx5xcrw.chrome.webkit.x1.Locale_es_LA.cores-gte4.hasAXNavMenubar._19_u","_4__a.fbx._-kb._605a.j_1_vx5xcrw.chrome.webkit.x1.Locale_es_LA.cores-gte4._19_u.hasAXNavMenubar"]
	names = [filename,filename.replace(".html","_info.html"),filename.replace(".html","_friends.html"),filename.replace(".html","_react.html")]
	catch_html(links[0], codes[0], names[0])
		
	if os.path.isfile("sessions.txt") == False:	 # Register the new entrys for izanagi use
		sessions = open('sessions.txt', "w")
		sessions.write('1# ID '+str(filename.replace(".html",""))+': '+str(url)+'\n')
		sessions.close()
	else:
		sessions = open('sessions.txt', "r")
		num_id = sessions.readlines()[-1].split('#')[0]
		sessions.close()
		num_id = int(num_id)+1
		sessions = open('sessions.txt', "a+")
		sessions.write(str(num_id)+'# ID '+str(filename.replace(".html",""))+': '+str(url)+'\n')
		sessions.close()
	# ----------------------------------------------------------------- FASE 3 ----------------------------------------------------------------- #
	categ = ['photos','videos','map','sports','music','movies','tv','books','games','likes','events','did_you_know','reviews','group','notes','app_instapp']
	file_3 = open('IDs/'+str(url)+'/'+filename, "r")
	data_3 = file_3.read()
	getdata = data_3.find("Información")
	info1 = data_3[getdata-200:getdata-2].split('href="')[1].replace('amp;', '')
	links.append(info1)

	file_3 = open('IDs/'+str(url)+'/'+filename, "r")
	data_3 = file_3.read()
	getdata = data_3.find("pb_friends_tl")
	info2 = data_3[getdata-200:getdata+13].split('href="')[1]
	links.append(info2)

	file_3 = open('IDs/'+str(url)+'/'+filename, "r")
	data_3 = file_3.read()
	getdata = data_3.find('/ufi/reaction/profile/browser/?ft_ent_identifier=')
	info3 = "https://www.facebook.com/"+data_3[getdata:getdata+500].split('"')[0]
	links.append(info3)
	# ----------------------------------------------------------------- FASE 4 ----------------------------------------------------------------- #
	L = 1
	C = 1
	N = 1
	CA = 0
	for i in range(1,20):
		try:
			if CA < 16:
				links.append(info1.replace('about', categ[CA]))
				names.append(filename.replace(".html","_")+categ[CA]+".html")
				CA += 1
			catch_html(links[L], codes[C], names[N])
		except Exception:
			instancia.dialogError("[ERROR!]"+" Info {0}: {1} don't downloaded".format(L,names[N]))
		L += 1
		N += 1
		sleep(1)
		if L >= 4:
			C = 1
		else:
			C += 1


	links.append(info1.replace('about', 'photos_all'))
	driver.get(links[20])
	srcs = []
	reacts = []
	photos = driver.find_elements_by_xpath('//a[@class="uiMediaThumb _6i9 uiMediaThumbMedium"]')
	for i, photo in enumerate(photos):
		src = photo.get_attribute('href')
		#driver.get(src)
		srcs.append(src)
		print(src,'\n')

	for i, src in enumerate(srcs):
		driver.get(src)
		catch_html(src, '_3og5._5wel.hasLeftCol._2yq.home.composerExpanded._5vb_.fbx._-kb._605a.j_1_vx5xcrw.chrome.webkit.x1.Locale_es_LA.cores-gte4.hasAXNavMenubar._19_u', filename.replace(".html","_")+'photo_{}.html'.format(i))

		file_3 = open('IDs/'+str(url)+'/'+filename.replace(".html","_")+'photo_{}.html'.format(i), "r")
		data_3 = file_3.read()
		getdata = data_3.find('/ufi/reaction/profile/browser/?ft_ent_identifier=')
		info3 = "https://www.facebook.com/"+data_3[getdata:getdata+500].split('"')[0]
		print(info3)
		reacts.append(info3)
	for i, react in enumerate(reacts):
		driver.get(react)
		catch_html(react, '_4__a.fbx._-kb._605a.j_1_vx5xcrw.chrome.webkit.x1.Locale_es_LA.cores-gte4._19_u.hasAXNavMenubar', filename.replace(".html","_")+'react_{}.html'.format(i))
		print('react_{}.html descargado !'.format(i))
		
	#dialogInfo('[+] IZANAMI scraping ended, you now can use IZANAGI for data-extraction')
	driver.close()