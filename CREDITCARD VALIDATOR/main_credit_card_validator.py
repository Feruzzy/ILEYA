card_number = input("Hello, Kindly Enter card details to verify: ")


card_type = "Invalid Card"
if card_number[0:1] == "4":
    card_type = "Visa"
elif card_number[0:1] == "5":
    card_type = "MasterCard"
elif card_number[0:2] == "37":
    card_type = "American Express"
elif card_number[0:1] == "6":
    card_type = "Discover"


total_sum = 0


reversed_card = card_number[::-1]


position = 1

for character in reversed_card:
    digit = int(character)
    if position % 2 == 0:
        doubled = digit * 2
        if doubled > 9:
            total_sum = total_sum + (doubled - 9)
        else:
            total_sum = total_sum + doubled
    else:
        total_sum = total_sum + digit

    position = position + 1

card_length = len(card_number)

if card_length >= 13 and card_length <= 16 and card_type != "Invalid Card" and (total_sum % 10 == 0):
    status = "Valid"
else:
    status = "Invalid"


print("*******************************************")
print("**Credit Card Type:", card_type)
print("**Credit Card Number:", card_number)
print("**Credit Card Digit Length:", card_length)
print("**Credit Card Validity Status:", status)
print("*******************************************")
