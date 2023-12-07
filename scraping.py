import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pytz

def getDay(day):
    # Get the current date and time
    if day == 'Monday':
        return 'Lun'
    elif day == 'Tuesday':
        return 'Mar'
    elif day == 'Wednesday':
        return 'Mier'
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
    # url = "https://www.ivenezuela.travel/venezuela/dolar/precio-dolar-venezuela-dolartoday-monitor-oficial-bcv-hoy-tipo-de-cambio/"

    # Send a request to the website and get the HTML content
    response = urllib.request.urlopen(url)
    html_content = response.read()

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the elements with class 'wp-block-table is-style-stripes'
    elements = soup.find_all(class_='wp-block-table is-style-stripes')

    # Get the current date and time in UTC
    now_utc = datetime.utcnow()

    # Create a timezone object for UTC-4
    utc_minus_4 = pytz.timezone('America/Caracas')

    # Convert the UTC time to UTC-4 time
    now_utc_minus_4 = now_utc.astimezone(utc_minus_4)

    # Format the day of the week in Spanish
    day_of_week =  now_utc_minus_4.strftime("%A")

    number_of_week =  now_utc_minus_4.strftime("%-d")

    price = 0

    for element in elements:
        # Find the strong element with the value "Mie 18"
        print(getDay(day_of_week) + ' ' + number_of_week)
        strong_element = element.find('strong', string=getDay(day_of_week) + ' ' + number_of_week)
        if strong_element:
            # Find the td element that is next to the strong element
            td_element = strong_element.find_next('td')
            if td_element:
                # Print the values of the strong and td elements
                price = td_element.text.strip().replace("Bs. ", "").replace("↑", "").replace("↓", "").replace(",", ".")
    return float(price)


print(price())