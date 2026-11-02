# Reflections Questions:
# 1. The first bug spotted was a syntax error discovered by reading the 
# traceback and tracing variables with a print() statement. This shows 
# that my debugging instincts are growing stronger when it comes to 
# systematically reading error logs instead of guessing fixes blindly.

# 2. The apply_discount(price, tier) function takes a numerical price 
# and a customer tier string as inputs, applies a specific percentage 
# reduction depending on whether the tier is gold, silver, bronze, or none,
# and returns the final discounted price as a float. Yes, a colleague could 
# easily use it just by looking at its clear parameter names and return value 
# without needing to inspect the internal if/elif logic.

# 3. # AI Disclosure: AI was used as a tool to brainstorm logic and troubleshoot syntax for Exercise 5. 
# Reflection: Using the AI helped bridge gaps in understanding tracebacks, building my comprehension rather than
#just providing a copy-paste shortcut.

# Exercise 1
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for 100 at 7%: ${tax1:.2f}")
print(f"Tax for 250 at 8%: ${tax2:.2f}")

#Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"(tier): ${apply_discount(original_price, tier):.2f}")

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold'), (150,'silver'), (8, 'bronze'), (500, 'none')]

rate = 0.07

for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

#Exercise 5
# broken_sales.py - corrected version

sales = [120, 80, 250, 175, 90]

# LogicError: Change the assignment operator from '=' to '+=' so we add each sale to the running total instead of overwriting it every time.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# SyntaxError: Add the missing colon (:) at the end of the for statement so Python knows where the loop body starts.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# IndexError: Change the loop condition from '<=' to '<' because list indexes start at 0 and end at length minus one, preventing an index out of range crash.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6

x = 100 # global x

def double_it():
    x = 99 # local x
    return x * 2

print(x)    # output: 100
print(double_it())  #output: 1998
print(x)    # x does not change