class Clients:
    def __init__(self, client_name, client_age, prescription):
        self.client_name = client_name
        self.client_age = client_age
        self.prescription = prescription
        self.medicines_bought = []

class Medicine:
    def __init__(self, medicine_name, prescription_needed, min_age):
        self.medicine_name = medicine_name
        self.prescription_needed = prescription_needed
        self.min_age = min_age

clients_list = []
medicine_list = [
    Medicine("Acetaminophen", False, 14),
    Medicine("Ibuprofen", False, 14),
    Medicine("Diphenhydramine", False, 14),
    Medicine("Cetirizine", False, 14),
    Medicine("Loratadine", False, 16),
    Medicine("Famotidine", False, 16),
    Medicine("Ranitidine", False, 16),
    Medicine("Loperamide", False, 18),
    Medicine("Guaifenesin", False, 18),
    Medicine("Dextromethorphan", False, 18),
    Medicine("Amoxicillin", True, 18),
    Medicine("Metformin", True, 18),
    Medicine("Lisinopril", True, 14),
    Medicine("Simvastatin", True, 18),
    Medicine("Omeprazole", True, 18),
    Medicine("Atorvastatin", True, 18),
    Medicine("Losartan", True, 18),
    Medicine("Hydrochlorothiazide", True, 18),
    Medicine("Levothyroxine", True, 18),
    Medicine("Metoprolol", True, 18),
    Medicine("Amlodipine", True, 18),
    Medicine("Warfarin", True, 18),
    Medicine("Clopidogrel", True, 18),
    Medicine("Zolpidem", False, 18),
    Medicine("Fluoxetine", False, 18)
]

def add_user():
    print("╭──────────────────────────────╮")
    print("│      User  Registration      │")
    print("╰──────────────────────────────╯")

    print("\nPlease enter the following details:")

    username = input("╭──────────────────────────────╮\n│ Enter user name:             │ ").strip()
    user_age = int(input("╭──────────────────────────────╮\n│ Enter User Age:              │ ").strip())
    prescription = input("╭─────────────────────────────────────────────────────────────────╮\n│ Does the user have a prescription? (True/False): │ ").strip().lower() == 'true'

    new_client = Clients(username, user_age, prescription)
    clients_list.append(new_client)

    print("\n╭───────────────────────────────────────╮")
    print("│       User registration successful    │")
    print("╰───────────────────────────────────────╯")
    print(f"Username: {username}")
    print(f"Age: {user_age}")
    print(f"Prescription: {'Yes' if prescription else 'No'}")

def display_medicine():
    while True:
        print("\033[1m╔════════════════════════════════════════════════════╗\033[0m")
        print("\033[1m║               \033[96mMedicine Information Display\033[0m         ║")
        print("\033[1m╚════════════════════════════════════════════════════╝\033[0m")
        print("Enter your choice:")
        print("\033[1m1. Display only medicine names\033[0m")
        print("\033[1m2. Display medicine names and prescription status\033[0m")
        print("\033[1m3. Display detailed medicine information\033[0m")
        print("\033[1mq. Quit\033[0m")
        
        choice = input("╭────────────────────────────────────────────────────╮\n│ Enter your choice:                                  │ ").strip().lower()
        
        if choice == 'q':
            print("\n\033[1mExiting the program.\033[0m")
            break
        elif choice == '1':
            print("\n\033[1mMedicine Names:\033[0m")
            print("\033[1m════════════════\033[0m")
            for medicine in medicine_list:
                print(f"• {medicine.medicine_name}")
            print()
        elif choice == '2':
            print("\n\033[1mMedicine Names and Prescription Status:\033[0m")
            print("\033[1m══════════════════════════════════════════\033[0m")
            for medicine in medicine_list:
                prescription_status = "\033[92mYes\033[0m" if medicine.prescription_needed else "\033[91mNo\033[0m"
                print(f"• {medicine.medicine_name}: Prescription needed - {prescription_status}")
            print()
        elif choice == '3':
            print("\n\033[1mDetailed Medicine Information:\033[0m")
            print("\033[1m════════════════════════════\033[0m")
            for medicine in medicine_list:
                print(f"\033[1m• Medicine name:\033[0m {medicine.medicine_name}")
                print(f"  \033[1mPrescription needed:\033[0m {'Yes' if medicine.prescription_needed else 'No'}")
                print(f"  \033[1mMinimum age to sell:\033[0m {medicine.min_age}")
                print()
        else:
            print("\n\033[91mInvalid choice. Please enter a valid option.\033[0m\n")

def display_users():
    if not clients_list:
        print("\n\033[91mNo registered users.\033[0m\n")
        return

    print("\033[1m╔════════════════════════════════════════════╗\033[0m")
    print("\033[1m║          \033[96mUser Information Display\033[0m          ║")
    print("\033[1m╚════════════════════════════════════════════╝\033[0m")
    for client in clients_list:
        print(f"\033[1m• Username:\033[0m {client.client_name}")
        print(f"  \033[1mAge:\033[0m {client.client_age}")
        print(f"  \033[1mPrescription:\033[0m {'Yes' if client.prescription else 'No'}")

def buy_medicine():
    if not clients_list:
        print("First add a client to buy medicine.")
        return

    user_name = input("╭────────────────────────────────────────────────────╮\n│ Enter the user's name:                             │ ").strip()
    user = None
    for client in clients_list:
        if client.client_name.lower() == user_name.lower():
            user = client
            break

    if not user:
        print("\nUser not found. Please register the user first.")
        return

    medicine_name = input("╭────────────────────────────────────────────────────╮\n│ Enter the name of the medicine you want to buy:    │ ").strip()
    medicine = None
    for med in medicine_list:
        if med.medicine_name.lower() == medicine_name.lower():
            medicine = med
            break

    if not medicine:
        print("\nMedicine not found. Please check the name and try again.")
        return

    if user.client_age < medicine.min_age:
        print("\nUser does not meet the minimum age requirement for this medicine.")
        return

    if medicine.prescription_needed and not user.prescription:
        print("\nA prescription is required to buy this medicine.")
        return

    user.medicines_bought.append(medicine)

    print("\n╭──────────────────────────────────────╮")
    print("│       Medicine purchase successful!  │")
    print("╰──────────────────────────────────────╯")
    print(f"Medicine: {medicine.medicine_name}")
    print(f"User: {user.client_name}")
    print(f"Age: {user.client_age}")
    print(f"Prescription: {'Yes' if user.prescription else 'No'}")

def display_purchases():
    if not clients_list:
        print("\n\033[91mNo registered users.\033[0m\n")
        return

    print("\033[1m╔════════════════════════════════════════════════════════╗\033[0m")
    print("\033[1m║                 \033[96mUser Purchases Information\033[0m                 ║")
    print("\033[1m╚════════════════════════════════════════════════════════╝\033[0m")
    for client in clients_list:
        print(f"\033[1m• Username:\033[0m {client.client_name}")
        if client.medicines_bought:
            print(f"  \033[1mMedicines Bought:\033[0m")
            for medicine in client.medicines_bought:
                print(f"    • {medicine.medicine_name}")
        else:
            print("  \033[1mNo medicines bought yet.\033[0m")
        print()

def main():
    while True:
        print("\n\033[1m╔═════════════════════════════════════════════════════════════════╗\033[0m")
        print("\033[1m║                          \033[96mMain Menu\033[0m                              ║")
        print("\033[1m╠═════════════════════════════════════════════════════════════════╣\033[0m")
        print("\033[1m║ \033[92m1. Add User\033[0m                                                     ║")
        print("\033[1m║ \033[92m2. Display Medicines\033[0m                                            ║")
        print("\033[1m║ \033[92m3. Display Users\033[0m                                                ║")
        print("\033[1m║ \033[92m4. Buy Medicine\033[0m                                                 ║")
        print("\033[1m║ \033[92m5. Display User Purchases\033[0m                                       ║")
        print("\033[1m║ \033[91m-1. Exit\033[0m                                                        ║")
        print("\033[1m╚═════════════════════════════════════════════════════════════════╝\033[0m")

        choice = int(input("╭────────────────────────────────────────────────────╮\n│ Enter your choice:                                  : ").strip())
        
        if choice == 1:
            add_user()
        elif choice == 2:
            display_medicine()
        elif choice == 3:
            display_users()
        elif choice == 4:
            buy_medicine()
        elif choice == 5:
            display_purchases()
        elif choice == -1:
            print("\033[1mExiting program.\033[0m")
            break
        else:
            print("\033[91mInvalid choice. Please enter a valid option.\033[0m")

if __name__ == "__main__":
    main()
