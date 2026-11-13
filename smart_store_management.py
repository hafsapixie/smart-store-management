
# Smart Grocery Store Management System

print("=" * 45)
print("       SMART GROCERY STORE SYSTEM")
print("=" * 45)

# Step 1: Create empty lists
products = []
sales_records = []


# Function 1: Add a new product
def add_product():

    print("\n----- Add New Product -----")

    product_id = input("Enter product ID: ")

    # Check for duplicate product ID
    for product in products:

        if product["id"] == product_id:
            print("Product ID already exists!")
            return

    product_name = input("Enter product name: ")
    category = input("Enter product category: ")

    # Validate product price
    while True:
        price = input("Enter product price: ")

        if price.replace(".", "", 1).isdigit():
            price = float(price)
            break

        else:
            print("Invalid price! Enter a valid number.")

    # Validate available stock
    while True:
        stock = input("Enter available stock: ")

        if stock.isdigit():
            stock = int(stock)
            break

        else:
            print("Invalid stock! Enter a whole number.")

    # Create product dictionary
    new_product = {
        "id": product_id,
        "name": product_name,
        "category": category,
        "price": price,
        "stock": stock
    }

    # Add product to products list
    products.append(new_product)

    print("\nProduct added successfully!")


# Function 2: Display all products
def view_products():

    print("\n----- Available Products -----")

    if len(products) == 0:
        print("No products available.")

    else:
        for product in products:

            print("\nProduct ID:", product["id"])
            print("Product Name:", product["name"])
            print("Category:", product["category"])
            print("Price: Rs.", product["price"])
            print("Available Stock:", product["stock"])


# Function 3: Search for a product
def search_product():

    print("\n----- Search Product -----")

    search_value = input("Enter product name or ID: ").strip()

    found = False

    for product in products:

        if (product["id"] == search_value or
                product["name"].lower() == search_value.lower()):

            print("\nProduct Found!")
            print("Product ID:", product["id"])
            print("Product Name:", product["name"])
            print("Category:", product["category"])
            print("Price: Rs.", product["price"])
            print("Available Stock:", product["stock"])

            found = True

    if found == False:
        print("Product not found.")


# Function 4: Update product stock
def update_stock():

    print("\n----- Update Product Stock -----")

    product_id = input("Enter product ID: ")

    found = False

    for product in products:

        if product["id"] == product_id:

            found = True

            print("Product Name:", product["name"])
            print("Current Stock:", product["stock"])

            print("\n1. Add Stock")
            print("2. Set New Stock Quantity")

            choice = input("Enter your choice: ")

            if choice == "1":

                quantity = input("Enter quantity to add: ")

                if quantity.isdigit():
                    product["stock"] = product["stock"] + int(quantity)
                    print("Stock added successfully!")

                else:
                    print("Invalid quantity!")

            elif choice == "2":

                quantity = input("Enter new stock quantity: ")

                if quantity.isdigit():
                    product["stock"] = int(quantity)
                    print("Stock updated successfully!")

                else:
                    print("Invalid quantity!")

            else:
                print("Invalid choice!")

            if choice == "1" or choice == "2":
                print("Updated Stock:", product["stock"])

            break

    if found == False:
        print("Product not found.")


# Function 5: Process customer sale
def process_sale():

    print("\n----- Process Customer Sale -----")

    product_id = input("Enter product ID: ")

    found = False

    for product in products:

        if product["id"] == product_id:

            found = True

            print("Product Name:", product["name"])
            print("Available Stock:", product["stock"])
            print("Price: Rs.", product["price"])

            quantity = input("Enter purchase quantity: ")

            if quantity.isdigit():

                quantity = int(quantity)

                if quantity <= 0:
                    print("Quantity must be greater than zero.")

                elif quantity <= product["stock"]:

                    # Calculate total amount
                    total_amount = quantity * product["price"]

                    # Deduct sold quantity from stock
                    product["stock"] = product["stock"] - quantity

                    # Create sales record
                    sale = {
                        "id": product["id"],
                        "name": product["name"],
                        "quantity": quantity,
                        "total": total_amount
                    }

                    # Store completed sale
                    sales_records.append(sale)

                    print("\nSale completed successfully!")
                    print("Product:", product["name"])
                    print("Quantity Sold:", quantity)
                    print("Total Amount: Rs.", total_amount)
                    print("Remaining Stock:", product["stock"])

                else:
                    print("Insufficient stock!")
                    print("Available Stock:", product["stock"])

            else:
                print("Invalid quantity! Enter numbers only.")

            break

    if found == False:
        print("Product not found.")


# Function 6: Display sales records
def view_sales():

    print("\n----- Sales Records -----")

    if len(sales_records) == 0:
        print("No sales records available.")

    else:
        for sale in sales_records:

            print("\nProduct ID:", sale["id"])
            print("Product Name:", sale["name"])
            print("Quantity Sold:", sale["quantity"])
            print("Total Amount: Rs.", sale["total"])


# Function 7: Generate store report
def generate_report():

    print("\n========== STORE REPORT ==========")

    total_products = len(products)

    total_stock = 0

    for product in products:
        total_stock = total_stock + product["stock"]

    total_transactions = len(sales_records)

    total_revenue = 0

    for sale in sales_records:
        total_revenue = total_revenue + sale["total"]

    print("Total Products:", total_products)
    print("Total Available Stock:", total_stock)
    print("Total Sales Transactions:", total_transactions)
    print("Total Revenue: Rs.", total_revenue)

    # Display products with stock below 5
    print("\nProducts with Low Stock:")

    low_stock_found = False

    for product in products:

        if product["stock"] < 5:
            print(product["name"], "-", product["stock"], "units")
            low_stock_found = True

    if low_stock_found == False:
        print("No products with low stock.")

    # Find highest and lowest priced products
    if len(products) > 0:

        highest_price = max(product["price"] for product in products)
        lowest_price = min(product["price"] for product in products)

        print("\nProduct with Highest Price:")

        for product in products:

            if product["price"] == highest_price:
                print(product["name"], "- Rs.", product["price"])

        print("\nProduct with Lowest Price:")

        for product in products:

            if product["price"] == lowest_price:
                print(product["name"], "- Rs.", product["price"])

    else:
        print("\nNo products available for price comparison.")

    print("==================================")


# Step 2: Main application menu
while True:

    print("\n========== MAIN MENU ==========")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        process_sale()

    elif choice == "6":
        view_sales()

    elif choice == "7":
        generate_report()

    elif choice == "8":
        print("\nThank you for using Smart Grocery Store System!")
        break

    else:
        print("Invalid choice! Please select between 1 and 8.")
