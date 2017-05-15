import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-alba-slat-back-dining-chair/p1099108?colour=Soft%20Grey/Oak")
content = request.content
soup = BeautifulSoup(content, 'html.parser')

element = soup.find('span', {'itemprop':'price', 'class':'now-price'})

price_string = element.text.strip()

print(price_string)

price_num = float(price_string[1:])
# [:] makes a real copy and cuts off the pound sign

print(price_num)

if price_num < 200:
    print('gooD price!')
else:
    print('huh')

#<span itemprop="price" class="now-price">£99.00 </span>

