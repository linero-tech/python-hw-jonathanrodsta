from to_do import TODO

# Define the function signature
from typing import List, Dict ,Any

def groceries(grocery_list: List[Dict[str, Any]]) -> float:
  total_price = 0.0
  for grocery in grocery_list:
    # Get the quantity and price from the map
    quantity = grocery["quantity"]
    price = grocery["price"]

    # Calculate the total price for this item
    item_total = quantity * price

    # Add the total price to the shopping cart total
    total_price += item_total
  return total_price





if __name__ == "__main__":
    shopping_cart = [{"product": "Milk","quantity": 1, "price": 1.50}]
    total_price = groceries(shopping_cart)
    print("Total price:", total_price)

