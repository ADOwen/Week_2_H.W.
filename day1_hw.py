# exercise 1

for num in range(500):
    if num**3 > 1000:
        break
    else:
        print(num**3)


#  exercise 2

def get_prime(range_1, range_2):
    print(f"\nHere are all the prime numbers from {range_1} to {range_2}: ")
    # or print(<hr style = "border: 1px dashed red">) ;-)
    print("=========================================="*3)
    for num in range(range_1, range_2 + 1):
        if num == 2 or (num > 1 and num % 2 != 0):
            print(num, end=", ")


get_prime(1, 100)

# exercise 3

age = int(input("Please enter your age: "))
if age < 18:
    print("You're a kid! Your life's so hard right now ugh, no one understands.")
elif 18 < age <= 65:
    print("Do I see some grey hairs over there? You're an adult, you may have your mid-life crisis any minute now.")
else:
    print("You remember all the shows you loved growing up? Well you're the only one, you're a senior now.")
    print("Don't forget to take your medicine.")
