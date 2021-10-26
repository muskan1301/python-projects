print("Welcome to tip calculator ")
bil = input("What was the total bill? $ ")
bill = float(bil)
tp = input("What percentage tip you want to give? 10, 12 or 15 ? ")
tip = float(int(tp)/100)
am = bill*tip
amount = bill+am
total_people = input("How many people to split the bill: ")
people = int(total_people)
total_bill = round(amount/people,2)
print(f"Each person should pay ${total_bill}")
