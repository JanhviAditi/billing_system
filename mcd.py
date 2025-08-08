class McD:
    def __init__(self):
        self.choice = 0
        self.category = 0
        #self.option = 0
        self.quantity = 0

a = 0.00
total = 0.00

def display_menu():
    print("\n\t\t\t======Welcome to McDonald's======\n")
    print("\n\n===MENU===\n\n")

def options():
    print("1. Burgers(5)\n2. Fries(2)\n3. Wraps(3)\n4. Desserts(4)\n5. Beverages(3)\n\n")
    print("What would you like to have today? : ")

def menu(order):
    options()
    order.choice = int(input())

    if order.choice == 1:
        print("\n1. Chicken Mc Maharaja(non-veg) - ₹ 255.32\n2. Mc Maharaja(veg) - ₹ 235.32\n3. Mc Veggie(veg) - ₹ 170.32\n4. Paneer Thikka Burger(veg) - ₹ 185.32\n5. Chicken Burger(non-veg) - ₹ 195.32\n6. Mc Aloo Tikki(veg) - ₹ 70.43\n\n")
    elif order.choice == 2:
        print("\n1. Regular Fries - ₹ 60.23\n2. Peri Peri Fries - ₹ 86.34\n\n")
    elif order.choice == 3:
        print("\n1. Big Spicy Chicken Wrap - ₹ 185.42\n2. Big Spicy Paneer Wrap - ₹ 170.32\n3. Veggie Wrap - ₹ 165.32\n\n")
    elif order.choice == 4:
        print("\n1. Oreo Mc Flurry(veg) - ₹ 160.23\n2. Choco Lava Cake(veg) - ₹ 109.34\n3. Choco Lava Cake(non-veg) - ₹ 99.32\n4. Softie - ₹ 35\n\n")
    elif order.choice == 5:
        print("\n1. Water - ₹ 30.34\n2. Coke - ₹ 40\n3. Sprite - ₹45.43\n4. Diet Coke - ₹ 255.32\n\n")

    print("------------------------------")
    order.category = int(input("Please Specify = "))
    order.quantity = int(input("Please enter the quantity = "))
    total_cost(order)
    print("\n-------------------------------")
    finalize_order(order)

def total_cost(order):
    global total
    if order.choice == 1:
        if order.category == 1:
            total = 255.32 * order.quantity
        elif order.category == 2:
            total = 235.32 * order.quantity
        elif order.category == 3:
            total = 170.32 * order.quantity
        elif order.category == 4:
            total = 185.32 * order.quantity
        elif order.category == 5:
            total = 195.32 * order.quantity
        elif order.category == 6:
            total = 70.43 * order.quantity
    elif order.choice == 2:
        if order.category == 1:
            total = 60.23 * order.quantity
        elif order.category == 2:
            total = 86.34 * order.quantity
    elif order.choice == 3:
        if order.category == 1:
            total = 185.42 * order.quantity
        elif order.category == 2:
            total = 170.32 * order.quantity
        elif order.category == 3:
            total = 165.32 * order.quantity
    elif order.choice == 4:
        if order.category == 1:
            total = 160.23 * order.quantity
        elif order.category == 2:
            total = 109.34 * order.quantity
        elif order.category == 3:
            total = 99.32 * order.quantity
        elif order.category == 4:
            total = 35.0 * order.quantity
    elif order.choice == 5:
        if order.category == 1:
            total = 30.34 * order.quantity
        elif order.category == 2 or order.category == 3:
            total = 40.0 * order.quantity
        elif order.category == 4:
            total = 45.43 * order.quantity

    print("Total cost = {:.2f}".format(total))
    global a
    a += total

def finalize_order(order):
    print("\n Anything else?\n 1.Yes\n 2.No\n 3.Cancel Order")
    order.option = int(input("\n\nEnter your choice : "))

    if order.option == 1:
        menu(order)
    elif order.option == 2:
        print("---------------")
        print("\nTotal Amount: Rs. {:.2f}".format(a))
        print("---------------")
        print("\n\nThank You!!\nPlease Wait while we prepare your order.\nEnjoy your meal :)\n-----------------------------------------------------")
    elif order.option == 3:
        main()
        total = 0
        a = 0

"""def cancelorder():
    print("do you want to cancel your order")
    print("1.Yes 2.No")
    userinput=input()
    if(userinput=='1'):
        print("order cancelled")
    else:
        print("proceed with order")"""


def main():
    display_menu()
    order = McD()
    menu(order)

if __name__ == "__main__":
    main()
