import csv
from datetime import datetime

def export_to_csv(expences):
    if not expences:
        print("No data to export")
        return

    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Header row
        writer.writerow(["ID", "Name", "Category", "Amount", "Date"])

        # Data rows
        for exp in expences:
            writer.writerow([
                exp['id'],
                exp['name'],
                exp['category'],
                exp['amount'],
                exp['date']
            ])

    print("Data exported successfully to expenses.csv")
    
   

def total(expences):
    while True:
        print("\n ===TOTAL EXPENSES ===:")
        print("1. Total Overall: ")
        print("2. Total per date: ")
        print("3. Total per category:")
        print("4. Back")
        
        try:
            option = int(input("Enter an option: "))
            if option == 1:
                total_spending(expences)
            elif option ==2:
                total_per_date(expences)
            elif option ==3:
                total_by_category(expences)
            elif option ==4:
                return
            else:
                print("Enter an option 1,2 or 3: ")
                
        except ValueError:
            print("Enter a valid option! Try again:")


              

def total_spending(expences):
    if not expences:
        print("No expence available")
        return
    total=0
    
    for exp in expences:
        total+= exp['amount']    
    
    print("\n=== TOTAL SPENDINGS ===")  
    print(f"Total spending: KSH {total}:")  
    



def total_per_date(expences):
    while True:
        target_date = input("\nEnter date to find spendings. Use format (YYYY-MM-DD): !") 
        try:
            datetime.strptime(target_date, "%Y-%m-%d")
            total = 0
            found = False
            for exp in expences:
                if exp['date']  == target_date:
                    total+=exp['amount']
                    found =True
            if found:
                print(f"\nTotal spending for {target_date}: KSH {total}.")
                return
            else:
                print("No expence found for this date.")
                return
        except ValueError:
            print("Enter a valid date. Use format (YYYY-MM-DD)")




def total_by_category(expences):
    if not expences:
        print("No expence made:")
        return
    while True:
        category=input("Enter category:").lower().strip()
        total = 0
        found = False
        
        for exp in expences:
            if exp['category'].lower()== category:
                total+= exp['amount']
                found =True
                
        if found:
            print(f"Total expence for {category} is KSH {total}")
        else:
            print("No expence in this category")
        again =input("Search again ? yes/y or no/n").lower().strip()
        if again in ["yes", "y"]:
            continue
        elif again in ["no", "n"]:
            return
        else:
            print("Enter yes/y or no/n!")
            
            
            
def display_sorted(expences):
    if not expences:
        print("No expence to sort:")
        return
    print("=== SORTED LIST ===")
    for exp in expences:
        print(f"ID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")



def sort_menu(expences):
    while True:
        print("\n=== SORT MENU ===")
        print("1. Sort by Amount (low to high: )")
        print("2. Sort by Amount (high to low: )")
        print("3. Sort by Name (A to Z): ")
        print("4. Sort by Date (old to new): ")
        print("5. Back: ")
        
        try:
            option = int(input("Enter an option: "))
        except ValueError:
            print("Enter a valid option!")
            
        if option == 1:
            sorted_list = sorted(expences, key = lambda exp : exp['amount'])
            display_sorted(sorted_list)
            
        elif option == 2:
            sorted_list = sorted(expences, key= lambda exp: exp['amount'], reverse = True)
            display_sorted(sorted_list)
            
        elif option ==3:
            sorted_list = sorted(expences, key = lambda exp: exp['name'].lower())
            display_sorted(sorted_list)
            
        elif option == 4:
            sorted_list = sorted(expences, key = lambda exp: exp['date'])
            display_sorted(sorted_list)
            
        elif option == 5:
            return
            
        else:
           print("Enter an option 1,2,3,4,5")
           
        again = input("\nSort again? yes/y or no/n: ")
        if again in ["yes", "y"]:
            continue
        elif again in ["no", "n"]:
            return
        else:
            print("Enter yes/y or no/n!")

