# Smart Grocery Store Management System

A beginner-friendly Python application designed to manage grocery store products, inventory, customer sales, and daily store reports.

## Repository Information

**Repository Name:** `python-smart-grocery-store-management-system`

**Programming Language:** Python 3

## Project Overview

The Smart Grocery Store Management System is a menu-driven Python application that helps a grocery store manage its daily operations.

It allows users to add new products, view available products, search for products, update stock quantities, process customer sales, maintain sales records, and generate a complete store report.

## Features

### 1. Product Management
- Store multiple products using a list of dictionaries.
- Maintain product ID, name, category, price, and available stock.
- Prevent duplicate product IDs.

### 2. Add New Products
- Collect product information from the user.
- Create a dictionary for each product.
- Store products using the `append()` method.

### 3. View All Products
- Display all available products.
- Show product ID, name, category, price, and stock quantity.

### 4. Search Products
- Search for products using their name or ID.
- Display complete product details.
- Show a message if the product is not found.

### 5. Update Product Stock
- Search for a product using its ID.
- Add new stock or set a new stock quantity.
- Display updated stock information.

### 6. Process Customer Sales
- Search for products using their ID.
- Check product availability and stock quantity.
- Calculate the total purchase amount.
- Deduct the sold quantity from available stock.
- Display a purchase summary.
- Prevent sales when sufficient stock is unavailable.

### 7. Sales Records
- Maintain a separate list of dictionaries for completed sales.
- Store product ID, product name, quantity sold, and total amount.
- Display all completed sales transactions.

### 8. Generate Store Report
- Display the total number of products.
- Calculate total available stock.
- Count sales transactions.
- Calculate total revenue.
- Identify products with stock below 5 units.
- Find products with the highest and lowest prices.

## Python Concepts Covered

The following Python concepts are demonstrated in this project:

- Variables and data types
- Lists and dictionaries
- List of dictionaries
- Dictionary keys and values
- Functions (`def`)
- Function calls and parameters
- `return` statement
- `for` and `while` loops
- Conditional statements (`if`, `elif`, `else`)
- Comparison and logical operators
- List methods (`append()`)
- String methods (`strip()`, `lower()`, `isdigit()`, `replace()`)
- Built-in functions (`len()`, `max()`, `min()`)
- Input validation
- Counters and accumulators
- Menu-driven programming

## Project Structure

```text
python-smart-grocery-store-management-system/
│
├── smart_grocery_store.py
└── README.md