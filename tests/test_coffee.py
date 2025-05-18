import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("ab")  # Too short
    c = Coffee("Mocha")
    assert c.name == "Mocha"

def test_num_orders_and_average_price():
    cust = Customer("Ben")
    coffee = Coffee("Cappuccino")
    cust.create_order(coffee, 4.0)
    cust.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0

def test_customers_list():
    cust1 = Customer("Sam")
    cust2 = Customer("Liz")
    coffee = Coffee("Americano")
    cust1.create_order(coffee, 3.0)
    cust2.create_order(coffee, 4.0)
    customers = coffee.customers()
    assert cust1 in customers
    assert cust2 in customers
