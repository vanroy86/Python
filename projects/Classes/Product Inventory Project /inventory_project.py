""" Copyright (C) 2014  https://www.github.com/IrrelevantPenguin

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."""
import yaml, sys

class Product(object):
    def __init__(self, yaml_data):
        self.yaml_data = yaml_data

    def create_product(self):
        ID = self.get_new_ID() # Automatically get new ID
        name = str(raw_input("[+] Enter the NAME of the new product: "))
        price = float(raw_input("[+] Enter the PRICE of the new product: "))
        quantity = int(raw_input("[+] Enter the QUANTITY of the new product: "))

        # Formatting
        name.lower()

        if (ID == None) | (name == "") | (price == None) | (quantity == None):
            print "[!] Error. Cannot be None"
            exit(0)
        else:
            product = {name: {"price" : price, "id" : ID, "quantity" : quantity}}
            return product

    def get_price(self, name):
        return self.price

    def get_ID(self):
        return self.ID

    def get_new_ID(self): # Automatically find the highest ID and then add 1 to create a new ID
        highest_ID = 0 # Keep track of the IDs
        # yaml_data is a list with 2 dicts inside.
        # Here we loop through the list and then through the dicts to finally find the ID
        for key,value in self.yaml_data.items(): # Looping through the list
            for i,k in value.items(): # Looping through the dicts
                if i == "id":
                    if highest_ID < k:
                        highest_ID = k
        return highest_ID + 1

    def get_quantity(self, name):
        return self.quantity

class Inventory(object):
    def __init__(self, yaml_file_path, yaml_data):
       self.yaml_file_path = yaml_file_path
       self.yaml_data = yaml_data

    def add_product(self, product):
        stream = file(self.yaml_file_path, "a") # Open the YAML file in append mode
        yaml.dump(product,stream, default_flow_style = False) # .dump() can be used to append YAML files or print them
        main()

    def remove_product(self):
        product_to_delete = self.get_search_term()
        stream = file(self.yaml_file_path, "w") # Open the YAML file in write mode instead of append so we don't get duplicates
        try:# If the product actually exists
            if yaml.dump(self.yaml_data[product_to_delete], default_flow_style = False) != KeyError:
                new_yaml = self.yaml_data
                del new_yaml[product_to_delete]
                yaml.dump(new_yaml, stream,default_flow_style = False) # Write the new YAML layout to the file

        except KeyError, e:
            print "[!] Product not found: " + str(e)
            main()

    def update_product(self, new_product):
        stream = file(self.yaml_file_path, "w")
        # Check if the current product exists
        if yaml.dump(self.yaml_data[new_product.keys()[0]], default_flow_style = False) != KeyError:
            new_yaml = self.yaml_data
            del new_yaml[new_product.keys()[0]] # Delete the old product
            new_yaml.update(new_product) # Add the new updated product to the file
            yaml.dump(new_yaml, stream, default_flow_style = False) # Write the new changes to the file
            print "[+] Product updated"

    def view_inventory(self):
        print yaml.dump(self.yaml_data, default_flow_style = False)

    def get_search_term(self):
        search_term = raw_input("[+] Type the NAME of the product: ")
        return search_term.lower()

    def search_inventory(self):
        product_name = self.get_search_term()

        try: # If the product actually exists then print it otherwise throw an error
            if yaml.dump(self.yaml_data[product_name], default_flow_style = False) != KeyError:
                print "\n[+] Product found: " + product_name
                print yaml.dump(self.yaml_data[product_name], default_flow_style = False)
        except KeyError, e:
            print "\n[!] Product not found: " + str(e)
            main()

def main():
    # Open the YAML file and load it into a variable
    yaml_file_path = "./products.yaml"
    with open(yaml_file_path) as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    inventory = Inventory(yaml_file_path, yaml_data)
    product = Product(yaml_data)

    # Set up a loop so the program doesn't end and display the menu
    running = True
    while running:
        print "\n-- Product Inventory --"
        print "-- Options --\n"
        print "1. View inventory"
        print "2. Search inventory"
        print "3. Add product to inventory"
        print "4. Remove product"
        print "5. Update a product"

        try: # Check that the user input is a whole number
            user_input = int(raw_input("> "))

            if user_input == 1:
                inventory.view_inventory()
            elif user_input == 2:
                inventory.search_inventory()
            elif user_input == 3:
                 new_product = product.create_product()
                 inventory.add_product(new_product)
            elif user_input == 4:
                 inventory.remove_product()
            elif user_input == 5:
                 new_product = product.create_product()
                 inventory.update_product(new_product)
            else:
                exit(0)
        except:
           print "[!] " + str(sys.exc_info())
           exit(0)

if __name__ == "__main__":
    main()
