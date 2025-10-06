menu ={
    'Pizza':50,
    'Pasta':70,
    'Burger':80,
    'Coffee':40,
    'Cold drink':30,
}
print("Welcome to Satpute restaurant")
print("Pizza: Rs50\nPasta:Rs70\nBurger:Rs80\nCoffee:Rs40\nCold drink:Rs30")

order_total=0

item_1=input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Please add Another item is available in the menu {item_1}")

another_order=input("Do you want to add another item?(Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name second item=")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available in menu!")

print(f"The total amount of your bill is {order_total}")
