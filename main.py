from storage import load_data, save_data
from expenses import add_expence, view_expences, update_expence, delete, clear_storage
from search import search
from analytics import total, sort_menu, export_to_csv
            
expences = load_data()
    
def main():
    print("\n=== MAIN MENU ===")
    print("1. Add Expence:")
    print("2. View Expences:")
    print("3. Update Expence:")
    print("4. Delete :")
    print("5. Search :")
    print("6. Total  :")
    print("7. Clear  :")
    print("8. Sort   :")
    print("9. Export to CSV: ")
    print("10. Exit   :")
    
    try:
        option=int(input("\nEnter an option (1-10): "))
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
        view_expences(expences)
        total(expences)
    elif option ==7:
        clear_storage(expences)
    elif option ==8:
        sort_menu(expences)
    elif option == 9:
        export_to_csv(expences)
    elif option ==10:
        return
    else:
        print("Enter a valid option")
while True:        
    main()               