import requests
from bs4 import BeautifulSoup
import lxml
import math
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Access the environment variables
variable_value = os.getenv("VARIABLE_NAME")

headers = {
    'Accept-Language' : 'en-US',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0'
}

URL = "https://www.amazon.com/Blink-Outdoor-Wireless-Security-Camera-5cam/dp/B086DKGCFP/ref=sr_1_1?keywords=blink&qid=1668612599&sr=8-1"
response = requests.get(URL, headers=headers)
content = response.text

soup = BeautifulSoup(content, 'lxml')
source_tag_price = soup.find(name="span", class_="a-price-whole")
price_tag = str(source_tag_price).split(">")
price_list = price_tag[1].split("<")
price = int(price_list[0])

if price < 300:
    my_email = os.getenv("MY_EMAIL")
    my_password = os.getenv("MY_PASSWORD")
    title = "Blink Outdoor wireless"
    with smtplib.SMTP("smtp.gmail.com") as offert_remainder:
        offert_remainder.starttls()
        offert_remainder.login(user=my_email, password=my_password)
        offert_remainder.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Blink set Camaras Under Price!\n\nTitle: {title}\nCurrent Price: {price}\nLink: {URL}")