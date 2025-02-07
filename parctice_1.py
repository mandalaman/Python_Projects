items = []
total_sum = 0

while True:
    user_input = input("Enter the price or press 'q' to quit: \n").strip()

    if user_input == 'q':
        print(f"\n your total bill is {total_sum}. Thanks for shopping with us.")
        print("----------------MSTORE--------------")
        break

    else:
        try:
            price = float(user_input)
            items.append(price)
            total_sum += price
            print(f"order total so far: {total_sum}")

        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

print("\nItemized Bill:")

for idx, bill in enumerate(items, start=1):
    print(f"{idx}: {bill}")