import re
import os
from selenium import webdriver
from bs4 import BeautifulSoup
# ----------------------------------------------- Abre archivo HTML
print("=======================================================================================================================================")
load_sessions = open('sessions.txt', "r")
for line in open('sessions.txt', "r"):
    line = str(load_sessions.readline().split('\n')[0])
    print(line)
load_sessions.close()
print("=======================================================================================================================================")
session = input("Number of session: ")
rootDir = str(os.getcwd())+"/"+str(session)
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        part1 = fname.split('_')[1]
        part2 = fname.split('_')[0]
dir_root = "file://"+os.getcwd()+"/"+str(session)+"/"+part2+'_'+part1
print("================================================================ INFO =================================================================")
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
try:
    driver.get(dir_root+"_info.html") 
except:
    print("[!] Module 'info' not found.")
# ----------------------------------------------- Extraer texto del html(info).
for letter in "abcdefghijklmnopqrstuvwxyz":
    try:
        label_inf = driver.find_element_by_xpath('//*[@id="u_0_2'+letter+'"]/div[1]/ul').text
    except Exception as err:
        continue
    try:
        label_inf2 = driver.find_element_by_xpath('//*[@id="u_0_2'+letter+'"]/div[2]/ul').text # Obtine informacion del HTML en texto plano.
    except Exception as err:
        continue
patterns_delete = ["No hay lugares de trabajo para mostrar","No hay escuelas para mostrar","No hay lugares para mostrar","No hay información de situación sentimental para mostrar"]
for pattern in patterns_delete:
    label_inf = label_inf.replace(pattern, "")
# ------------------------------------------------ Regular Expressions --------------------------------------------------------
modules = ['regx_email','regx_bdate','regx_insta','regx_face','regx_instalink','regx_cellphone','regx_work','regx_studies','regx_living_in','regx_from','regx_lived','regx_love']
codes = [r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)",r"([\d]+\sde\s[\w\.-]+\sde\s\d\d\d\d)",r"[^Enlaces sociales][\w\W\.\d-]+(Instagram)[\)$]",
r"(https://www.facebook)[\w\.]+(/)([\W\w\.\_-]+)(\?)(ref=tn_tnmn)",r"(https://www.instagram)[\w\.]+(/)([\W\w\.\_-]+)(/)",
r"(Teléfonos)(\n[0-9]{4,5}\s[0-9]{2}-[0-9]{4})",r"((Encargad[oa]|Trabaja)\sen\s[\W\w\d\.-]+[\n$])",r"(Estudió\sen\s[\W\w\d\.-]+[\n$])",
r"(Vive\sen\s[\W\w\d\.-]+[\n$])",r"(De\s[\W\w\d\.-]+[\n$])",r"(Vivió\sen\s[\W\w\d\.-]+[\n$])",r"((En\suna\srelación|Comprometid[oa]|Casad[oa])\scon\s[\W\w\.-]+[\n$]?)"]
variation = ['','',".split('\n')[1]",".split('\n')[0]",".split('\n')[0]",".split('\n')[1]",".split('\n')[0]",
".split('\n')[0]",".split('\n')[0]",".split('\n')[0]",".split('\n')[0]",".split('\n')[0]"]
counter = 0
for code in codes:
    modules[counter] = code
    if counter <= 5:
        matcher = re.search(modules[counter], label_inf2)
    else:
        matcher = re.search(modules[counter], label_inf)
    if matcher:
        if counter <= 1:
            print(matcher.group())
        elif counter == 2:
            print(matcher.group().split('\n')[1])
        elif counter == 3 or 4: 
            print(matcher.group().split('\n')[0])
        elif counter == 5:
            print(matcher.group().split('\n')[1])
        elif counter > 5:
            print(matcher.group().split('\n')[0])
    counter += 1
# ============================================== LOOP PARA INFO GENERAL ============================================= #
def acssi_transform(inputString): # Funcion para quitar emojis.
    return inputString.encode('ascii', 'ignore').decode('ascii')
modules = ["events","app_instapp","music","sports","movies","tv","likes","map","books","games","reviews","notes","did_you_know"]
codes = ['//*[@id="collection_wrapper_2344061033"]','//*[@id="collection_wrapper_124024574287414"]','//*[@id="collection_wrapper_221226937919712"]',
'//*[@id="collection_wrapper_330076653784935"]','//*[@id="collection_wrapper_177822289030932"]','//*[@id="collection_wrapper_309918815775486"]',
'//*[@id="collection_wrapper_2409997254"]','//*[@id="collection_wrapper_302324425790"]','//*[@id="collection_wrapper_332953846789204"]',
'//*[@id="collection_wrapper_249944898349166"]','//*[@id="collection_wrapper_254984101287276"]','//*[@id="collection_wrapper_2347471856"]',
'//*[@id="collection_wrapper_1773166999589123"]']
counter = 0
for module in modules:
    try:
        driver.get(dir_root+"_"+module+".html")
    except:
        print("[!] Module "+"'"+module+"'"+" not found.")
    print("================================================================ "+module.upper()+" ===============================================================")
    try:
        label_inf = driver.find_element_by_xpath(codes[counter]).text
        if counter == 1 or 12: # Filtros para modulos especiales.
            label_inf_t = acssi_transform(label_inf)
            if counter == 1:
                regx_hashtag = r"(#[\w-]+[\s])+[\n]*"
                matcher = re.search(regx_hashtag, label_inf_t)
                if matcher:
                    matcher = acssi_transform(matcher.group())
                    print('Hashtags de instagram: ',matcher)
            else:
                print(label_inf_t.replace('Comentarios',""))
        else:
            print(label_inf.replace('Músico/banda',"")) # Se puede aplicar filtros generales
    except Exception as err:
        pass
    counter += 1
    
post_modules = ["friends","group","photos","react","videos"]