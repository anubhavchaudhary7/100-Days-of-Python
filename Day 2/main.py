print("Welocme to the Tip Calculator.")

total = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split the bill? "))

split = round((total + total * tip / 100) / people, 2)

# spilt = round(split, 2)

print(f"Each person should pay: ${split}")
