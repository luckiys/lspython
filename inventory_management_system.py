"""
Inventory Management System
---------------------------
A product inventory system that manages items, applies discounts,
and searches products by price threshold.

Author: Lakulish Saini
"""

def print_info(names, ids, prices, quantities):
    """Display product information in a formatted table."""
    print()
    print(f"{'Name':<12}{'ID':<12}{'Price':<12}{'Quantity':<12}")
    print("-" * 48)
    for i in range(len(names)):
        print(f"{names[i]:<12}{ids[i]:<12}${prices[i]:<11.2f}{quantities[i]:<12}")


def average_prices(prices):
    """Calculate and return the average price of all products."""
    total = 0
    for price in prices:
        total += price
    return total / len(prices)


def apply_discount(prices, rate=0.15):
    """Apply a discount rate to all prices and return updated list."""
    discounted = []
    for price in prices:
        discounted.append(price * (1 - rate))
    return discounted


def search_by_price(names, ids, prices, quantities, threshold):
    """Display products with price greater than or equal to threshold."""
    print(f"\nProducts with price >= ${threshold:.2f}")
    print()
    print(f"{'Name':<12}{'ID':<12}{'Price':<12}{'Quantity':<12}")
    print("-" * 48)
    for i in range(len(prices)):
        if prices[i] >= threshold:
            print(f"{names[i]:<12}{ids[i]:<12}${prices[i]:<11.2f}{quantities[i]:<12}")


def main():
    print("*" * 50)
    print("       Inventory Management System")
    print("*" * 50)
    print()
    
    # Initialize lists to store product data
    names = []
    ids = []
    prices = []
    quantities = []
    
    # Get product details from user
    num_products = 6
    print(f"Enter details for {num_products} products\n")
    
    for i in range(num_products):
        print(f"Product {i + 1} details:")
        names.append(input("  Enter product name: "))
        ids.append(int(input("  Enter product ID: ")))
        prices.append(float(input("  Enter product price: ")))
        quantities.append(int(input("  Enter product quantity: ")))
        print()
    
    # Display original inventory
    print("Original Product Information:")
    print_info(names, ids, prices, quantities)
    
    # Calculate and display average price before discount
    avg_before = average_prices(prices)
    print(f"\nAverage price before discount: ${avg_before:.2f}")
    
    # Apply 15% discount
    prices = apply_discount(prices, 0.15)
    print("\n✓ 15% discount has been applied to all products!")
    print_info(names, ids, prices, quantities)
    
    # Calculate and display average price after discount
    avg_after = average_prices(prices)
    print(f"\nAverage price after discount: ${avg_after:.2f}")
    
    # Search for products above average price
    print()
    search_by_price(names, ids, prices, quantities, avg_after)


if __name__ == "__main__":
    main()

