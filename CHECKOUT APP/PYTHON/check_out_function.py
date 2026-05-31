def calculate_bill_total(sub_total, discount_percent):
    discount_amount = (discount_percent / 100) * sub_total
    vat_amount = (17.5 / 100) * sub_total
    return sub_total - discount_amount + vat_amount


def calculate_balance(amount_paid, bill_total):
    return amount_paid - bill_total
