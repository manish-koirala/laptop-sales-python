class Transaction:
    """ A class to manage the buy and sell transactions by making changes to stock_data list. """
    def __init__(self, mp_instance):
        """ Initialize the attributes of the Transaction instance. """
        self.stock_data = mp_instance.stock_data

    def buy(self, purchases_cart):
        """ Make changes to the stock_data based on products selected for purchase  """
        for product_id, purchase_quantity in purchases_cart.items():
            intial_quantity = int(self.stock_data[product_id][3])
            final_quantity = intial_quantity + purchase_quantity
            self.stock_data[product_id][3] = str(final_quantity)
        
    def sell(self, sales_cart):
        """  Make changes to the stock_data based on products selected for sale"""
        for product_id, sale_quantity in sales_cart.items():
            initial_quantity = int(self.stock_data[product_id][3])
            final_quantity = initial_quantity - sale_quantity
            self.stock_data[product_id][3] = str(final_quantity)
