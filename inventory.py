# Reflection:
# 1. The most surprising thing about how lists work in Python is how negative indexing 
# allows you to count backward from the end of the list seamlessly (-1 for the last item). 
# Coming from tools like Excel, where indexing usually starts at 1 and looking backward 
# requires complex formulas, Python's flexibility with slicing and negative indices makes 
# data manipulation much more intuitive once you get used to it.
#
# 2. In a previous class project managing retail inventory and sales data, we had to manually 
# filter and calculate weekly averages for hundreds of product transactions across multiple 
# spreadsheets. Using a Python script with list methods like .append(), sum(), and conditional filtering 
# would have saved hours of tedious manual copy-pasting and formula debugging in Excel.

# Exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2

print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5

coords = (40.7128, -74.0060) #NYC coordinates

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuple protect coodinates from being changed by accident")

# Exercise 6

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sale: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for sale in sales:
    if sale > best:
        best = sale
    if sale < worst:
        worst = sale

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}") 

# Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round[price * 0.9, 2])

print(prices)
print(discounted)

# Exercise 8

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")
