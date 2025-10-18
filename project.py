class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cafe:
    def __init__(self):
        self.menu = []
        self.order = []

    def add_menu_item(self, name, price):
        self.menu.append(MenuItem(name, price))

    def show_menu(self):
        print("\n--- Cafe Menu ---")
        for idx, item in enumerate(self.menu, 1):
            print(f"{idx}. {item.name} - ${item.price:.2f}")

    def take_order(self):
        self.show_menu()
        while True:
            choice = input("\nEnter item number to add to order (or 'done' to finish): ")
            if choice.lower() == 'done':
                break
            if choice.isdigit() and 1 <= int(choice) <= len(self.menu):
                self.order.append(self.menu[int(choice)-1])
                print(f"Added {self.menu[int(choice)-1].name} to order.")
            else:
                print("Invalid choice.")

    def show_bill(self):
        print("\n--- Bill ---")
        total = 0
        for item in self.order:
            print(f"{item.name} - ${item.price:.2f}")
            total += item.price
        print(f"Total: ${total:.2f}")

# Sample run
cafe = Cafe()
cafe.add_menu_item("Espresso", 2.5)
cafe.add_menu_item("Cappuccino", 3.0)
cafe.add_menu_item("Tea", 1.5)
cafe.add_menu_item("Croissant", 2.0)

cafe.take_order()
cafe.show_bill()
