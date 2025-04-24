def atm_simulation():
    try:
        balance = float(input("Enter your current balance: $"))
        
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            print(f"\n💰 Your current balance is: ${balance:.2f}")

        elif choice == 2:
            withdraw_amount = float(input("Enter amount to withdraw: $"))
            if withdraw_amount <= balance:
                if withdraw_amount % 100 == 0 or withdraw_amount % 500 == 0:
                    balance -= withdraw_amount
                    print(f"\n✅ Withdrawal successful. New balance: ${balance:.2f}")
                else:
                    print("\n❌ Withdrawal amount must be in multiples of 100 or 500.")
            else:
                print("\n❌ Insufficient balance.")

        elif choice == 3:
            deposit_amount = float(input("Enter amount to deposit: $"))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"\n✅ Deposit successful. New balance: ${balance:.2f}")
            else:
                print("\n❌ Invalid deposit amount.")

        else:
            print("\n❗ Invalid option selected.")

    except ValueError:
        print("\n❗ Please enter valid numeric values.")

# Run the ATM simulation
atm_simulation()
