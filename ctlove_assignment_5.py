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
