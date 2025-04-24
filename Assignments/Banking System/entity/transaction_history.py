# transaction_history.py

print("🏦 Welcome to Shruthi Bank Transaction System!")
print("Enter your transactions. Type 'exit' to quit.\n")

# List to store transactions
transactions = []

while True:
    action = input("Enter transaction type (deposit/withdraw) or 'exit' to finish: ").lower()

    if action == "exit":
        break
    elif action not in ["deposit", "withdraw"]:
        print("❌ Invalid transaction type. Please enter 'deposit' or 'withdraw'.")
        continue

    try:
        amount = float(input(f"Enter amount to {action}: $"))
        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            continue
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        continue

    # Store transaction as tuple
    transactions.append((action, amount))
    print(f"✅ {action.capitalize()} of ${amount:.2f} recorded.\n")

# Display transaction history
print("\n📋 Transaction History:")
if transactions:
    for index, (t_type, amt) in enumerate(transactions, 1):
        print(f"{index}. {t_type.capitalize()} - ${amt:.2f}")
else:
    print("No transactions recorded.")
