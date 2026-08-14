def calculate_total(price, quantity, discount_rate=0):
    subtotal = price * quantity
    discount = subtotal * discount_rate

    return int(subtotal - discount)


total = calculate_total(12000, 3, 0.1)
print(f"할인 적용 금액: {total:,}원")
