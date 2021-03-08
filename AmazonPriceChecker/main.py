import requests
import lxml
from smtplib import SMTP
from email.message import EmailMessage
from pprint import *
from bs4 import BeautifulSoup
MY_EMAIL = "mypython.botmail@gmail.com"
MY_PSWD = "CCLYRDOCTOR2002"
ADDRESS = "davidhuertas11@gmail.com"
url ="https://www.amazon.es/Microsoft-Surface-Laptop-Ordenador-i5-1035G1/" \
     "dp/B08JZVBZ13?ref_=Oct_DLandingS_D_be179183_60&smid=A1AT7YVPFBWXBL"
headers = {"Accept-Language": "en-US,en;q=0.9,es;q=0.8,zh-CN;q=0.7,zh;q=0.6",
           "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) " 
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
response = requests.get(url = url, headers= headers)
pprint(response.text)
amazon_html = response.text
soup = BeautifulSoup(amazon_html,"lxml")
web_price = soup.find(id="priceblock_dealprice").get_text().split()
product_title = soup.find(id="productTitle").get_text().strip()
print(product_title)
price = web_price[0].replace(",",".")

message = EmailMessage()
message.add_header("From", MY_EMAIL)
message.add_header("To", ADDRESS)
message.add_header("Subject","Amazon price alert!" )
message.set_content(f"{product_title} is now {web_price[0]} €\n"
                    f"{url}")
message.set_payload(f"{product_title} is now {web_price[0]} €\n"
                    f"{url}",charset = "utf-8")
if float(price) < 640.0:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PSWD)
        connection.send_message(message,from_addr = MY_EMAIL,to_addrs = ADDRESS)
