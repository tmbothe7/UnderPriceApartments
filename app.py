import requests
import re
from pages.all_apartment_page import ApartmentPage
from bs4 import BeautifulSoup
from locators.apartments_locators import ApartmentLocator
from locators.all_apartment_page import ApartmentsPageLocators

page_content = requests.get('https://www.renthop.com/nyc/apartments-for-rent').content

page = ApartmentPage(page_content)

Apartments =page.apartments()

for ap in Apartments:
    print (f'{ap.apartment_name},{ap.address}')


