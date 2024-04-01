# Laptops-sales-py
# Author: Manish Koirala
# Copyright (c) 2023 Manish Koirala

# Imports
from file import File
from display import Display
from transaction import Transaction
from invoice import Invoice

class MainProgram:
    """ A class representing the main program. """
    def __init__(self):
        """ Initialize the attributes of MainProgram instance. """
        self.file = File()
        self.stock_data = self.file.read() # A 2D List where each inner list represents information about a product.
        self.display = Display(self)
        self.transaction = Transaction(self)
        self.invoice = Invoice(self)
        self.loop = True
        
    def run_program(self):
        """ Run the main program. """
        while self.loop:
            self.display.show_options()
            option = self.display.prompt_option()

            # Option 1 - Buy products to the stock
            if option == 1:
                distributor_name = self.display.prompt_distributor_name()
                self.display.show_product_info()
                purchases_cart = self.display.gen_purchases_cart()
                self.transaction.buy(purchases_cart)
                self.invoice.gen_purchase(distributor_name, purchases_cart)
                self.file.write(self.stock_data)

            # Option 2 - Sell products from the stock
            elif option == 2:
                customer_name = self.display.prompt_customer_name()
                customer_phone = self.display.prompt_customer_phone()
                self.display.show_product_info()
                sales_cart = self.display.gen_sales_cart()
                self.transaction.sell(sales_cart)
                self.invoice.gen_sales(customer_name, customer_phone, sales_cart)
                self.file.write(self.stock_data)

            # Option 3 - Display products in the stock
            elif option == 3:
                self.display.show_product_info()
                input("Press 'Enter' to continue...")

            # Option 4 - Quit the program
            elif option == 4:
                print("\nQuitting...")
                self.loop = False                        

# Create a MainProgram instance and run it's run_program() method only if 
# the module is directly called by the python interpreter.
if __name__ == '__main__':
    mp = MainProgram()
    mp.run_program()
