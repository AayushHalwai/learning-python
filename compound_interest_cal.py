principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("Enter Principle: "))
    if principle <= 0:
        print("Principle is invalid")

while rate <=0 :
    rate = float(input("Enter Rate: "))
    if rate <= 0:
        print("Invalid Rate")

while time <=0 :
    time = int(input("Enter Time in years: "))
    if time <= 0 :
        print("Invalid Time")


compound_interest = principle*pow((1+rate/100),time) - principle
total_interest = principle*pow((1+rate/100),time)
print(f"your Compound Interest is Rs.{compound_interest:.2f}")
print(f"Your Total Interest is Rs.{total_interest:.2f}")