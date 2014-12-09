import yaml

class Product(object):
    def __init__(self, ID, name, price, quantity):
        self.ID = ID
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self, name):
        print "get_price"

    def get_ID(self, name):
        print "get_ID"

    def get_quantity(self, name):
        print "get_quantity"

class Inventory(object):
    def __init__(self):
        pass

    def add_product(self):
        pass

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
            if yaml.dump(yaml_data["Products"][product_name], default_flow_style = False) != KeyError:
                print "\n[+] Product found: " + product_name
                print yaml.dump(yaml_data["Products"][product_name], default_flow_style = False)
        except KeyError, e:
            print "\n[!] Product not found: " + str(e)
            main()
def main():
    inventory = Inventory()

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
        print "3. Exit"

        user_input = int(raw_input("> "))

        if user_input == 1:
            inventory.view_inventory(yaml_data)
        elif user_input == 2:
            inventory.search_inventory(yaml_data)
        else:
            exit(0)

if __name__ == "__main__":
    main()
