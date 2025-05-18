import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_validation():
    cust = Customer("Mike")
    coffee = Coffee("Flat White")
    with pytest.raises(ValueError):
        Order("NotCustomer", coffee, 5.0)
    with pytest.raises(ValueError):
        Order(cust, "NotCoffee", 5.0)
    with pytest.raises(ValueError):
        Order(cust, coffee, 0.5)  # Price too low
    order = Order(cust, coffee, 7.5)
    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 7.5
