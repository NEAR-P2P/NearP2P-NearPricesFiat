import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

def getDay(day):
    # Get the current date and time
    if day == 'Monday':
        return 'Lun'
    elif day == 'Tuesday':
        return 'Mar'
    elif day == 'Wednesday':
        return 'Mie'
    elif day == 'Thursday':
        return 'Jue'
    elif day == 'Friday': 
        return 'Vie'   
    elif day == 'Saturday':
        return 'Sab'
    else:
        return 'Dom'

def price():
    # URL to scrape
    url = "https://www.ivenezuela.travel/venezuela/dolar/precio-dolar-venezuela-dolartoday-monitor-oficial-bcv-hoy-tipo-de-cambio/"

    # Send a request to the website and get the HTML content
    response = urllib.request.urlopen(url)
    html_content = response.read()

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the elements with class 'wp-block-table is-style-stripes'
    elements = soup.find_all(class_='wp-block-table is-style-stripes')

    # Print the elements
    # Get the current date and time
    now = datetime.now()

    # Format the day of the week in Spanish
    day_of_week = now.strftime("%A")

    number_of_week = now.strftime("%d")

    price = 0

    for element in elements:
        # Find the strong element with the value "Mie 18"
        strong_element = element.find('strong', string=getDay(day_of_week) + ' ' + number_of_week)
        if strong_element:
            # Find the td element that is next to the strong element
            td_element = strong_element.find_next('td')
            if td_element:
                # Print the values of the strong and td elements
                price = td_element.text.strip().replace("Bs. ", "").replace("↑", "").replace("↓", "").replace(",", ".")
    return float(price)


# print(price())