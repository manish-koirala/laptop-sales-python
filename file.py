class File:
    """ A class for reading and writing from and to stock.txt file. """
    def __init__(self):
        """ Initialize the attributes of File instance"""
        self.file_path = './stock/stock.txt'

    def read(self):
        """ Read the stock.txt file and return a 2d-list containing data from the file."""
        stock_data = [] # stock_data is a 2d list where each inner list contains data about a particular product.
        with open(self.file_path, 'r') as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                line_data = line.replace('\n','').split(',') # line_data is a list of comma delimeted data_fields from a line. 
                stock_data.append(line_data)
        return stock_data

    def write(self, stock_data):
        """ Accept a 2d list 'stock-data', convert the list into appropriate string format and write to the stock.txt file."""
        file_string = ""
        with open(self.file_path, 'w') as file_obj:
            for line_data in stock_data:
                line = ','.join(line_data)
                line +=  '\n'
                file_string += line # Recreate the appropriate string to write to the file.
            file_obj.write(file_string)
