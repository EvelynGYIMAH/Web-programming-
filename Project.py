# Personal Budget Tracker

def budget_tracker():
    print("==== Personal Budget Tracker ====")

    # Accept user's income
    income = float(input("Enter your monthly income: "))

    # Enter expenses
    expenses = {}
    while True:
        category = input("Enter expense category (or type 'done' to finish): ").strip()
        if category.lower() == 'done':
            break
        amount = float(input(f"Enter amount for {category}: "))
        expenses[category] = expenses.get(category, 0) + amount

    # Calculate total expenses and remaining balance
    total_expenses = sum(expenses.values())
    remaining_balance = income - total_expenses

    print("\n==== Budget Summary ====")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${remaining_balance:.2f}")

    # Warning if expenses exceed income
    if total_expenses > income:
        print("⚠️ Warning: Your expenses exceed your income!")

    # Display expense percentages
    print("\nExpense Breakdown (% of income):")
    for category, amount in expenses.items():
        percentage = (amount / income) * 100
        print(f"{category}: ${amount:.2f} ({percentage:.2f}%)")

    # Savings goal check
    saving_goal = float(input("\nEnter your monthly saving goal: "))
    if remaining_balance >= saving_goal:
        print("✅ You met your saving goal!")
    else:
        print("❌ You did not meet your saving goal.")

# Run the program
budget_tracker()
