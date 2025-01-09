#check if the number is prime or not
num = int(input("Enter any number :"))
if num <=1:
    print("It is not a prime number")
else:
    for i in range(2,11):
        if num%i == 0:
            print("It is not a prime number")
            break
        else:
            print("It is a prime number")   
            break 