customer_name = input("What is the customer's Name: ")

items = []
quantities = []
prices = []


shopping = True
while shopping:
    product = input("What did the user buy? ")
    qty = int(input("How many pieces? "))
    price = float(input("How much per unit? "))
   
    
    items.append(product)
    quantities.append(qty)
    prices.append(price)
   
    
    choice = input("Add more Items? (yes/no): ")
    if choice.lower() == "no":
        shopping = False

cashier_name = input("What is your name? ")
discount_percent = int(input("How much discount will he get (in %)? "))


sub_total = 0.0
print("\n--- INVOICE ---")
print(f"Customer: {customer_name}")
print(f"Cashier: {cashier_name}")
print("---------------------------------")


for item in range(len(items)):
    item_total = quantities[item] * prices[item]
    sub_total += item_total
    print(f"{items[item]} - Qty: {quantities[item]} at {prices[item]} = {item_total}")

print("---------------------------------")


discount_amount = (discount_percent / 100) * sub_total
vat_amount = (17.5 / 100) * sub_total
bill_total = sub_total - discount_amount + vat_amount

print(f"Sub Total: {sub_total}")
print(f"Discount: {discount_amount}")
print(f"VAT (17.5%): {vat_amount}")
print(f"Bill Total: {bill_total}")
print("---------------------------------")
print(f"THIS IS NOT A RECEIPT KINDLY PAY {bill_total}")
print("---------------------------------")


amount_paid = float(input("\nHow much did the customer give to you? "))
balance = amount_paid - bill_total

print("\n--- FINAL RECEIPT ---")
print(f"Bill Total: {bill_total}")
print(f"Amount Paid: {amount_paid}")
print(f"Balance: {balance}")
print("---------------------------------")
print("THANK YOU FOR YOUR PATRONAGE")
print("---------------------------------")
