from bs4 import BeautifulSoup

from locators.all_apartment_page import ApartmentsPageLocators
from parsers.apartment import ApartmentParser

class ApartmentPage:
    def __init__(self,page):
        self.soup=BeautifulSoup(page,'html.parser')

    def apartments(self):
        return [ApartmentParser(a) for a in self.soup.select(ApartmentsPageLocators.APARTMENTS)]