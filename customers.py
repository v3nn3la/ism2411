# Reflection:
# 1. Use .get() if there's a possibility of the key not being there and a safe default value rather than an error such as, while parsing messy user input 
# or an optional field. Use {} syntax when the key is mandatory for the program logic to work and its absence is an important bug that should immediately
# crash the program with a KeyError.

# 2. This is the equivalent of a PivotTable or a SUMIF formula in Excel. However, the Python variant is more useful when working with big data sets, since 
# it immediately repeats a workflow automatically, is error-free compared to manual spreadsheet work, and works with enormous data fiels without crashing 
# or row limit eorrs that Excel might produce.


# Exercise 1:
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400.00
}

print(customer["name"])  # Output: Alice
print(customer["email"])  # Output: alice@example.com
print(customer["tier"])  # Output: gold
print(customer["ytd_spend"])  # Output: 12400.00

# Exercise 2:
customer["phone"] = "555-5555"
print(customer)
customer['tier'] = "platinum"
print(customer)
del customer["email"]
print(customer)

print(customer.get('ytd_spend', 0))

# Exercise 3:
print(customer.get("email", "Email not found"))

# Exercise 4:
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

# Exercise 5:
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
purchase = 200
discount = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1- discount)
print(f"Tier; {customer['tier']}")
print(f"Discount: {discount*100}%")
print(f"Final price: ${final_price:.2f}")

# Exercise 6:
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "bronze"}
]

for cust in customers:
    tier = cust["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount
    print(f"Name: {cust['name']}, Tier: {tier}, Discount Amount: ${discount_amount:.2f}")

# Exercise 7: 
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK ALERT: {product} has only {details['stock']} units left.")


# Exercise 8:
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

region_summary = {}
for tx in transactions:
    region = tx["region"]
    amount = tx["amount"]
    region_summary[region] = region_summary.get(region, 0) + amount


for region in sorted(region_summary):
    print(f"{region}: {region_summary[region]}")