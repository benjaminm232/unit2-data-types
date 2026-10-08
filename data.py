""" bill = input()
print(bill) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" x = input("Write a sentence: ")
y = x.split( )
z = len(y)
print(f"This sentence has {z} words.") """

""" def check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
e = int(input("Enter a whole number: "))
result = check(e)
print(f"The number {e} is {result}.") """

""" print("Welcome to tip calculator")
bill = float(input("How much was your bill? $"))
service = input("How was your service: Bad, Okay, Good, Great? ")
if service == "bad":
    total = bill * 1.00
elif service == "okay":
    total = bill * 1.15
elif service == "good":
    total = bill * 1.20
elif service == "great":
    total = bill * 1.25
# this part is so the tip calculator will also work if they type in caps
elif service == "Bad":
    total = bill * 1.00
elif service == "Okay":
    total = bill * 1.15
elif service == "Good":
    total = bill * 1.20
elif service == "Great":
    total = bill * 1.25
else:
    print("Invalid option entered, defaulting to no tip.")
    total = bill * 1.00
print(f"Your total is: ${total:.2f}") """

""" def spaces(N,Y,T):
    B = 0
    for i in range(N):
        if Y[i] == "C" and T[i] == "C":
           B += 1
    print(B)
spaces(5, "CC..C", ".CC..") """

""" # Create a function that accepts an input and determines all factors of the number.
def f(number):
    i = int(input("Enter an integer: "))
    ...

f(i) """

def find_gcf(a,b):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    while b != 0:
        a, b = b, a % b
    return a

""" def wizards(N,start,duels):
    owner = start
    num_owners= 1
    for i in range(N):
        if duels[i][1] == owner:
            owner = duels[i][0]
            num_owners += 1
    print(owner)
    print(num_owners)

wizards(3, "A", ["BA", "CB", "DA"]) """

