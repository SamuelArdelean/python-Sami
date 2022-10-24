import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
link = BeautifulSoup(req.text, 'html.parser')  #html5lib
#print(link)

main= link.find_all('div', attrs={'id':'contentDiv'})
#print(main)
header_list = []
for obj in main:
    for table_index in obj.find_all('table'):
        #print(table_index)
        for table_trs in table_index.find_all('tr'):
            #print(table_trs)

            if table_trs.find_all('th'):
                header_list=[header_data.get_text() for header_data in table_trs.find_all('th')]
                #for header_data in table_trs.find_all('th'):
                #    header_list.append(header_data.get_text())
            for td in table_trs
print(header_list)


