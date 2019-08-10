import requests 
from bs4 import BeautifulSoup
import smtplib
import time

# url to your product you want to watch for price drops
url="url_to_your_product_you_wanna_watch"

# Browser Agent
# Just Google: "My User Agent" and paste it here
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0 '}

def preis_check():

    # call for data
    page = request.get(url, headers=hearders)
    soup = BeautifulSoup(page.content, 'html.parser')

    # title of the product
    title = soup.find(id="productTitle").get_text()

    # price of the product, normally a string
    price = soup.find(id="priceblock_ourprice").get_text()

    # first 5 digits in front of the comma from the price
    converted_price = float(price[0:5])

    # send a mail if the price matches 
    if(converted_price < 1.000):
        send_mail()

  
def send_mail():

        # to send mails from gmail 
        server = smtplib.SMTP('smtp.gmail.com', 587)    

        # established connection between two mail servers
        server.ehlo()
        server.starttls()
        server.ehlo()

        # your gmail login
        server.login('youruser', 'yourpassword')

        # mesage content
        subject = 'Price dropped'
        body = 'Check the link: url_to_your_product_you_wanna_watch'

        msg = f"Subject: {subject} \n \n {body}"

        server.send_mail(
              'your_email_account' 
              'maybe_another_email_account'

              msg
        )
        print('Mail has been succesfully sent!')

        # close connection
        server.quit()

# Check once a day if the price chanced
while(true):
        preis_check()
        time.sleep(86400)