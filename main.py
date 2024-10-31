from tabulate import tabulate
import os

class NeoBank:
    def __init__(self):
        self.accounts = {}  
        self.next_account_id = 1  

    def clear_console(self):
        os.system('clear')

    def display_menu(self):
        print("--------------------------------------------------------------", "", sep="\n")
        print("       Welcome To The NeoBank")
        menu = [
            ["1", "Create an Account"],
            ["2", "View Account Details"],
            ["3", "Update Account Details"],
            ["4", "Delete Account"],
            ["5", "Send Money"],
            ["6", "Exit"]
        ]
        print(tabulate(menu, headers=["Option", "       Dashboard "], tablefmt="grid"), "", sep="\n")

    def create_account(self):
        name = input("Please Enter Your Name: ")
        date_of_birth = input("Please Enter Your Date Of Birth: ")
        city = input("Please Select Your City: ")
        branch = input("Please Select Your Branch: ")

        account_id = self.next_account_id
        self.accounts[account_id] = {
            "name": name,
            "date_of_birth": date_of_birth,
            "city": city,
            "branch": branch
        }
        self.next_account_id += 1

        print(f"\nAccount Created Successfully! Your Account ID is {account_id}")
        print(f"Name: {name}, Date of Birth: {date_of_birth}, City: {city}, Branch: {branch}\n")

    def view_account_details(self):
        account_id = int(input("Enter Account ID to view details: "))
        account = self.accounts.get(account_id)
        if account:
            print("\nAccount Details:")
            for key, value in account.items():
                print(f"{key.capitalize()}: {value}")
            print()
        else:
            print("\nAccount not found.\n")

    def update_account_details(self):
        account_id = int(input("Enter Account ID to update: "))
        account = self.accounts.get(account_id)
        if account:
            print("Leave blank if you don't want to change a field.")
            name = input(f"Name [{account['name']}]: ") or account['name']
            date_of_birth = input(f"Date of Birth [{account['date_of_birth']}]: ") or account['date_of_birth']
            city = input(f"City [{account['city']}]: ") or account['city']
            branch = input(f"Branch [{account['branch']}]: ") or account['branch']

            self.accounts[account_id] = {
                "name": name,
                "date_of_birth": date_of_birth,
                "city": city,
                "branch": branch
            }
            print("\nAccount Updated Successfully!\n")
        else:
            print("\nAccount not found.\n")

    def delete_account(self):
        account_id = int(input("Enter Account ID to delete: "))
        if account_id in self.accounts:
            del self.accounts[account_id]
            print("\nAccount Deleted Successfully!\n")
        else:
            print("\nAccount not found.\n")

    def send_money(self):
        from_id = int(input("Enter Your Account ID: "))
        to_id = int(input("Enter Recipient's Account ID: "))
        amount = input("Enter Amount to Send: ")
        if from_id in self.accounts and to_id in self.accounts:
            print(f"\nSuccessfully sent {amount} from Account {from_id} to Account {to_id}.\n")
        else:
            print("\nInvalid Account IDs.\n")

    def run(self):
        self.clear_console()
        while True:
            self.display_menu()
            choice = input("What would you like to do (1-6): ")
            print("")
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.view_account_details()
            elif choice == "3":
                self.update_account_details()
            elif choice == "4":
                self.delete_account()
            elif choice == "5":
                self.send_money()
            elif choice == "6":
                print("Thank You for Banking with NeoBank (^.^)\n")
                break
            else:
                self.clear_console()
                print("Invalid Choice, Please Try Again.\n")


if __name__ == "__main__":
    bank = NeoBank()
    bank.run()
