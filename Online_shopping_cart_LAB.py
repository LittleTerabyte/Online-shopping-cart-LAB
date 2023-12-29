
# Classes 
class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price                                        
        self.item_quantity = item_quantity                                  
        self.item_description = item_description

    def print_item_cost(self):
        print(f"{self.item_name.capitalize()} x{self.item_quantity} @ ${self.item_price:.2f} = ${self.item_price * self.item_quantity:.2f}")
    
    def print_item_description(self):
        print(f"{self.item_name.capitalize()}: {self.item_description.capitalize()}.")
        
class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item):
        # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
        self.item = item
        self.cart_items.append(item)
        
    def remove_item(self, item_name):
        # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")  
    
    def modify_item(self, item):
        # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
        found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                found = True
                if item.item_description != "none":
                    self.cart_items[i].item_description = item.item_description
                if item.item_price != 0:
                    self.cart_items[i].item_price = item.item_price
                if item.item_quantity != 0:
                    self.cart_items[i].item_quantity = item.item_quantity
                break
            
    def get_num_items_in_cart(self):
         #Returns quantity of all items in cart. Has no parameters. 
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items
    
    def get_cost_of_cart(self):
        #Determines and returns the total cost of items in cart. Has no parameters.
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_quantity * item.item_price)
        return total_cost   
    
    def print_total(self):
        #Outputs total of objects in cart. If cart is empty, output this message: SHOPPING CART IS EMPTY.
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name.capitalize()}'s Shopping Cart - {self.current_date.capitalize()}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            print()
            for item in self.cart_items:
                item.print_item_cost()
            print()
            print(f"Total: ${self.get_cost_of_cart():.2f}")
            
            
    def print_descriptions(self):
        #Prints each item's description. Has no parameters. Does not return anything.
        print(f"{self.customer_name.capitalize()}'s Shopping Cart - {self.current_date.capitalize()}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            item.print_item_description()
            

# Functions
def print_menu(customer_Cart):
    # Prints menu
    menu = ("\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n")

    command = ""
    while command != "q":
        print(menu)
        command = input("Choose an option:\n").lower()
        while command != "a" and command != "o" and command != "i" and command != "r" and command != "c" and command != "q":
            command = input("Please choose an valid option:\n")
        if command == "a":
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n").lower()
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            customer_Cart.add_item(item)
        elif command == "o":
            print("\nOUTPUT SHOPPING CART")
            customer_Cart.print_total()
        elif command == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            customer_Cart.print_descriptions()
        elif command == "r":
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n").lower()
            customer_Cart.remove_item(item_name)
            print(f"{item_name.capitalize()} removed from cart.")
        elif command == "c":
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n").lower()
            item_quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(item_name, 0, item_quantity)
            customer_Cart.modify_item(item)
            print(f"{item_name.capitalize()}'s quantity changed to {item_quantity}.")
        elif command == "q":
            print("\nGOODBYE")
            break

        

# MAIN 
if __name__ == "__main__":
    customer_name = input("\nEnter customer's name:\n").capitalize()
    print()
    current_date = input("Enter today's date:\n[Month] [Day], [Year]\n").capitalize()
    customer1 = ShoppingCart(customer_name, current_date)
    print(f"\nCustomer name: {customer1.customer_name}")
    print(f"Today's date: {customer1.current_date}")

    print_menu(customer1)   
