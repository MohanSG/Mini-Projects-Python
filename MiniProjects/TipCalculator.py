print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?: $"))
tip = int(input("How much tip would you like to give? 10%, 12% or 15%: "))
number_of_people = int(input("How many people to split the bill?: "))

total_bill_tip = ((tip / 100) * total_bill + total_bill)
each_person_pays = total_bill_tip / number_of_people

print(f"Each person pays: {round(each_person_pays, 2)}")