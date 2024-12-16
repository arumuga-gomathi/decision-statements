age = int(input("Enter your age: "))

# Decision-making statements to classify age into categories
if age < 0:  # If age is negative, it's invalid
    print("Invalid age")
elif age <= 2:  # If age is between 0 and 2, classify as Infant
    print("Infant")
elif age <= 12:  # If age is between 3 and 12, classify as Child
    print("Child")
elif age <= 19:  # If age is between 13 and 19, classify as Teen
    if age % 2 == 0:  # Nested if statement to check if the age is even or odd
        print("Teen (even age)")
    else:
        print("Teen (odd age)")
elif age <= 64:  # If age is between 20 and 64, classify as Adult
    print("Adult")
else:  # If age is 65 or more, classify as Senior
    print("Senior")
