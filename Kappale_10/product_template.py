"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
Eppu Hassinen
50044786
eppu.hassinen@tuni.fi
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    # TODO: Define all the methods here.  You can see what they are,
    #       what parameters they take, and what their return value is
    #       by examining the main-function carefully.
    #
    #       You also need to consider which attributes the class needs.
    #
    #       You are allowed to modify the main function, but your
    #       methods have to stay compatible with the original
    #       since the automatic tests assume that.

    def __init__(self, product_name, price=1, sale_percentage=0):
        """

        :param product_name: Name of the product
        :param price: float, price of product
        :param sale_percentage: float, sale percentage
        """
        self.__name = product_name
        self.__price = price
        self.__sale_percentage = sale_percentage

    def printout(self):
        """
        Prints the values of the product
        :return:
        """

        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f'  Sale%: {self.__sale_percentage:.2f}')

    def get_price(self):
        """
        Returns the price with the calculated sale
        :return: float, price
        """
        return self.__price * ((100 - self.__sale_percentage) / 100)

    def set_sale_percentage(self, percentage):
        """
        Sets the sale percentage
        :param percentage: float, new sale percentage
        :return: Bool, returns true if the input can be converted to float
        """

        try:
            self.__sale_percentage = percentage
        except ValueError:
            return False
        return True


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price:.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price:.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price:.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
