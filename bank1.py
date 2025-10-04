bal = int(input("Enter the balance: "))

deposit = int(input("Enter the deposit amount: "))
bal += deposit
print(f"Balance after deposit: {bal}")

withdraw = int(input("Enter the withdrawal amount: "))
if withdraw <= bal:
    bal -= withdraw
    print(f"Withdrawal successful. New balance: {bal}")
else:
    print("Insufficient balance.")