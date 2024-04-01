class Display():
    """ A class to manage the display in the main program such as creating display menus and options."""
    def __init__(self, mp_instance):
        """ Initialize the attributes of the Display instance. """
        self.stock_data = mp_instance.stock_data # A 2D List where each inner list represents information about a product

    def show_product_info(self):
        """ Display the full information about available products in tabular format. """
        print("\n" + " Products Information ".center(30,':'))
        print('-'*120)
        print('|' + f"{'S.N.'.center(4)}" + '|' + f"{'Product Name:'.center(18)}" + '|' + f"{'Brand:'.center(18)}" + '|' + f"{'Price:'.center(18)}" + '|' + f"{'Quantity:'.center(18)}" + '|' + f"{'CPU Info:'.center(18)}" + '|' + f"{'GPU Info:'.center(18)}" + '|')
        print('-'*120)
        for index, product_info in enumerate(self.stock_data):
            print('|' + f'{str(index+1).center(4)}' + '|', end='')
            for data in product_info:
                print(data.center(18) + '|', end='')
            print('\n', end='')
        print('-'*120)

    def show_options(self):
        """ Display the first menu which provides available options to the user."""
        print("\n")
        print(" CIRCUIT-CITY LAPTOPS ".center(120, '-'))
        print("  Welcome to the interactive menu. Please choose an option below to continue...  ".center(80).center(120, '-'))
        print("\n" + " Options Available ".center(30, ':'))
        print("1. Buy an item to the stock.")
        print("2. Sell an item from the stock.")
        print("3. Display current stock information.")
        print("4. Exit the program.")
        
    def gen_sales_cart(self):
        """ Display the second menu and return a dictionary with product_id as key and product_quantity as value."""
        sales_cart = {} # A dictionary containing product-id as keys and product-quantities as value, for a sale.
        while True:
            # Prompt the user for product_id and sale_quantity
            product_id = self.prompt_product_id()
            sale_quantity = self.prompt_product_quantity()
            
            available_quantity = int(self.stock_data[product_id][3])
            # If the available quantity of the product is 0, then the product cannot be sold.
            if available_quantity == 0: 
                print(f"{product_id+1}: {self.stock_data[product_id][0]} is out of stock. Please try again.")
                continue
            # If the quantity to sell is more than the available quantity, then the product cannot be sold.
            elif sale_quantity > available_quantity:
                print("The available quantity is less than the desired quantity. Please try again.")
                continue
            
            # If the product is already added to sales_cart, then, increase it's quantity in sales_cart.
            if product_id in sales_cart.keys():
                sales_cart[product_id] += sale_quantity
            # If a new product is being added to sales_cart, create a new key value pair in sales_cart.
            else:
                sales_cart[product_id] = sale_quantity
            # Display that the product has been added to sales.
            print(f"{sale_quantity} amount of product: {self.stock_data[product_id][0]} has been added to the sales..")
            # Prompt the user whether to continue adding new items or not.
            choice_to_continue = self.prompt_continue()
            if (choice_to_continue == False):
                return sales_cart

    def gen_purchases_cart(self):
        """ Display the second menu and return a dictionary with product_id as key and product_quantity as value """
        purchases_cart = {} # A dictionary containing product-names as keys and product-quantities as value, during a purchase.
        while True:
            # Prompt the user for product_id and purchase_quantity
            product_id = self.prompt_product_id()
            purchase_quantity = self.prompt_product_quantity()

            # If the selected product is already added to the purchase, update it's quantity in product_bought.
            if product_id in purchases_cart.keys():
                purchases_cart[product_id] += purchase_quantity
            # If the selected product hasn't been added to the purchase, create a new key-value pair in purchases_cart.
            else:
                purchases_cart[product_id] = purchase_quantity
            # Display that the product has been added to purchase.
            print(f"{purchase_quantity} amount of product: {self.stock_data[product_id][0]} has been added to the purchase...")
            # Prompt the user whether to continue adding products to the purchase or not.
            choice_to_continue = self.prompt_continue()
            if (choice_to_continue == False):
                return purchases_cart
               

    # All the methods that implement validation
    def prompt_option(self):
        """ Prompt user for option, validate the option and return the validated option."""
        while True:
            try:
                option = int(input("Choose an option(1-4): "))
            except ValueError:
                print("\nInvalid Option. Please enter a valid numeric value in range 1-4.\n")
            else:
                if option in range(1,5):
                    return option
                else:
                    print("\nInvalid Option. Please enter a valid numeric value in range 1-4.\n")

    
    def prompt_customer_name(self):
        """ Prompt user for customer name and return the validated name. """
        while True:
            customer_name = input("Enter the customer name: ")
            if (len(customer_name) ==0 ):
                print("Customer name cannot be empty. Please enter a valid name...\n")
            elif (customer_name.isdecimal()):
                print("Customer name cannot be numeric. Please enter a valid name...\n")
            else:
                return customer_name
    
    def prompt_distributor_name(self):
        """ Prompt user for distributor name and return the validated name."""
        while True:
            distributor_name = input("Enter the distributor name: ")
            if (len(distributor_name) == 0):
                print("Distributor name cannot be empty. Please enter a valid name...\n")
            elif (distributor_name.isdecimal()):
                print("Distributor name cannot be numeric. Please enter a valid name...\n")
            else:   
                return distributor_name

    def prompt_customer_phone(self):
        """ Prompt user for customer phone number and return the validated phone."""
        while True:
            customer_phone = input("Enter the customer phone number: ")
            if (len(customer_phone) == 0):
                print("Customer phone number cannot be empty. Please enter a valid number...\n")
            elif (customer_phone.isalpha()):
                print("Customer phone number invalid. Please enter number only...\n")
            else:
                return customer_phone

    def prompt_product_id(self):
        """ Prompt user for product id and return the validated product id. """
        while True:
            product_id = input("Enter the product id: ")
            try:
                product_id = int(product_id)
            except ValueError:
                print("Invalid value for product id '"+ str(product_id) +"'\n")
            else:
                if product_id in range(1, len(self.stock_data)+1):
                    product_id -= 1
                    return product_id
                else:
                    print("Invalid range for product id'"+ str(product_id) +"'\n")
            
    def prompt_product_quantity(self):
        """ Prompt user for product quantity and return the validated product quantity. """
        while True:
            product_quantity = input("Enter the product quantity: ")
            try:
                product_quantity = int(product_quantity)
            except ValueError:
                print("Invalid value for product quantity:'"+ str(product_quantity) +"'\n")
            else:
                if product_quantity < 0:
                    print("Product quantity cannot be negative. Please enter a valid value...")
                else:
                    return product_quantity

    def prompt_continue(self):
        """ Prompt the user whether to continue adding more products or not."""
        while True:
            choice_to_continue = input("Do you want to continue(y/n): ")
            if choice_to_continue.lower() == "n":
                return False
            elif choice_to_continue.lower() == 'y':
                return True     
            else:
                print("Invalid option: '"+choice_to_continue+"'.") 
