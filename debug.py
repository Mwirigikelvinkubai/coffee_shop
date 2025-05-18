from customer import Customer
from coffee import Coffee
from order import Order

# Create Customers
kelvin = Customer("Kelvin")
jane = Customer("Jane")

# Create Coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create Orders
kelvin.create_order(latte, 5.0)
kelvin.create_order(espresso, 3.5)
jane.create_order(latte, 4.5)
jane.create_order(latte, 4.0)

# Test relationship methods
print("Kelvin's Coffees:", [c.name for c in kelvin.coffees()])
print("Latte Orders:", latte.num_orders())
print("Latte Avg Price:", latte.average_price())
print("Aficionado for Latte:", Customer.most_aficionado(latte).name)

# Validate error handling
try:
    Customer("")
except ValueError as e:
    print("Caught error for bad customer name:", e)

try:
    Coffee("A")
except ValueError as e:
    print("Caught error for bad coffee name:", e)

try:
    Order(kelvin, latte, 0.5)  # Invalid price
except ValueError as e:
    print("Caught error for bad price:", e)
