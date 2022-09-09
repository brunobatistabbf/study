gender = input("Gender? ")
gender = gender.lower()
if gender == "male":
    print("Your cat is male")
elif gender == "female":
    print("Your cat is female")
else:
    print("Invalid input")

age = int(input("Age of your cat? "))
if age < 5:
    print("Your cat is young.")
else:
    print("Your cat is adult.")

#Elif
