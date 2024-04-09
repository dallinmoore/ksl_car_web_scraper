class Car():
    def __init__(self, make, model, year, trim, miles, price, link):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__trim = trim
        self.__miles = miles
        self.price = price
        self.link = link

    def __str__(self) -> str:
        pass
    # Getters
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_trim(self):
        return self.__trim

    def get_miles(self):
        return self.__miles

    def get_price(self):
        return self.__price

    def get_link(self):
        return self.__link

    # Setters

    def set_price(self, price):
        self.__price = price

    def set_link(self, link):
        self.__link = link