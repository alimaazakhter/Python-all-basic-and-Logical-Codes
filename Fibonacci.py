n = int(input("Enter any number: "))
a = 0
b = 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")   # har step pe current number print karo
    fact = a + b
    a = b
    b = fact
