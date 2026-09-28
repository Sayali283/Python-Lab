# Program 1: Retail Point of Sale (POS) and Tier Evaluation
print("--- Welcome to the Store POS System ---")
item_price = float(input("Enter the price of the item: $"))
quantity = int(input("Enter the quantity purchased: "))

# Arithmetic Operators: Calculating the bill
subtotal = item_price * quantity
tax_amount = subtotal * 0.08  # Applying an 8% sales tax
final_total = subtotal + tax_amount

print("\n--- Receipt ---")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax_amount:.2f}")
print(f"Final Total: ${final_total:.2f}")

# Relational Operators: Checking business rules
# A customer becomes a "Gold Member" if they spend $200 or more in one transaction
is_gold_member = final_total >= 200.00
qualifies_free_shipping = final_total > 50.00

print("\n--- Customer Status ---")
print(f"Qualifies for Free Shipping (> $50): {qualifies_free_shipping}")
print(f"Upgraded to Gold Member (>= $200): {is_gold_member}")
