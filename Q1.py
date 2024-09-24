def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example usage with price 60
price = 60
discount_percent = 25  # For example, a 25% discount

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
print(f"The final price after applying {discount_percent}% discount is: ${final_price:.2f}")
