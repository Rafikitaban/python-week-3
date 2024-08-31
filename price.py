#Task 1
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:

        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    
    else:
        return price

original_price = 1000
discount_percentage = 25

final_price = calculate_discount(original_price, discount_percentage)
print(final_price) 

#Task 2
def calculate_discount(price, discount_percent):
   
   
    if discount_percent >= 20:
       
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    
    else:
        return price

try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    
    final_price = calculate_discount(original_price, discount_percentage)

   
    if final_price < original_price:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")

