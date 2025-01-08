#billing program  
while True:
    Name = input("Enter customer's name :")
    total = 0

    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter Amount :"))
        quantity = float(input("Enter quantity :"))
        total += amount * quantity
        repeat = input("do you want to add more items? (yes/no): ")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name", Name)
    print("Total amount to be paid", amount)
    print("-"*40)
    print("*****************HAPPY SHOPPING*********************")

    repeat1 = input("do you want to repeat this program? (yes/no) :")
    if repeat1 =="no" or repeat1 =="No":
        break
