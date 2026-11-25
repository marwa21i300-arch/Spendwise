
income = 0
expense = 0 

transactions = []

while True:
    print("===== SPENDWISE =====")
    print("Personal Expense Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Exit")
    print("5. View Transactions")
    print("6. View Category Summary")


    choice = input("Enter your choice: ")

    print("You selected:", choice)

    if choice == "1":
        try:
            amount = float(input("Enter your income: "))
            income += amount

            print("Income added successfully!")
            print("Your Income:", income)

        except ValueError:
            print("Invalid input! Please enter a number.")

#ADD EXPENSE
    elif choice == "2":
        try:
            amount = float(input("Enter your expense: "))

            print("Choose a category:")
            print("1. Food")
            print("2. Travel")
            print("3. Shopping")
            print("4. Bills")

            category = input("Enter category number: ")

            if category == "1":
                category = "Food"
            elif category == "2":
                category = "Travel"
            elif category == "3":
                category = "Shopping"
            elif category == "4":
                category = "Bills"
            else:
                category = "Other"

            expense += amount

            transactions.append({
                "amount": amount,
                "category": category
            })

            print("Expense added successfully!")

        except ValueError:
            print("Invalid input! Please enter a number.")
    #VIEW BALANCE
    elif choice == "3":
        balance = income - expense

        print("Your remaining balance:", balance)

    elif choice == "5":
        print("===== TRANSACTION HISTORY =====")

        for transaction in transactions:
            print("Category:", transaction["category"])
            print("Amount:", transaction["amount"])
            print("--------------------")    

    elif choice == "6":

        category_totals = {}

        for transaction in transactions:

            category = transaction["category"]
            amount = transaction["amount"]

            if category in category_totals:
                category_totals[category] += amount

            else:
                category_totals[category] = amount

        print("===== CATEGORY SUMMARY =====")

        for category, total in category_totals.items():
            print(category, ":", total)

    elif choice == "4":
        print("Thank you for using SpendWise!")
        break

    else:
            print("Invalid choice!")
