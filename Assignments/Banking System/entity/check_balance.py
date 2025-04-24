# Sample data: account numbers mapped to their balances
accounts = {
    "1001": 1500.75,
    "1002": 2450.50,
    "1003": 325.00,
    "1004": 9870.20,
    "1005": 456.60
}

print("🏦 Welcome to Shruthi Bank!")
print("Enter 'exit' to quit.\n")

# Loop to keep asking until a valid account number is entered or user exits
while True:
    acc_number = input("Enter your 4-digit account number: ")

    if acc_number.lower() == "exit":
        print("Thank you for using our service.")
        break

    # Validate account number
    if acc_number in accounts:
        print(f"✅ Account Found!\n💰 Your current balance: ${accounts[acc_number]:.2f}\n")
    else:
        print("❌ Invalid account number. Please try again.\n")
