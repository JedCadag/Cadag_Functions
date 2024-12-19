menu = {
    "Burger": 100,
    "Fries": 50,
    "Soda": 30
}

def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ₱{price}")

def get_order():
    while True:
        order = input("Enter the item you want to order: ")
        if order in menu:
            return order
        else:
            print("Item not found on the menu. Please try again.")

def calculate_total(order):
    return menu[order]

def process_payment(total):
    while True:
        try:
            cash_rendered = float(input(f"Total cost is ₱{total}. Enter cash rendered: "))
            if cash_rendered >= total:
                change = cash_rendered - total
                print(f"Payment accepted. Your change is ₱{change:.2f}.")
                break
            else:
                print("Insufficient amount. Please enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main():
    display_menu()
    order = get_order()
    total = calculate_total(order)
    process_payment(total)

if __name__ == "__main__":
    main()
