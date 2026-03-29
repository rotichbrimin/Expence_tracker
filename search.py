from datetime import datetime

def search(expences):
    while True:
        print("1. Search by ID or Name: ")
        print("2. Search by Date: ")
        print("3. Search by Category:")
        print("4. Back")
            
        try:
            option = int(input("Enter an option 1,2,3 or 4: "))
            
            if option == 1:
                search_expence(expences)
            elif option ==2:
                search_by_date(expences)
            elif option ==3:
                search_by_category(expences)
            elif option ==4:
                return
            else:
                print("Choose either 1,2,3 or 4: ")
        except ValueError:
            print("Enter a valid option. Try again!")

def search_expence(expences):
    if not expences:
        print("No expence made") 
        return
    while True:
        search = input("Enter ID or name of expence to search:").lower().strip()
        found = False
        for exp in expences:
            if search.isdigit():
                if int(search)==exp['id']:
                    
                    print(f"\nExpence: {exp['id']} | Name: {exp['name']} | Category: {exp['category']}| Amount: {exp['amount']} | Date: {exp['date']}")
                    found =True
            else:
                if search in exp['name'].lower():
                    print("\n=== SEARCH RESULTS ===")  
                    print(f"\nExpence: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")
                    found = True
        if not found:
            print("Expence not found")   
        again = input("\nSearch again? (yes/y) or (no/n)? ").strip().lower()
        if again in ["yes", "y"]:
            continue       
        if again in ["no", "n"]:
            return     
        print("Enter yes or no")


def search_by_date(expences):
    while True:
        target_date = input("Search expence per date. Use format (YYYY-MM-DD):")
        try:
            datetime.strptime(target_date, "%Y-%m-%d")
            found = False
            for exp in expences:
                if exp['date'] == target_date:
                    print(f"ID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")
                    found = True
            if not found:
                print(f"Expence not found for date: {target_date}")
                return
        except ValueError:
            print("Enter a valid date! Try again")

def search_by_category(expences):
    while True:
        search = input("Enter search category: ").lower() 
        found=False
    
        for exp in expences:
            if exp['category'].lower()== search:
                print("=== SEARCH BY CATEGORY ===")
                print(f"ID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")
            
                found = True
            
        if not found:
            print("No expence in this category")
            
        again = input("Search again yes/y no/n ?").lower().strip()
        
        if again in ["yes", "y"]:
            continue
        elif again in ["no", "n"]:
            return
        else:
            print("Type yes/y or no/n!")
            



