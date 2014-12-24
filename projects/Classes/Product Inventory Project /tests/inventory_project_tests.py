from nose.tools import *
from inventory_project import *

def test_create_product():
    product = Product()
    product.create_product(3,"Orange", 0.4, 12)
