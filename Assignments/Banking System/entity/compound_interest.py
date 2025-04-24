# Function to calculate compound interest
def calculate_future_balance(initial_balance, annual_interest_rate, years):
    future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years
    return future_balance

# Number of customers
num_customers = int(input("Enter the number of customers: "))

# Loop through each customer
for customer in range(1, num_customers + 1):
    print(f"\nCustomer {customer}:")
    
    # Get customer details
    initial_balance = float(input("Enter initial balance: $"))
    annual_interest_rate = float(input("Enter annual interest rate (in %): "))
    years = int(input("Enter number of years: "))
    
    # Calculate future balance
    future_balance = calculate_future_balance(initial_balance, annual_interest_rate, years)
    
    # Display future balance
    print(f"Future balance after {years} years: ${future_balance:.2f}")
