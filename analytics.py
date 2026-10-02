import csv
from datetime import datetime
from expenses import view_expenses, monthly_budget

# def export_to_csv(expences):
#     if not expences:
#         print("No data to export")
#         return

#     with open("expenses.csv", "w", newline="") as file:
#         writer = csv.writer(file)

#         # Header row
#         writer.writerow(["ID", "Name", "Category", "Amount", "Date"])

#         # Data rows
#         for exp in expences:
#             writer.writerow([
#                 exp['id'],
#                 exp['name'],
#                 exp['category'],
#                 exp['amount'],
#                 exp['date']
#             ])

#     print("Data exported successfully to expenses.csv")
    
   

def total(expenses):
    while True:
        print("\n ===TOTAL EXPENSES ===:")
        print("1. Check Monthly Budget:")
        print("2. Total Overall: ")
        print("3. Total per date: ")
        print("4. Total per category:")
        print("5. Filter By Date Range:")
        print("6. Back")
        
        try:
            option = int(input("Enter an option: "))
            if option == 1:
                monthly_budget(expenses)
            elif option == 2:
                total_spending(expenses)
            elif option ==3:
                total_per_date(expenses)
            elif option ==4:
                total_by_category(expenses)
            elif option == 5:
                filter_by_date_range(expenses)
            elif option ==6:
                return
            else:
                print("Enter an option 1,2,3,4 or 5: ")
                
        except ValueError:
            print("Enter a valid option! Try again:")


              

def total_spending(expenses):
    if not expenses:
        print("No expence available")
        return
    total=0
    
    for exp in expenses:
        total+= exp['amount']    
    
    print("\n=== TOTAL SPENDINGS ===")  
    print(f"Total spending: KSH {total}:")  
    



def total_per_date(expenses):
    while True:
        target_date = input("\nEnter date to find spendings. Use format (YYYY-MM-DD): ")
        results = [] 
        try:
            datetime.strptime(target_date, "%Y-%m-%d")
            total = 0
            found = False
            for exp in expenses:
                if exp['date']  == target_date:
                    total+=exp['amount']
                    results.append(exp)
                    found =True
            if found:
                view_expenses(results)
                print(f"\nTotal spending for {target_date}: KSH {total}.")
                return
            else:
                print("No expense found for this date.")
                return
        except ValueError:
            print("Enter a valid date. Use format (YYYY-MM-DD)! ")




def total_by_category(expenses):
    if not expenses:
        print("No expense made:")
        return
    while True:
        category=input("Enter category: ").lower().strip()
        results = []
        total = 0
        found = False
        
        for exp in expenses:
            if exp['category'].lower()== category:
                total+= exp['amount']
                results.append(exp)
                found =True
                
        if found:
            view_expenses(results)
            print(f"\nTotal expense for {category} is KSH {total}.")
        else:
            print("No expense in this category")
        while True:
            again =input("Search again ? yes/y or no/n: ").lower().strip()
            if again in ["yes", "y"]:
                break #breaks from the inner loop to total menu
            elif again in ["no", "n"]:
                return #exits the entire loop
            else:
                print("Enter yes/y or no/n!")
            
            
            
# def display_sorted(expences):
#     if not expences:
#         print("No expence to sort:")
#         return
#     print("=== SORTED LIST ===")
#     print("-" * 65)
#     for exp in expences:
#         print(f"{exp['id']:<5} | {exp['name']:<15} | {exp['category']:<15} | {exp['amount']:<10} | {exp['date']:<12}")

        # print(f"ID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")

def view_summary(expenses):
    if not expenses:
        print("No expense recorded! ")
        return

    total_amount = sum(exp['amount'] for exp in expenses)
    category_total = {}

    for exp in expenses:
        cat = exp['category']
        category_total[cat] = category_total.get(cat,0) + exp['amount']

    print("\n === EXPENSE SUMMARY ===")
    print(f"Total Spent: KSH: {total_amount}: ")
    print("\n=== BREAKDOWN BY CATEGORY ===")
    print("-" * 40)
    for category, amount in category_total.items():
        percentage = (amount/ total_amount) * 100
        print(f"{category:<15} : KSH {amount:<8} : ({percentage:.1f}%)")


def filter_by_date_range(expenses):
    if not expenses:
        print("No expense made! ")
        return
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()
    
    #Date error handling
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please use (YYYY-MM-DD)")
        return
    if start_date > end_date:
        print("Error: Start date cannot be after end date! ")
        return
    filtered = [
        exp for exp in expenses
        if start_date <= exp.get("date", "") <= end_date
    ]

    if not filtered:
        print(f"No expense found between {start_date} and {end_date}! ")
        return
    #Sum of expenses from given date range
    total = sum(exp['amount'] for exp in filtered)

    print(f"\n===SPENDINGS FROM {start_date} TO {end_date}")
    for exp in filtered:
        #Pass through filtered list to print expenses only from date range
        view_expenses(filtered)
    print(f"\nTotal spending from {start_date} to {end_date} is KSH: {total}")

def sort_menu(expenses):
    while True:
        print("\n=== SORT MENU ===")
        print("1. Sort by Amount (low to high: )")
        print("2. Sort by Amount (high to low: )")
        print("3. Sort by Name (A to Z): ")
        print("4. Sort by Name (z to A): ")
        print("5. Sort by Date (old to new): ")
        print("6. Sort by Date (new to old): ")
        print("7. Back: ")
        
        try:
            option = int(input("Enter an option: "))
        except ValueError:
            print("Enter a valid option!")
            
        if option == 1:
            sorted_list = sorted(expenses, key = lambda exp : exp['amount'])
            view_expenses(sorted_list)
            
        elif option == 2:
            sorted_list = sorted(expenses, key= lambda exp: exp['amount'], reverse = True)
            view_expenses(sorted_list)
            
        elif option ==3:
            sorted_list = sorted(expenses, key = lambda exp: exp['name'].lower())
            view_expenses(sorted_list)
        elif option == 4:
            sorted_list = sorted(expenses, key = lambda exp : exp['name'].lower(), reverse=True)  
            view_expenses(sorted_list)          
        elif option == 5:
            sorted_list = sorted(expenses, key = lambda exp: exp['date'])
            view_expenses(sorted_list)

        elif option == 6:
            sorted_list = sorted(expenses, key = lambda exp: exp['date'], reverse = True)
            view_expenses(sorted_list)
            
        elif option == 7:
            return
            
        else:
           print("Enter an option 1,2,3,4,5,6,7! ")
        while True:

            again = input("\nSort again? yes/y or no/n: ")
            if again in ["yes", "y"]:
                break #break out of this inner loop to the main looop
            elif again in ["no", "n"]:
                return #Exit to the sort menu
            else:
                print("Enter yes/y or no/n!")#print the warning and stays in this same loop

