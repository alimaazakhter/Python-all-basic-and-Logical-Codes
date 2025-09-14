#Write a program to check the Letter is vowel or not 
character = input("Enter any letter here : ")
if (character in "aeiou") or (character in "AEIOU"):
    print("The letter is Vowel", character)
else:
    print("The letter is not vowel") 
