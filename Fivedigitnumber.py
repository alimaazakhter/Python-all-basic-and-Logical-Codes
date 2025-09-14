#Write a program to find how many digit number 

num = int(input("Enter any five digit number: "))
if (num>=0) and (num<=9):
    print("The number is the Single digit number: ", num)
elif (num>9) and (num<=99):
    print("The number is two digit number: ", num)
elif (num>99) and (num<=999):
    print("The number is three digit number: ", num)     
elif (num>999) and (num<=9999):
    print("The number is four digit number: ", num)
elif (num>9999) and (num<=99999):
    print("The number is five digit number", num)
else:
    print("The number is Six digit number:", num)   
