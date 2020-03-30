from locators.apartments_locators import ApartmentLocator

class ApartmentParser:
    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        f'< Apartment {self.apartment_name},{self.address}, {self.price}>'

    @property
    def listingid(self):
        locator =ApartmentLocator.LISTINGID_LOCATOR
        return self.parent.select_one(locator).attrs['listing_id']

    @property
    def longitude(self):
        locator=ApartmentLocator.LONGITUDE_LOCATOR
        return self.parent.select_one(locator).attrs['longitude']

    @property
    def latitude(self):
        locator =ApartmentLocator.LATITUDE_LOCATOR
        return self.parent.select_one(locator).attrs['latitude']

    @property
    def apartment_link(self):
        locator=ApartmentLocator.LINK_LOCATOR
        return self.parent.select_one(locator).attrs['href']

    @property
    def address(self):
        locator=ApartmentLocator.ADRESS_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def apartment_name(self):
        locator=ApartmentLocator.NAME_LOCATOR
        return self.parent.select_one(locator).string  # .attrs['class']

    @property
    def price(self):
        locator=ApartmentLocator.PRICE_LOCATOR
        #pricelocator = '$([0-9]+\,[0-9])+'
        price_link = self.parent.select_one(locator).get_text()
        price_split = [x for x in price_link.split('\n') if len(x) != 0]
        #matcher = re.search(pricelocator, price_split[0])
        return float(price_split[0].replace('$', '').replace(',', ''))

    @property
    def number_bed(self):
        locator = ApartmentLocator.PRICE_LOCATOR
        # pricelocator = '$([0-9]+\,[0-9])+'
        price_link = self.parent.select_one(locator).get_text()
        price_split = [x for x in price_link.split('\n') if len(x) != 0]
        return price_split[1].split(' ')[0]

    @property
    def number_bath(self):
        locator = ApartmentLocator.PRICE_LOCATOR
        price_link = self.parent.select_one(locator).get_text()
        price_split = [x for x in price_link.split('\n') if len(x) != 0]
        return price_split[2].split(' ')[0]

    @property
    def broker_name(self):
        locator =ApartmentLocator.BROKER_LOCATOR
        features =self.parent.select_one(locator).get_text().split('\n')  # .attrs['div']
        listfeatures = [x for x in features if len(x) != 0]
        return [x for x in listfeatures if x.startswith('By')][0][3:]

