""" bill = input()
print(bill) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" bill = float(input("How much was your bill?: $"))
tip_percent = float(input("What percentage tip would you like to give?: "))
tip_amount = bill * (tip_percent/100)
total_bill = bill + tip_amount 
print(total_bill)
 """

print("Welcome to tip calculator")
bill = float(input("How much was your bill? $"))
service = input("How was your service: Bad, Okay, Good, Great? ")
if service == "bad":
    total = bill * 1.00
elif service == "okay":
    total = bill * 1.05
elif service == "good":
    total = bill * 1.10
elif service == "great":
    total = bill * 1.20
# now this part is so the tip calculator will also work if they type in caps
elif service == "Bad":
    total = bill * 1.00
elif service == "Okay":
    total = bill * 1.05
elif service == "Good":
    total = bill * 1.10
elif service == "Great":
    total = bill * 1.20
else:
    print("Invalid option entered, defaulting to no tip.")
    total = bill * 1.00
print(f"Your total is: ${total:.2f}")

""" x = input("Write a sentence: ")
y = x.split( )
z = len(y)
print(f"This sentence has {z} words.") """