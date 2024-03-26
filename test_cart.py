'''
UNIT TESTING PRODUCT FUNCTIONS 
'''
from unittest.mock import Mock
from cart import Cart
import pytest
from item_database import ItemDatabase


@pytest.fixture
def cart():
    #Initalizing cart for alltest
    return Cart(3)

def test_add_item(cart):
    cart.add("brush")
    assert cart.size() ==1 #If stmt true execute , else throws exception

def test_check_item_exists(cart):
    cart.add("iPhone")
    cart.add("AirPods")
    assert "iPhone" in cart.get_items() 

def test_cart_size(cart):
    cart.add("iPhone")
    cart.add("AirPods")
    assert cart.size() ==2

def test_cart_overflow(cart):
    cart.add("apple")
    cart.add("banana")
    cart.add("mango")
    #Adding 4th item
    with pytest.raises(OverflowError):
        cart.add("apple")

def test_total_price_calculation(cart):
    cart.add("apple")
    cart.add("banana")
    cart.add("mango")
    priceMap={
        "apple": 2,
        "mango": 3,
        "banana":1
    }
    def mock_get_item(item: str):
        if item == "apple":
            return 2
        if item == "banana":
            return 1
        if item == "mango":
            return 3
    
    item_database = ItemDatabase()
    item_database.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(item_database) == 6

def test_delete_item(cart):
    cart.add("apple")
    cart.add("banana")
    cart.add("mango")
    
    with pytest.raises(KeyError):
        cart.delete_item("apple")
        cart.delete_item("iPhone")

