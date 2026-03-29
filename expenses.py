
from storage import save_data
from datetime import datetime

def clear_storage(expences):
    expences.clear()
    save_data(expences)
    print("All saved data cleared")




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
        category = input("Enter category: ")
        if category:
            break
        print("Category cannot be empty!")
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
        "category":category,
        "amount":amount,
        "date":date
    }
    
    
    
def view_expences(expences):
    if not expences:
        print("No expence made")
        return
    print("\n=== YOUR EXPENSES ===")
    for exp in expences:
        print(f"ID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")



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
                print(f"\nID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} Amount:{exp['amount']} | Date: {exp['date']}")

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
        
      

