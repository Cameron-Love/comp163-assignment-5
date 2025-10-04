print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
count = 0
print('Sequence:',end=' ' )

while current_number > 0:
    if current_number % 2 == 0:
        print(current_number, end=' ')
        current_number = current_number // 2
    elif current_number == 1:
        print(current_number)
        break
    elif current_number % 2 != 0:
        print(current_number, end=' ')
        current_number = (current_number * 3) + 1
    count += 1

print(f"Steps: {count}")
print("")
print("=== Challenge 2: Prime Number Checker ===")
number_2 = int(input("Enter a number: "))
number_3 =  number_2 - 1
print(f"Testing divisors from 2 to {number_3}...")
prime = True
for i in range(2, number_2):
    if number_2 % i == 0:
        prime = False
        break

if prime == True:
    print(f"{number_2} is prime!")
else:
    print(f"{number_2} is not prime (divisible by 3)")
