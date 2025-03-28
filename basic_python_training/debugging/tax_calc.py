def calculate_tax(amount, tax_rate):
    return amount * tax_rate / 100  #Incorrect calculation should add tax to amount

total_price = calculate_tax(100, 10)  # Expected: 110, but this returns 10
print(f"Total Price: {total_price}")
