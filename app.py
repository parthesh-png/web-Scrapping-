
# this app scrap product data from amazon website 

# beautifulSoup
# requests - it req to the web site 
# lxml - converter 

from bs4 import BeautifulSoup
import requests
import csv
url = "https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJ7S59D/ref=sr_1_3?crid=26GV7GTWWX6FE&dib=eyJ2IjoiMSJ9.y08pMqaeTlUXGU64oyMGlzJpvwJmFja_2WSBVs3GZOGZhsU6s-KsHLVTWzO21l03qir4fMp-gwNdlMVVxkeB0U0a9Sv9exSHe_q5RDa6QKlG5lViUEKE-ydbpQqKkjxJrQaz8itht_kSZ4EU2EO0fAxExyo1V42LXHxoClmXLf1yH5SV8mSmR_PrwxeWwF-_B-z8oV8_aYNp3O4RqCdTAp_gtRGSnJYAoCKrKpHfDAI.aLuwb4PWEz4XfLvTmJJpZzBz2SkLGQcrvSByxEsn4tg&dib_tag=se&keywords=apple%2Bairpod%2Bpro%2Bmax&nsdOptOutParam=true&qid=1752966680&sprefix=apple%2Bairpod%2Bpro%2Bmax%2Caps%2C291&sr=8-3&th=1"

headers = {"user_Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36" }

response = requests.get(url,headers=headers)

if response.status_code ==200:
    # print(response.status_code)
    html_content = response.text
else:
    print("fetching error")


soup = BeautifulSoup(html_content,'lxml')

# print(soup.prettify())
  

product_title = soup.find("span", id = "productTitle").text.strip()
product_price = soup.find("span", class_= "a-price-whole").text.strip()
product_rating = soup.find("span",id ="acrPopover").text.strip()

product_bp= soup.find("ul",class_="a-unordered-list a-vertical a-spacing-mini").text.strip()

product_description = soup.find("div", id="productDescription").text.strip()
reviews = soup.find("ul", id="cm-cr-dp-review-list").text.strip()



# print(product_rating)
# print(product_bp)
print(reviews)




# saving the data
with open("amazon_airpod pro max.csv", mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["product_title", "product_price", "product_rating", "product_bp", "product_description", "reviews"])

    writer.writerow([product_title, product_price, product_rating, product_bp, product_description, reviews])

print("data saved!")