import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

headers = { 'Accept-Language' : "en-US,en;q=0.8",
            'User-Agent':"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/126.0.0.0 Safari/537.36",
        }

product_url = "https://www.amazon.in/GIGABYTE-REV2-0-WINDFORCE-GV-N3060GAMING-OC-12GD/dp/B0971BG25M/ref=sr_1_2?sr=8-2"
response = requests.get(url=product_url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price_product = soup.find(class_='a-price-whole')
number_without_comma = price_product.text.replace(",", "")
price = float(number_without_comma)

price_low = 31000

my_mail = MY_MAIL
password = PASSWORD
to = TO_MAIL

SUBJECT = 'Low Price Alert'
TEXT = f"GIGABYTE pci_e_x16 GeForce RTX 3060 is now ₹{price}"

title = soup.find(id="productTitle").get_text().strip()

if price < price_low:
    subject = 'Amazon Price Alert!'
    body = f"The price of {title} has dropped to Rs. {price}!\n\nCheck it out here: {product_url}"

    message = f"Subject: {subject}\n\n{body}"


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=to, msg=message.encode('utf-8'))
    print("Email sent successfully!")
