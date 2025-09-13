#Marksheet

rno= int(input("Enter your roll.no : "))
name = input("Enter your name: ")
dept = input("Enter your department: ")
sem = input("Enter your sem: ")

if (rno>=70):
    Div = 'A'
else:
    Div = 'B'

pps_t= int(input("Enter your PPS_theory marks: "))
pps_p=int(input("Enter your PPS_practical marks: "))
Lf_p=int(input("Enter your LF_practical marks: "))
Wdf_p=int(input("Enter your WDF_practical marks: "))
Rdbms_t=int(input("Enter your RDBMS_theory marks:"))
Rdbms_p=int(input("Enter your RDBMS_practical marks:"))
Py_t=int(input("Enter your Py_theory marks:"))
Py_p=int(input("Enter your Py_practical marks:"))
Iks_t=int(input("Enter your IKS_theory marks:"))

total = pps_t+pps_p+Lf_p+Wdf_p+Rdbms_t+Rdbms_p+Py_t+Py_p+Iks_t
percentage= total/ 9 

if percentage >=90:
    grade='A+'
elif percentage >=80:     
    grade='A'
elif percentage >=70:
    grade='B'
elif percentage >=60:
    grade='C'
elif percentage >=50:
    grade='D'
else:
    grade='Fail'

# Print Marksheet

print("\n===============Marksheet=============")
print("Roll no     : ", rno)
print("Name        : ", name)
print("Department  : ", dept)   
print("Semester    : ", sem)
print("---------------------------------")

print("PPS(Theory)  : ", pps_t)   
print("PPS(Practical)  : ", pps_p)
print("LF(Practical)  : ", Lf_p)
print("WDF(Practical)  : ", Wdf_p)
print("RDBMS(Theory)  : ", Rdbms_t)
print("RDBMS(Practical)  : ", Rdbms_p)
print("Python(Theory)  : ", Py_t)
print("Python(Practical)  : ", Py_p)
print("IKS(Theory)  : ", Iks_t)

print("----------------------------------")

print("Total Marks :", total, "/900")
print("Percentage  :", round(percentage,2), "%")
print("Grade       :", grade)

if percentage >= 50:
        print("------------------------Congratulations! You have passed.---------------------------")
else:
        print("------------------------Sorry, you didn't clear the exam.---------------------------")





    
        
        