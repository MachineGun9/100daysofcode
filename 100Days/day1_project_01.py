#day1 project
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? "))

tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_amount = round((tip_percent / 100) * total_bill, 2)

total_peoples = int(input("How many people would you like to split bill with? "))

split_bill_per_person = (total_bill + tip_amount) / total_peoples

print(f"Each person should pay: ${split_bill_per_person:.2f}")