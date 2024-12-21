print("Welcome to the Tip Calculator!\n")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill
print(f"Bill with tip included is ${bill_with_tip}\n")

each_person_share = bill_with_tip / number_of_people
print(f"Each person's contribution is ${each_person_share}")
print(round(each_person_share, 2))
























"""
# Subscripting
print("hello"[0])

# Strings
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

# PEMDAS

()
**
* OR /
+ OR -

print(3 * 3 + 3 / 3 - 3)

# BMI Calculator
height = 1.65
weight = 84

# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi)
print(int(bmi))
print(round(bmi))  # rounding off the result
print(round(bmi, 2))  # rounding off to the 2 decimals for accuracy
"""