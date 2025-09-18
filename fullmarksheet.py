# Marksheet Program in Python

# Input basic details
rno = int(input("Enter Roll No: "))

if rno > 0:
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    sem = input("Enter Semester: ")

    # Input marks
    print("\nEnter Marks (out of 100):")
    pps_t = int(input("PPS (Theory): "))
    pps_p = int(input("PPS (Practical): "))
    lf_p = int(input("LF (Practical): "))
    wdf_p = int(input("WDF (Practical): "))

    # Calculate totals
    total = pps_t + pps_p + lf_p + wdf_p
    percentage = total / 4

    # Grade system
    if percentage >= 85:
        grade = "A+"
      
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Print Marksheet
    print("\n================= MARKSHEET =================")
    print(f"Roll No     : {rno}")
    print(f"Name        : {name}")
    print(f"Department  : {dept}")
    print(f"Semester    : {sem}")
    print("=============================================")

    # Table Header
    print("| Sr.No |   Subject   | Theory | Practical |")
    print("|-------|-------------|--------|-----------|")

    # Subjects Row
    print(f"|  1    |    PPS      |  {pps_t:<6} |   {pps_p:<7} |")
    print(f"|  2    |    LF       |    -   |   {lf_p:<7} |")
    print(f"|  3    |    WDF      |    -   |   {wdf_p:<7} |")

    print("|-------|-------------|--------|-----------|")

    # Summary
    print(f"Total Marks : {total} / 400")
    print(f"Percentage  : {round(percentage, 2)}%")
    print(f"Grade       : {grade}")
    print("=============================================")

    # Pass/Fail Message
    if percentage >= 50:
        print("🎉 Congratulations! You have passed. 🎉")
    else:
        print("❌ Sorry, you didn't clear the exam. ❌")

else:
    print("Invalid Roll No")
