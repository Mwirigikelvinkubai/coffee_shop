import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # Name too short
    with pytest.raises(ValueError):
        Customer("a"*16)  # Name too long
    c = Customer("Kelvin")
    assert c.name == "Kelvin"

def test_create_order():
    cust = Customer("Anna")
    coffee = Coffee("Latte")
    order = cust.create_order(coffee, 5.0)
    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 5.0

def test_most_aficionado():
    cust1 = Customer("Joe")
    cust2 = Customer("Ann")
    coffee = Coffee("Espresso")
    cust1.create_order(coffee, 5.0)
    cust1.create_order(coffee, 2.0)
    cust2.create_order(coffee, 10.0)
    assert Customer.most_aficionado(coffee) == cust2
