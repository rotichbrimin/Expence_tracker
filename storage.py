import csv
FILE_PATH = "expenses.csv"

def load_data():
    expenses = []

    try :
        # open im 'r' (read) mode
        with open(FILE_PATH, "r") as file:
            reader = csv.reader(file)
            is_header = True

            for row in reader:
                #skip first row because it contains header
                if is_header:
                    is_header = False
                    continue
                #Rebuild the dictionary from CSV row
                if row:
                    exp = {
                            "id" : int(row[0]),
                            "name": row[1],
                            "category": row[2],
                            "amount": int(row[3]),
                            "date": row[4]
                    }
                    #Safely handle the time column if it exists.
                    exp["time"] = row[5] if len(row) > 5 else "N/A"
                    #Appended the finished dictionary
                    expenses.append(exp)
        return expenses
    except FileNotFoundError:
        #If program is run for the very first time without any CSV retutn an empty list
        return []

def save_data(expenses):
    #open in "w" (write) mode. newline = "" prevents windows from addind blank rows between data
    with open(FILE_PATH, "w", newline="") as file:
        writer = csv.writer(file)

        #write column header
        writer.writerow(["ID", "NAME", "CATEGORY", "AMOUNT", "DATE", "TIME"])

        #loop through the list and write the actual data wrows
        for exp in expenses:
            writer.writerow([
                exp['id'],
                exp['name'],
                exp['category'],
                exp['amount'],
                exp['date'],
                exp.get('time', 'N/A')
            ])