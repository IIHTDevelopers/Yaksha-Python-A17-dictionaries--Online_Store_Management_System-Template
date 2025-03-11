"""
Online Store Management System
This program demonstrates dictionary operations through an online store inventory management system.
"""

def initialize_data():
    """
    Initialize the store inventory with predefined products and categories using dictionaries.
    
    Returns:
        dict: A dictionary containing product data organized by product ID
    """
    # Create the main product inventory dictionary
    inventory = {
        "P001": {
            "name": "Smartphone XS",
            "category": "electronics",
            "price": 59999.99,
            "stock": 25,
            "rating": 4.5,
            "features": ["5G", "128GB Storage", "Dual Camera"]
        },
        "P002": {
            "name": "Designer Jeans",
            "category": "clothing",
            "price": 4999.99,
            "stock": 40,
            "rating": 4.2,
            "features": ["Slim Fit", "Stretch Denim", "Dark Wash"]
        },
        "P003": {
            "name": "Bluetooth Headphones",
            "category": "electronics",
            "price": 7999.99,
            "stock": 15,
            "rating": 4.7,
            "features": ["Noise Cancelling", "40hr Battery", "Hi-Fi Sound"]
        },
        "P004": {
            "name": "Organic Coffee Beans",
            "category": "groceries",
            "price": 899.99,
            "stock": 50,
            "rating": 4.8,
            "features": ["Fair Trade", "Whole Bean", "Medium Roast"]
        },
        "P005": {
            "name": "Running Shoes",
            "category": "footwear",
            "price": 6999.99,
            "stock": 30,
            "rating": 4.6,
            "features": ["Breathable", "Cushioned", "Lightweight"]
        }
    }
    
    # Create new products to be added later
    new_products = {
        "N001": {
            "name": "Smart Watch",
            "category": "electronics",
            "price": 15999.99,
            "stock": 20,
            "rating": 4.4,
            "features": ["Heart Rate Monitor", "GPS", "Water Resistant"]
        },
        "N002": {
            "name": "Protein Powder",
            "category": "health",
            "price": 1999.99,
            "stock": 45,
            "rating": 4.3,
            "features": ["Plant-Based", "20g Protein", "Sugar-Free"]
        }
    }
    
    return inventory, new_products

def filter_by_category(inventory, category):
    """
    Filter products by category using dictionary comprehension.
    
    Args:
        inventory (dict): The product inventory
        category (str): Category to filter by
    
    Returns:
        dict: Filtered products dictionary
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if category is None:
        raise ValueError("Category cannot be None")
    
    return {pid: product for pid, product in inventory.items() if product["category"] == category}

def filter_by_price_range(inventory, min_price, max_price):
    """
    Filter products by price range using dictionary comprehension.
    
    Args:
        inventory (dict): The product inventory
        min_price (float): Minimum price
        max_price (float): Maximum price
    
    Returns:
        dict: Filtered products dictionary
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if min_price is None or max_price is None:
        raise ValueError("Price range cannot be None")
    if min_price > max_price:
        raise ValueError("Minimum price cannot be greater than maximum price")
    
    return {pid: product for pid, product in inventory.items() 
            if min_price <= product["price"] <= max_price}

def filter_by_availability(inventory, min_stock=1):
    """
    Filter products by availability using dictionary comprehension.
    
    Args:
        inventory (dict): The product inventory
        min_stock (int): Minimum stock level required
    
    Returns:
        dict: Filtered products dictionary
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if min_stock < 0:
        raise ValueError("Minimum stock cannot be negative")
    
    return {pid: product for pid, product in inventory.items() if product["stock"] >= min_stock}

def filter_by_feature(inventory, feature):
    """
    Filter products by a specific feature using dictionary comprehension.
    
    Args:
        inventory (dict): The product inventory
        feature (str): Feature to filter by
    
    Returns:
        dict: Filtered products dictionary
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if feature is None:
        raise ValueError("Feature cannot be None")
    
    return {pid: product for pid, product in inventory.items() if feature in product["features"]}

def find_products_with_keyword(inventory, keyword):
    """
    Find products containing a keyword in their name or features.
    
    Args:
        inventory (dict): The product inventory
        keyword (str): Keyword to search for
    
    Returns:
        dict: Filtered products dictionary
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if keyword is None:
        raise ValueError("Keyword cannot be None")
    
    keyword = keyword.lower()
    return {pid: product for pid, product in inventory.items() 
            if keyword in product["name"].lower() or 
            any(keyword in feature.lower() for feature in product["features"])}

def update_product_price(inventory, product_id, new_price):
    """
    Update a product's price.
    
    Args:
        inventory (dict): The product inventory
        product_id (str): Product ID to update
        new_price (float): New price
    
    Returns:
        dict: Updated inventory
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if product_id is None:
        raise ValueError("Product ID cannot be None")
    if new_price is None or new_price < 0:
        raise ValueError("New price cannot be None or negative")
    
    if product_id not in inventory:
        raise ValueError(f"Product ID {product_id} not found")
    
    # Create a new dictionary with the updated price
    updated_inventory = inventory.copy()
    updated_inventory[product_id] = {**updated_inventory[product_id], "price": new_price}
    
    return updated_inventory

def update_stock_level(inventory, product_id, quantity_change):
    """
    Update a product's stock level.
    
    Args:
        inventory (dict): The product inventory
        product_id (str): Product ID to update
        quantity_change (int): Amount to change stock by (positive or negative)
    
    Returns:
        dict: Updated inventory
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if product_id is None:
        raise ValueError("Product ID cannot be None")
    if quantity_change is None:
        raise ValueError("Quantity change cannot be None")
    
    if product_id not in inventory:
        raise ValueError(f"Product ID {product_id} not found")
    
    # Create a new dictionary with the updated stock
    updated_inventory = inventory.copy()
    new_stock = updated_inventory[product_id]["stock"] + quantity_change
    
    if new_stock < 0:
        raise ValueError("Stock cannot be negative")
    
    updated_inventory[product_id] = {**updated_inventory[product_id], "stock": new_stock}
    
    return updated_inventory

def add_product_feature(inventory, product_id, new_feature):
    """
    Add a new feature to a product.
    
    Args:
        inventory (dict): The product inventory
        product_id (str): Product ID to update
        new_feature (str): New feature to add
    
    Returns:
        dict: Updated inventory
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if product_id is None:
        raise ValueError("Product ID cannot be None")
    if new_feature is None or new_feature == "":
        raise ValueError("New feature cannot be None or empty")
    
    if product_id not in inventory:
        raise ValueError(f"Product ID {product_id} not found")
    
    # Create a new dictionary with the updated features
    updated_inventory = inventory.copy()
    if new_feature not in updated_inventory[product_id]["features"]:
        updated_features = updated_inventory[product_id]["features"].copy()
        updated_features.append(new_feature)
        updated_inventory[product_id] = {**updated_inventory[product_id], "features": updated_features}
    
    return updated_inventory

def merge_inventories(existing_inventory, new_products):
    """
    Merge two inventory dictionaries with transformation.
    
    Args:
        existing_inventory (dict): The existing product inventory
        new_products (dict): New products to add
    
    Returns:
        dict: Merged inventory
    """
    if existing_inventory is None or new_products is None:
        raise ValueError("Inventories cannot be None")
    
    # Create a copy of the existing inventory
    merged_inventory = existing_inventory.copy()
    
    # Add new products with a "new_arrival" flag
    for pid, product in new_products.items():
        merged_inventory[pid] = {**product, "new_arrival": True}
    
    return merged_inventory

def calculate_category_counts(inventory):
    """
    Calculate the number of products in each category.
    
    Args:
        inventory (dict): The product inventory
    
    Returns:
        dict: Dictionary with categories as keys and counts as values
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    
    category_counts = {}
    for product in inventory.values():
        category = product["category"]
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1
    
    return category_counts

def calculate_total_inventory_value(inventory):
    """
    Calculate the total value of inventory (price * stock).
    
    Args:
        inventory (dict): The product inventory
    
    Returns:
        float: Total inventory value
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    
    return sum(product["price"] * product["stock"] for product in inventory.values())

def find_highest_rated_product(inventory):
    """
    Find the highest rated product.
    
    Args:
        inventory (dict): The product inventory
    
    Returns:
        tuple: (product_id, product_data) of the highest rated product
    """
    if inventory is None or not inventory:
        raise ValueError("Inventory cannot be None or empty")
    
    return max(inventory.items(), key=lambda item: item[1]["rating"])

def create_price_brackets(inventory):
    """
    Group products into price brackets.
    
    Args:
        inventory (dict): The product inventory
    
    Returns:
        dict: Dictionary with price brackets as keys and lists of product IDs as values
    """
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    
    price_brackets = {
        "budget": [],       # 0-3000
        "mid_range": [],    # 3000-10000
        "premium": []       # 10000+
    }
    
    for pid, product in inventory.items():
        price = product["price"]
        if price < 3000:
            price_brackets["budget"].append(pid)
        elif price < 10000:
            price_brackets["mid_range"].append(pid)
        else:
            price_brackets["premium"].append(pid)
    
    return price_brackets

def get_formatted_product(pid, product):
    """
    Format a product for display.
    
    Args:
        pid (str): Product ID
        product (dict): Product data
    
    Returns:
        str: Formatted product string
    """
    if product is None:
        raise ValueError("Product cannot be None")
    
    # Create a star rating representation
    stars = "★" * int(product["rating"]) + "☆" * (5 - int(product["rating"]))
    
    # Format features as comma-separated string
    features = ", ".join(product["features"])
    
    # Format the new arrival flag if present
    new_arrival = " [NEW]" if product.get("new_arrival", False) else ""
    
    # Return formatted string
    return (
        f"{pid} | {product['name']}{new_arrival} | {product['category']} | "
        f"₹{product['price']:.2f} | Stock: {product['stock']} | Rating: {stars} | {features}"
    )

def display_data(data, data_type):
    """
    Display formatted data based on data type.
    
    Args:
        data: Data to display (dict, tuple, etc.)
        data_type (str): Type of data being displayed
    """
    if data is None:
        print("No data to display.")
        return
    
    if data_type == "inventory" or data_type == "filtered":
        header = "\nCurrent Inventory:" if data_type == "inventory" else "\nFiltered Products:"
        print(header)
        
        if not data:
            print("No products to display.")
            return
        
        for pid, product in data.items():
            print(get_formatted_product(pid, product))
    
    elif data_type == "categories":
        print("\nProduct Categories:")
        for category, count in data.items():
            print(f"{category}: {count} products")
    
    elif data_type == "price_brackets":
        print("\nPrice Brackets:")
        for bracket, product_ids in data.items():
            print(f"{bracket}: {len(product_ids)} products")
            if product_ids:
                print(f"  Product IDs: {', '.join(product_ids)}")
    
    elif data_type == "highest_rated":
        print("\nHighest Rated Product:")
        pid, product = data
        print(get_formatted_product(pid, product))
    
    elif data_type == "inventory_value":
        print(f"\nTotal Inventory Value: ₹{data:.2f}")
    
    else:
        print(f"\n{data_type}:")
        print(data)

def main():
    """Main program function."""
    inventory, new_products = initialize_data()
    
    while True:
        # Show basic info about the inventory
        categories = set(product["category"] for product in inventory.values())
        
        print(f"\n===== ONLINE STORE MANAGEMENT SYSTEM =====")
        print(f"Total Products: {len(inventory)}")
        print(f"Categories: {', '.join(sorted(categories))}")
        
        print("\nMain Menu:")
        print("1. View Inventory")
        print("2. Filter Products")
        print("3. Update Products")
        print("4. Add New Products")
        print("5. View Statistics")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        if choice == "0":
            print("Thank you for using the Online Store Management System!")
            break
        
        elif choice == "1":
            display_data(inventory, "inventory")
        
        elif choice == "2":
            print("\nFilter Options:")
            print("1. Filter by Category")
            print("2. Filter by Price Range")
            print("3. Filter by Availability")
            print("4. Filter by Feature")
            print("5. Search by Keyword")
            filter_choice = input("Select filter option (1-5): ")
            
            if filter_choice == "1":
                category = input("Enter category to filter by: ")
                filtered = filter_by_category(inventory, category)
                display_data(filtered, "filtered")
            
            elif filter_choice == "2":
                try:
                    min_price = float(input("Enter minimum price: ₹"))
                    max_price = float(input("Enter maximum price: ₹"))
                    filtered = filter_by_price_range(inventory, min_price, max_price)
                    display_data(filtered, "filtered")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif filter_choice == "3":
                try:
                    min_stock = int(input("Enter minimum stock level: "))
                    filtered = filter_by_availability(inventory, min_stock)
                    display_data(filtered, "filtered")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif filter_choice == "4":
                feature = input("Enter feature to filter by: ")
                filtered = filter_by_feature(inventory, feature)
                display_data(filtered, "filtered")
            
            elif filter_choice == "5":
                keyword = input("Enter keyword to search for: ")
                filtered = find_products_with_keyword(inventory, keyword)
                display_data(filtered, "filtered")
            
            else:
                print("Invalid choice.")
        
        elif choice == "3":
            print("\nUpdate Options:")
            print("1. Update Product Price")
            print("2. Update Stock Level")
            print("3. Add Product Feature")
            update_choice = input("Select update option (1-3): ")
            
            if update_choice == "1":
                try:
                    pid = input("Enter product ID to update: ")
                    new_price = float(input("Enter new price: ₹"))
                    inventory = update_product_price(inventory, pid, new_price)
                    print(f"Price updated for product {pid}.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif update_choice == "2":
                try:
                    pid = input("Enter product ID to update: ")
                    change = int(input("Enter quantity change (use negative for sales): "))
                    inventory = update_stock_level(inventory, pid, change)
                    print(f"Stock updated for product {pid}.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif update_choice == "3":
                try:
                    pid = input("Enter product ID to update: ")
                    feature = input("Enter new feature to add: ")
                    inventory = add_product_feature(inventory, pid, feature)
                    print(f"Feature added to product {pid}.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            else:
                print("Invalid choice.")
        
        elif choice == "4":
            try:
                print("\nAdding new products to inventory...")
                inventory = merge_inventories(inventory, new_products)
                print(f"{len(new_products)} new products added to inventory.")
                # Clear new_products after adding
                new_products = {}
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "5":
            print("\nStatistics Options:")
            print("1. Category Counts")
            print("2. Total Inventory Value")
            print("3. Highest Rated Product")
            print("4. Price Brackets")
            stats_choice = input("Select statistics option (1-4): ")
            
            if stats_choice == "1":
                category_counts = calculate_category_counts(inventory)
                display_data(category_counts, "categories")
            
            elif stats_choice == "2":
                total_value = calculate_total_inventory_value(inventory)
                display_data(total_value, "inventory_value")
            
            elif stats_choice == "3":
                highest_rated = find_highest_rated_product(inventory)
                display_data(highest_rated, "highest_rated")
            
            elif stats_choice == "4":
                price_brackets = create_price_brackets(inventory)
                display_data(price_brackets, "price_brackets")
            
            else:
                print("Invalid choice.")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()