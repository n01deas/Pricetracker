# Pricetracker
Application to track prices from websites e.g. amazon, ebay, etc.

# Prerequisites
Prerequisites to use the application:
- request - to fetch data from the url

install the package via pip:
```
pip install request
```

- BeautifulSoup - to scrape information from webpages
install the package via pip:
```
pip install bs4
```

# Usage
1. Define the url you wanna watch under the url variable
2. Define your User-Agent from your Webbrowser
(Google: "My User Agent" to find yours)
3. Match the length of your price in the variable converted_price (e.g. [0:5] stands for five digits before the comma)
4. Define the time how often the website should be checked (e.g. 60 = every hour)
5. Define a limit, if it's undershot you'll get notificated
6. Link your personal mail  
