from  bs4 import BeautifulSoup
import requests

#https://www.spravka333333.ru/currency?date=2021-06-08




#URL = 'https://www.spravka333333.ru/currency-data/full.json'
URL= 'https://www.spravka333333.ru/currency'
html= requests.get(URL)

#print(html.text)


model = BeautifulSoup(html.text, 'html.parser')
data = model.find(class_='onDate c-calendar').get_text()
last_data = data.strip()



table_main = model.find(class_ ='currency sorter tablesorter {sortlist: [[1,1]]}').tbody
trs = table_main.find_all('tr')

print(data)
print('-----------------------------------')

for tr in trs:

	bank_name = tr.td.div.div.get_text()
	bank_address =  tr.span.get_text()
	bank_phone  = tr.find(class_='fa fa-phone')['href']

	tds = tr.find_all('td')

	dollar_bay  = tds[1].get_text()
	dollar_sail = tds[2].get_text()

	euro_bay  = tds[3].get_text()
	euro_sail = tds[4].get_text()

	yan_bay   = tds[5].get_text()
	yan_sail  = tds[6].get_text()

	yena_bay  = tds[7].get_text()
	yena_sail = tds[8].get_text()
	print( bank_name , bank_address , bank_phone, '>>> ' , dollar_bay , dollar_sail, euro_bay,  euro_sail , yan_bay, yan_sail, yena_bay, yena_sail )
























#bank_name = trs[0].td.div.div.get_text()
#bank_address =  trs[0].span.get_text()
#bank_phone  = trs[0].find(class_='fa fa-phone')['href']

#tds = trs[0].find_all('td')

#dollar_bay  = tds[1].get_text()
#dollar_sail = tds[2].get_text()

#euro_bay  = tds[3].get_text()
#euro_sail = tds[4].get_text()

#yan_bay   = tds[5].get_text()
#yan_sail  = tds[6].get_text()

#yena_bay  = tds[7].get_text()
#yena_sail = tds[8].get_text()


















#print( bank_name , bank_address , bank_phone, ' ------------------- ' , dollar_bay , dollar_sail, euro_bay,  euro_sail , yan_bay, yan_sail, yena_bay, yena_sail )
#print( bank_name , bank_address , bank_phone) 
#print(  dollar_sail, euro_bay,  euro_sail , yan_bay, yan_sail, yena_bay, yena_sail )




















