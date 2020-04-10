from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def amaterasu(url, find, save, route):
    my_url = url

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    print(find.split(';')[2])
    containers = page_soup.findAll(find.split(';')[0],{str(find.split(';')[1]):str(find.split(';')[2])})

    for i, container in enumerate(containers):
        
        exec('print(i,": ",container.{})'.format(route))
        # container.div.div.a["href"])
        # container.div.a["title"])
        # container.div2,'\n')
        if save != None:
            code = url+' | '+find+' | '+'container.{}'.format(route)
            savef = open(str(save)+'.txt', 'w+')
            savef.write(code)
            savef.close()