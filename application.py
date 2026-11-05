import csv
applications = []  

try:
    with open("applications.csv", "r", newline="") as file:
        for company, role in csv.reader(file):
            applications.append(f"{company} - {role}")
except FileNotFoundError:
    pass

while True:
    print("\n1. Add application")
    print("2. View applications")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        
        company = input("Type in the company name: ")
        role = input("Type in the job role: ")
        applications.append(f"{company} - {role}")

        with open("applications.csv", "a", newline="") as file:
            csv.writer(file).writerow([company, role])

        

    elif choice == "2":
        
        for application in applications:
            print(application)
       

    elif choice == "3":
        break

    else:
        print("Please choose 1, 2, or 3.")