#check if the number is prime or not
num = int(input("Enter any number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 👉 Prime number wo number hai jo sirf 2 factors rakhta hai: 1 aur khud apna.

# Matlab usko divide karne par remainder 0 sirf 1 aur us number khud se hi aayega.

# Agar kisi aur number se divide ho gaya toh prime nahi hai (wo composite number hai).

# Special case: 1 prime nahi hota (kyunki uska sirf ek factor hai – 1 khud).

# Ab tujhne diya set:

# 𝑈={1,3,4,5,6,7,8,9,10,11,12}
# U={1,3,4,5,6,7,8,9,10,11,12}

# Check karte hain ek ek:

# 1 → prime nahi (sirf ek factor)

# 3 → prime (factors: 1,3)

# 4 → not prime (factors: 1,2,4)

# 5 → prime (factors: 1,5)

# 6 → not prime (factors: 1,2,3,6)

# 7 → prime (factors: 1,7)

# 8 → not prime (factors: 1,2,4,8)

# 9 → not prime (factors: 1,3,9)

# 10 → not prime (factors: 1,2,5,10)

# 11 → prime (factors: 1,11)

# 12 → not prime (factors: 1,2,3,4,6,12)

# 👉 Toh Prime numbers = {3,5,7,11}

# 👉 Prime number wo hota hai jo sirf 2 numbers se divide hota hai — 1 aur khud se.
# 👉 Agar koi number 2 ya usse zyada numbers se divide ho jaye → prime nahi hai.

# Ab tujhne diya set:

# 𝑈
# =
# {
# 1
# ,
# 2
# ,
# 3
# ,
# 4
# ,
# 5
# ,
# 6
# ,
# 7
# ,
# 8
# ,
# 9
# ,
# 10
# ,
# 11
# ,
# 12
# }
# U={1,2,3,4,5,6,7,8,9,10,11,12}

# Check karte hain simple:

# 1 → prime nahi hota (sirf 1 se hi divide hota hai).

# 2 → prime ✔️ (2 ko sirf 1 aur 2 divide karte hain).

# 3 → prime ✔️ (1 aur 3 se hi divide hota hai).

# 4 → prime nahi ❌ (1,2,4 se divide hota hai).

# 5 → prime ✔️ (1 aur 5 se hi divide hota hai).

# 6 → prime nahi ❌ (1,2,3,6 se divide hota hai).

# 7 → prime ✔️ (1 aur 7 se hi divide hota hai).

# 8 → prime nahi ❌ (1,2,4,8 se divide hota hai).

# 9 → prime nahi ❌ (1,3,9 se divide hota hai).

# 10 → prime nahi ❌ (1,2,5,10 se divide hota hai).

# 11 → prime ✔️ (1 aur 11 se hi divide hota hai).

# 12 → prime nahi ❌ (1,2,3,4,6,12 se divide hota hai).

