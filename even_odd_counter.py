num = int(input("Enter any number: "))
esum = 0
osum = 0
evenlist = []
oddlist = []
ecount = 0
ocount = 0

for i in range(1, num+1):
    if i % 2 == 0:   # i ke basis pe check kar
        evenlist.append(i)
        esum += i
        ecount += 1
    else:
        oddlist.append(i)
        osum += i
        ocount += 1

print("evenlist:", evenlist)
print("total of even numbers:", esum)
print("total count of even numbers:", ecount)

print("oddlist:", oddlist)
print("total of odd numbers:", osum)
print("total count of odd numbers:", ocount)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Append()

#Python me append() ka matlab hota hai list ke end me ek naya element add karna.

# eg: 
# numbers = []   # ek empty list
# numbers.append(5)   # list ke end me 5 add hoga
# numbers.append(10)  # list ke end me 10 add hoga
# numbers.append(20)  # list ke end me 20 add hoga

# print(numbers)
