import yaml,sys

class Product(object):
    def __init__(self):
        pass

    def create_product(self):
        ID = self.get_new_ID()
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

    def get_new_ID(self):
        yaml_file = open("./products.yaml")
        yaml_data = yaml.safe_load(yaml_file)

        highest_ID = 0 # keep track of the IDs

        for key,value in yaml_data.items():
            for i,k in value.items():
                if i == "id":
                    if highest_ID < k:
                        highest_ID = k
        return highest_ID + 1

    def get_quantity(self, name):
        return self.quantity

class Inventory(object):
    def __init__(self):
        pass

    def add_product(self, product):
        stream = file("./products.yaml", "a")
        yaml.dump(product,stream, default_flow_style = False) # .dump() can be used to append YAML files or print them

    def remove_product(self):
        pass

    def update_product(self):
        pass

    def view_inventory(self, yaml_data):
        print yaml.dump(yaml_data, default_flow_style = False)

    def get_search_term(self, yaml_data):
        search_term = raw_input("[+] Type the name of the product you want to search: ")
        return search_term.lower()

    def search_inventory(self,yaml_data):
        product_name = self.get_search_term(yaml_data)

        try: # If the product actually exists then print it otherwise throw an error
            if yaml.dump(yaml_data[product_name], default_flow_style = False) != KeyError:
                print "\n[+] Product found: " + product_name
                print yaml.dump(yaml_data[product_name], default_flow_style = False)
        except KeyError, e:
            print "\n[!] Product not found: " + str(e)
            main()

def main():
    inventory = Inventory()
    product = Product()

    # Open the YAML file and load it into a variable
    yaml_file = open("./products.yaml")
    yaml_data = yaml.safe_load(yaml_file)

    # Set up a loop so the program doesn't end and display the menu
    running = True
    while running:
        print "\n-- Product Inventory --"
        print "-- Options --\n"
        print "1. View inventory"
        print "2. Search inventory"
        print "3. Add product to inventory"

        try: # Check that the user input is a whole number
            user_input = int(raw_input("> "))

            if user_input == 1:
                inventory.view_inventory(yaml_data)
            elif user_input == 2:
                inventory.search_inventory(yaml_data)
            elif user_input == 3:
                 new_product = product.create_product()
                 inventory.add_product(new_product)
            else:
                exit(0)
        except ValueError, e:
           print "[!] Input must be a whole number: " + str(e)
           exit(0)

if __name__ == "__main__":
    main()
