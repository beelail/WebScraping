import requests 
from bs4 import BeautifulSoup 
# ANSI escape codes for text colors
BLUE = '\033[94m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def scrap_product(url): 
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='thumbnail-container text-xs-center')
        dic = {}
        for p in products:
            # Use find or find_all to locate elements based on their classes
            name_element = p.find('h2', class_='h3 product-title')
            price_element = p.find('span', class_='price')

            # Check if the elements are found before extracting text
            name = name_element.text.replace('Smarthphone', '').strip() if name_element else 'N/A'
            price = price_element.text.replace('\xa0', '').replace('DT', '').replace(',', '').strip() if price_element else 'N/A'
            dic[name] = price
        return dic
    else:
        print(RED+"Could not scrap site ",RESET)

   
        
def scrap_product2(url): 
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div',class_='thumbnail-container')
        dic = {}
        for p in products:
            # Use find or find_all to locate elements based on their classes
            name_element = p.find('h3', class_='h3 product-title')
            price_element = p.find('span', class_='price')
            # Check if the elements are found before extracting text
            name = name_element.text.replace('Smarthphone', '').strip() if name_element else 'N/A'
            price = price_element.text.replace('\xa0', '').replace('DT', '').replace(',', '').strip() if price_element else 'N/A'
            dic[name] = price
        return dic
    else:
        print("Could not scrap site ")
 
def find_cheaper(product_list1 , product_list2 , product_name) : 
    price_1=price_2=0
    
    for i in product_list1 :
         if product_name in i  : 
             price_1= int(product_list1.get(i , 0) )   
             
    for i in product_list2:
         if product_name in i  : 
            price_2= int(product_list2.get(i , 0) )
             
                   
    if (price_1<price_2):
        return("Tunisianet is cheaper "+product_name +" price is "+ str(price_1)+" with : " +str(price_1-price_2)+" diffrence")
    elif (price_2<price_1):
        return("Sumsung shop  is cheaper "+product_name +" price is " +str(price_2)+" with : " +str(price_2-price_1)+" diffrence")
    else: 
        return("Both shops have the same price for "+ product_name)


product_tunisianet = scrap_product("https://www.tunisianet.com.tn/recherche?controller=search&orderby=price&orderway=asc&s=SMARTPHONE+SAMSUNG+GALAXY+S23+ULTRA&submit_search=")
product_sumsungshop = scrap_product2("https://www.samsungtunisie.tn/fr/recherche?controller=search&s=Samsung+Galaxy+S23+ULTRA")
print(YELLOW+"Tunisianet product list  : ",RESET,product_tunisianet )
print(BLUE+"Sumsung Shop product list  : ",RESET,product_sumsungshop )
product_name='Samsung Galaxy S23 Plus'
print(GREEN+find_cheaper(product_tunisianet , product_sumsungshop , product_name), RESET)