from datetime import datetime

class Invoice:
    """ A class to manage the generation of invoices. """
    def __init__(self, mp_instance):
        """ Initialize the attributes of the Invoice instance. """
        self.stock_data = mp_instance.stock_data
    
    def gen_purchase(self, distributor_name, purchases_cart):
        """ Takes the string distributor_name and a dictionary called purchases_cart as parameters. 
        Then, generate invoice for a particular purchase. """
        total_cost_without_vat = 0
        date = datetime.now()
        invoice_num = int(date.timestamp())
        invoice_file = f'./invoices/purchases/{distributor_name}_{invoice_num}.txt'
        invoice_txt = " CIRCUIT-CITY LAPTOPS ".center(98,'-')
        invoice_txt += '\n' + "    Invoice For Purchase    ".center(98, '*')
        invoice_txt += f"\n\nDistributor Name: {distributor_name}"
        invoice_txt += f"\nDate And Time: {date}"
        invoice_txt += "\n\nTransaction Details: "
        invoice_txt += '\n' + '-'*98
        invoice_txt += '\n|' + f'{"S.N:".center(4)}' + '|' + f'{"Laptop Name".center(18)}' + '|' + f'{"Laptop Brand".center(18)}' + '|' + f'{"Unit Price".center(18)}' + '|' f'{"Laptop Quantity".center(18)}' + '|' + f'{"Total Price".center(15)}' + '|'
        invoice_txt += '\n'+ '-'*98
        for index, product_id in enumerate(purchases_cart.keys()):
            unit_cost = int(self.stock_data[product_id][2].replace('$',''))
            quantity_bought = purchases_cart[product_id]
            product_cost =  unit_cost * quantity_bought 
            total_cost_without_vat += product_cost
            invoice_txt += '\n|' + f'{str(index+1).center(4)}' + '|' + f'{self.stock_data[product_id][0].center(18)}' + '|' + f'{self.stock_data[product_id][1].center(18)}' + '|' + f'{self.stock_data[product_id][2].center(18)}' + '|' + f'{str(purchases_cart[product_id]).center(18)}' + '|' + f'{("$" + str(product_cost)).center(15)}' + '|'
        invoice_txt += '\n'+ '-'*98
        invoice_txt += '\n' + f'Total Cost Without VAT: ${total_cost_without_vat}'
        invoice_txt += '\n' + f'VAT Amount: ${total_cost_without_vat*0.13}'
        invoice_txt += '\n' + f'Total Cost With VAT: ${total_cost_without_vat + 0.13*total_cost_without_vat}'
        print('\n' + "#"*98)
        print(f"Invoice has been generated as {invoice_file}.txt".center(98))
        print("#"*98 + '\n')
        with open(invoice_file, 'w') as file_obj:
            file_obj.write(invoice_txt)
        print(invoice_txt)
        input("\nPress 'Enter' to continue...")

    def gen_sales(self, customer_name, customer_phone, sales_cart):
        """ Takes the customer name, customer phone number and a dictionary called sales_cart as parameters.
        Then, generate invoice for a particular sale"""
        total_cost_without_ship = 0
        date = datetime.now()
        invoice_num = int(date.timestamp())
        invoice_file = f'./invoices/sales/{customer_name}_{customer_phone}_{invoice_num}.txt'        
        invoice_txt = " CIRCUIT-CITY LAPTOPS ".center(98,'-')
        invoice_txt += '\n' + "    Invoice For Sale    ".center(98, '*')
        invoice_txt += f"\n\nCustomer Name: {customer_name}"
        invoice_txt += f'\nCustomer Phone Number: {customer_phone}'
        invoice_txt += f"\nDate And Time: {date}\n"
        invoice_txt += "\nTransaction Details: "
        invoice_txt += '\n'+ '-'*98
        invoice_txt += '\n|' + f'{"S.N:".center(4)}' + '|' + f'{"Laptop Name".center(18)}' + '|' + f'{"Laptop Brand".center(18)}' + '|' + f'{"Unit Price".center(18)}' + '|' + f'{"Laptop Quantity".center(18)}' + '|' + f'{"Total Price".center(15)}' + '|'
        invoice_txt += '\n'+ '-'*98
        for index, product_id in enumerate(sales_cart.keys()):
            unit_cost = int(self.stock_data[product_id][2].replace('$',''))
            quantity_sold = sales_cart[product_id]
            product_cost =  unit_cost * quantity_sold 
            total_cost_without_ship += product_cost
            invoice_txt += '\n|' + f'{str(index+1).center(4)}' + '|' + f'{self.stock_data[product_id][0].center(18)}' + '|' + f'{self.stock_data[product_id][1].center(18)}' + '|' + f'{self.stock_data[product_id][2].center(18)}' + '|'+ f'{str(sales_cart[product_id]).center(18)}' + '|' + f'{("$" + str(product_cost)).center(15)}' + '|'
        invoice_txt += '\n'+ '-'*98
        invoice_txt += '\n' + f'Total Cost Without Shipping: ${total_cost_without_ship}'
        invoice_txt += '\n' + f'Shipping Cost: $40'
        invoice_txt += '\n' + f'Total Cost With Shipping: ${total_cost_without_ship + 40}'
        print('\n' + "#"*98)
        print(f"Invoice has been generated as {invoice_file}.txt".center(98))
        print("#"*98 + '\n')
        with open(invoice_file, 'w') as file_obj:
            file_obj.write(invoice_txt)
        print(invoice_txt)
        input("\nPress 'Enter' to continue...")