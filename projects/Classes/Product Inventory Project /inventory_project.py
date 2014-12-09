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

    def view(self, yaml_data):
        print yaml.dump(yaml_data, default_flow_style =False)

def main():
    inventory = Inventory()

    yaml_file = open("./products.yaml")
    yaml_data = yaml.safe_load(yaml_file)

    running = True

    while running:
        print "-- Product Inventory --"
        print "-- Options --\n"
        print "1. View inventory"

        user_input = int(raw_input(">"))

        if user_input == 1:
            inventory.view(yaml_data)
        else:
            running = False

if __name__ == "__main__":
    main()
