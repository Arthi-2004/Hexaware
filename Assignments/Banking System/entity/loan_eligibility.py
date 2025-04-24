def check_loan_eligibility(credit_score, annual_income):
    if credit_score > 700 and annual_income >= 50000:
        return "✅ Eligible for loan."
    else:
        return "❌ Not eligible for loan."

# Taking input from user
try:
    credit_score = int(input("Enter credit score: "))
    annual_income = float(input("Enter annual income ($): "))

    result = check_loan_eligibility(credit_score, annual_income)
    print(result)

except ValueError:
    print("❗ Please enter valid numeric inputs for credit score and income.")
