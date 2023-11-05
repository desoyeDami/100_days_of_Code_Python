import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6",
                        headers=headers
                        )
amz_response = response.text

soup = BeautifulSoup(amz_response, "lxml")
price = int(soup.select_one(selector=".a-price-whole").text.split(".")[0])
product_title = soup.select_one(selector="#productTitle").text.encode('utf-8')

if price < 90:
    my_email = "desoyee@gmail.com"
    password = "wtvyqllmhffvuggh"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="desoyedami@gmail.com",
                            msg=f"Subject: Amazon Price Alert\n\n"
                                f"{product_title}\n\nPrice: {price}\n\n"
                                f"'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'")