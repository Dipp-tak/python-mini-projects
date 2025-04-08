def display_menu(menu):
    print("Welcome to my python restaurant")
    print("Menu:")
    for item,price in menu.items():
        print(f"{item.capitalize()}:Rs{price}")

def take_order(menu):

    order_value = 0

    item1 = str(input("What would you like to order?\nEnter Your order:")).strip().lower()

    if item1 in menu:
        order_value += menu[item1]
        print(f"Your {item1} has been added to your order")
        customer_choice = str(input("Do you need anything else?(Yes/No):")).strip().lower()

        if customer_choice == 'yes':
            while(True):
                customer_next_order = str(input("Enter your next rrder (or type 'done' to finish):\n")).strip().lower()

                if customer_next_order in menu:
                    order_value += menu[customer_next_order]
                    print(f"Your next order {customer_next_order} is confirmed")
                elif customer_next_order == 'done':
                    break
                else:
                    print("Sorry! We don't have that item")

        elif customer_choice == 'no':
            pass
        else:
            print("Invalid input.")

    else:
        print("Sorry! we don't have that item.")

    return order_value

def main():
    menu = {
    'pizza':80,
    'burger':90,
    'pasta':70,
    'coffee':40,
    'tea':30,
    'juice':45,
    'biriyani':120,
    'water bottle':20
    }

    display_menu(menu)
    total_bill = take_order(menu)
    
    if total_bill > 0:
        print(f"Your total bill is Rs{total_bill}")
        print("Thank you for visting my restaurant!")
    else:
        print("Thank you for visiting my restaurant!")
                
if __name__ =='__main__':
    main()
