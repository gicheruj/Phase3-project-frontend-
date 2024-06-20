import sys
from models import Category, Supplier, Product, Order
from utils import clear_screen

def main_menu():
    while True:
        clear_screen()
        print("Inventory Manager\n")
        print("1. Manage Categories")
        print("2. Manage Suppliers")
        print("3. Manage Products")
        print("4. Manage Orders")
        print("5. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            manage_categories()
        elif choice == '2':
            manage_suppliers()
        elif choice == '3':
            manage_products()
        elif choice == '4':
            manage_orders()
        elif choice == '5':
            sys.exit("Exiting...")
        else:
            input("Invalid choice. Press Enter to continue...")

def manage_categories():
    while True:
        clear_screen()
        print("Manage Categories\n")
        print("1. Add Category")
        print("2. Delete Category")
        print("3. View All Categories")
        print("4. Search Category")
        print("5. Return to Main Menu")
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            add_category()
        elif choice == '2':
            delete_category()
        elif choice == '3':
            view_all_categories()
        elif choice == '4':
            search_category()
        elif choice == '5':
            return
        else:
            input("Invalid choice. Press Enter to continue...")

def add_category():
    clear_screen()
    print("Add Category\n")
    name = input("Enter category name: ")
    Category(name=name).save()
    input("\nCategory added successfully. Press Enter to continue...")

def delete_category():
    clear_screen()
    print("Delete Category\n")
    name = input("Enter category name to delete: ")
    Category.objects(name=name).delete()
    input("\nCategory deleted successfully. Press Enter to continue...")

def view_all_categories():
    clear_screen()
    print("All Categories\n")
    categories = Category.objects()
    for category in categories:
        print(category.name)
    input("\nPress Enter to continue...")

def search_category():
    clear_screen()
    print("Search Category\n")
    name = input("Enter category name to search: ")
    category = Category.objects(name=name).first()
    if category:
        print(f"Category found: {category.name}")
    else:
        print("Category not found.")
    input("\nPress Enter to continue...")

def manage_suppliers():
    while True:
        clear_screen()
        print("Manage Suppliers\n")
        print("1. Add Supplier")
        print("2. Delete Supplier")
        print("3. View All Suppliers")
        print("4. Search Supplier")
        print("5. Return to Main Menu")
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            add_supplier()
        elif choice == '2':
            delete_supplier()
        elif choice == '3':
            view_all_suppliers()
        elif choice == '4':
            search_supplier()
        elif choice == '5':
            return
        else:
            input("Invalid choice. Press Enter to continue...")

def add_supplier():
    clear_screen()
    print("Add Supplier\n")
    name = input("Enter supplier name: ")
    Supplier(name=name).save()
    input("\nSupplier added successfully. Press Enter to continue...")

def delete_supplier():
    clear_screen()
    print("Delete Supplier\n")
    name = input("Enter supplier name to delete: ")
    Supplier.objects(name=name).delete()
    input("\nSupplier deleted successfully. Press Enter to continue...")

def view_all_suppliers():
    clear_screen()
    print("All Suppliers\n")
    suppliers = Supplier.objects()
    for supplier in suppliers:
        print(supplier.name)
    input("\nPress Enter to continue...")

def search_supplier():
    clear_screen()
    print("Search Supplier\n")
    name = input("Enter supplier name to search: ")
    supplier = Supplier.objects(name=name).first()
    if supplier:
        print(f"Supplier found: {supplier.name}")
    else:
        print("Supplier not found.")
    input("\nPress Enter to continue...")

def manage_products():
    while True:
        clear_screen()
        print("Manage Products\n")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. View All Products")
        print("4. Search Product")
        print("5. Update Stock")
        print("6. Return to Main Menu")
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            add_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            view_all_products()
        elif choice == '4':
            search_product()
        elif choice == '5':
            update_stock()
        elif choice == '6':
            return
        else:
            input("Invalid choice. Press Enter to continue...")

def add_product():
    clear_screen()
    print("Add Product\n")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    category_name = input("Enter product category: ")
    category = Category.objects(name=category_name).first()
    if category:
        Product(name=name, price=price, category=category).save()
        input("\nProduct added successfully. Press Enter to continue...")
    else:
        input("\nCategory does not exist. Press Enter to continue...")

def delete_product():
    clear_screen()
    print("Delete Product\n")
    name = input("Enter product name to delete: ")
    Product.objects(name=name).delete()
    input("\nProduct deleted successfully. Press Enter to continue...")

def view_all_products():
    clear_screen()
    print("All Products\n")
    products = Product.objects()
    for product in products:
        print(product.name, "-", product.price)
    input("\nPress Enter to continue...")

def search_product():
    clear_screen()
    print("Search Product\n")
    name = input("Enter product name to search: ")
    product = Product.objects(name=name).first()
    if product:
        print(f"Product found: {product.name} - {product.price}")
    else:
        print("Product not found.")
    input("\nPress Enter to continue...")

def update_stock():
    clear_screen()
    print("Update Stock\n")
    name = input("Enter product name to update stock: ")
    product = Product.objects(name=name).first()
    if product:
        quantity = int(input("Enter quantity to add to stock: "))
        product.stock += quantity
        product.save()
        input("\nStock updated successfully. Press Enter to continue...")
    else:
        input("\nProduct not found. Press Enter to continue...")

def manage_orders():
    while True:
        clear_screen()
        print("Manage Orders\n")
        print("1. Add Order")
        print("2. Delete Order")
        print("3. View All Orders")
        print("4. Search Order")
        print("5. Return to Main Menu")
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            add_order()
        elif choice == '2':
            delete_order()
        elif choice == '3':
            view_all_orders()
        elif choice == '4':
            search_order()
        elif choice == '5':
            return
        else:
            input("Invalid choice. Press Enter to continue...")

def add_order():
    pass  # Implement functionality to add an order

def delete_order():
    pass  # Implement functionality to delete an order

def view_all_orders():
    pass  # Implement functionality to view all orders

def search_order():
    pass  # Implement functionality to search for an order

if __name__ == "__main__":
    main_menu()

