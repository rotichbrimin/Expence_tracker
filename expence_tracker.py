
import json
from datetime import datetime



def load_data():
    try:
        with open("/storage/emulated/0/expences.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return[]
 
 
        
def save_data(expences):
    with open("/storage/emulated/0/expences.json", "w") as file:
        json.dump(expences, file, indent=4)
        



def add_expence(expences):
    while True:
        try:
            expence_id =int(input("Enter Expence ID: "))
            exists = False
            for exp in expences:
                if exp['id']==expence_id:
                    exists=True
                    break
                
            if exists:
                print(f"ID {expence_id} exists. Try again!")
                continue
            else:
                break
        except ValueError:
            print("Enter a valid ID")
     
    while True:           
        name = input("Enter expence name:")
        if name:
            break
        print("Name cannot be empty!")
    while True:
        try:
            amount = int(input(f"Enter amount for {name}:"))
            if amount >0:
                break
            print("Amount must be more than 0")
            continue
        except ValueError:
           print("Enter a valid amount")
           continue
    while True:       
        date = input(f"Enter expence date (YYYY-MM-DD) for {name}:").strip()
        if not date:
            print("Date cannot be empty!")
            continue
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD")
            continue
    
    return{
        "id":expence_id,
        "name":name,
        "amount":amount,
        "date":date
    }
    
    
    
def view_expences(expences):
    if not expences:
        print("No expence made")
        return
    print("\n=== YOUR EXPENSES ===")
    for exp in expences:
        print(f"ID: {exp['id']} | Name  {exp['name']} | Amount: {exp['amount']} | Date: {exp['date']}")


def search(expences):
    while True:
        print("1. Search by ID or Name: ")
        print("2. Search by Date: ")
        print("3. Back")
            
        try:
            option = int(input("Enter an option 1,2,3: "))
            
            if option == 1:
                search_expence(expences)
            elif option ==2:
                search_by_date(expences)
            elif option ==3:
                return
            else:
                print("Choose either 1,2 or 3")
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
                    
                    print(f"\nExpence: {exp['id']} | Name: {exp['name']} | Amount: {exp['amount']} | Date: {exp['date']}")
                    found =True
            else:
                if search in exp['name'].lower():
                    print("\n=== SEARCH RESULTS ===")  
                    print(f"\nExpence: {exp['id']} | Name: {exp['name']} | Amount: {exp['amount']} | Date: {exp['date']}")
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
                    print(f"ID: {exp['id']} | Name: {exp['name']} | Amount: {exp['amount']} | Date: {exp['date']}")
                    found = True
            if not found:
                print(f"Expence not found for date: {target_date}")
                return
        except ValueError:
            print("Enter a valid date! Try again")

        


def delete(expences):
    while True:
        print("1. Delete per ID or Name")
        print("2. Delete all.")
        print("3. Back")
        try:
            option = int(input("Enter an option (1,2,3): "))
        
            if option == 1:
                delete_expence(expences)
            elif option ==2:
                delete_all_expences(expences)
            elif option ==3:
                return
            else:
                print("Choose either 1,2 or 3:")
         
        except ValueError:
            print("Invalid option! Try again")
            
def delete_expence(expences):
    if not expences:
        print("No expence to delete!")
        return
        
    while True:
        query= input("\nEnter expence ID or Name to delete: ").strip()
        for i, exp in enumerate(expences):
            if query.isdigit():
                if int(query)==exp['id']:
                    confirm = input("Are you sure to delete? (yes/y), (no/n)").strip().lower()
                    if confirm in ["yes", "y"]:
                        del expences[i]
                        save_data(expences)
                        print(f"Expence: {exp['id']} - {exp['name']} deleted successfully")
                        return
                    elif confirm in ["no", "n"]:
                        print("Cancelled")
                        return
                         
            else:
                if query.lower() in exp['name'].lower():
                    confirm = input("Are you sure to delete? (yes/y), (no/n)").strip().lower()
                    if confirm in ["yes", "y"]:
                        del expences[i]
                        save_data(expences)
                        print(f"Expence: {exp['id']} - {exp['name']} deleted successfully")
                        return
                    elif confirm in ["no", "n"]:
                        print("Cancelled")
                        return
                        
        else:
            print("Expence not found")
            retry = input("Try again? (yes/y) or (no/n)").strip().lower()
            if retry in ["yes", "y"]:
                continue
            elif retry in ["no", "n"]:
                return
            else:
                print("Enter yes/y no/n")


def delete_all_expences(expences):
    confirm = input("!!! WARNING: Are you sure you want to delete ALL expenses? (yes/no): ").strip().lower()
    if confirm in ["yes", "y"]:
        expences.clear() 
        save_data(expences)
        print("All data has been wiped successfully.")
    else:
        print("Deletion cancelled. Your data is safe.")
        
      

def update_expence(expences):
    if not expences:
        print("No expence to update")
        return

    while True:
        search_update = input("Enter ID or name of expence to update: ").strip().lower()
        found = False

        for exp in expences:
            
            
            if search_update.isdigit() and int(search_update) == exp['id']:
                found = True

            
            elif search_update == exp['name'].lower():
                found = True

            if found:
                print(f"\nID: {exp['id']} | Name: {exp['name']} Amount:{exp['amount']} | Date: {exp['date']}")

                print("\n1. Update Name")
                print("2. Update Amount")
                print("3. Update Date")
                
                while True:

                    try:
                        choice = int(input("Enter an Option: "))
                    except ValueError:
                        print("Enter a valid option")
                        continue
                    if choice in [1,2,3]:
                        break
                    else:
                        print("Invalid option!")

                if choice == 1:
                    new_name = input("Enter new name: ").strip()
                    exp['name'] = new_name
                    save_data(expences)
                    return

                elif choice == 2:
                    while True:
                        try:
                            new_amount = int(input("Enter new amount: "))
                            if new_amount > 0:
                                exp['amount'] = new_amount
                                save_data(expences)
                                return
                            else:
                                print("Amount must be more than 0")
                        except ValueError:
                            print("Enter a valid number")

                elif choice == 3:
                    while True:     
                        new_date = input("Enter new date. Use format(YYYY-MM-DD): ").strip()
                        try:
                            datetime.strptime(new_date, "%Y-%m-%d")
                            exp['date'] = new_date
                            save_data(expences)
                            return
                           
                        except ValueError:
                            print("Invalid date. Use YYYY-MM-DD")

                else:
                    print("Invalid option")

        if not found:
            print("Expense not found")                   
        
def total(expences):
    while True:
        print("1. Total Overall: ")
        print("2. Total per date: ")
        print("3. Back")
        
        try:
            option = int(input("Enter an option: "))
            if option == 1:
                total_spending(expences)
            elif option ==2:
                total_per_date(expences)
            elif option ==3:
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
        except ValueError:
            print("Enter a valid date. Use format (YYYY-MM-DD)")





             
expences = load_data()
    
def main():
    print("\n=== MAIN MENU ===")
    print("1. Add Expence:")
    print("2. View Expences:")
    print("3. Update Expence:")
    print("4. Delete :")
    print("5. Search :")
    print("6. Total  :")
    print("7. Exit   :")
    
    try:
        option=int(input("Enter an option (1,2,3,4,5,6,7): "))
    except ValueError:
        print("Enter a valid option!")
        return
        
    if option==1:
        while True:
            expences.append(add_expence(expences))
            save_data(expences)
            again=input("Add another expence? yes/y no/n :").strip().lower()
            if again in ["yes", "y"]:  
                continue
            elif again in ["no", "n"]:
                view_expences(expences)
                return
            else:
                print("Enter yes/y no/n")
                 
    elif option ==2:
        view_expences(expences)
    elif option ==3:
        update_expence(expences)
        save_data(expences)
    elif option ==4:
        view_expences(expences)
        delete(expences)
        save_data(expences)
    elif option ==5:
        search(expences)
    elif option ==6:
        total(expences)
    elif option ==7:
        return
    else:
        print("Enter a valid option")
while True:        
    main()               