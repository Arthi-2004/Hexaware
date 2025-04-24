# password_validation.py

def is_valid_password(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        print("❌ Password must be at least 8 characters long.")
        return False

    # Check if password has at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("❌ Password must contain at least one uppercase letter.")
        return False

    # Check if password has at least one digit
    if not any(char.isdigit() for char in password):
        print("❌ Password must contain at least one digit.")
        return False

    return True

# Main program
print("🔐 Create a Password for Your Bank Account")
user_password = input("Enter your new password: ")

if is_valid_password(user_password):
    print("✅ Password is valid! Your account is now secure.")
else:
    print("⚠️ Please try again with a stronger password.")
