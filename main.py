# main.py
from tabulate import tabulate
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def neo_bank():
    print("--------------------------------------------------------------","",sep="\n")
    print("       Welcome To The NeoBank")
    menu = [
        ["1", "Create an Account"],
        ["2", "View Account Details"],
        ["3", "Update Account Details"],
        ["4", "Delete Account"],
        ["5", "Send Money"],
        ["6", "Exit"]
    ]
    print(tabulate(menu, headers=["Option", "       Dashboard "], tablefmt="grid"),"",sep="\n")
  
def main():
    clear_console()
    neo_bank()
    while True:
        
        choice = input("What would you like to do (1-6):")
        print("")
        if choice == "1":
            print("Account creation functionality here.","")
        elif choice == "2":
            print("Viewing account details.")
        elif choice == "3":
            print("Updating account details.")
        elif choice == "4":
            print("Deleting account.")
        elif choice == "5":
            print("Sending money.")
        elif choice == "6":
            print("Thank You for Banking with NeoBank (^.^)","", sep="\n")
            break
        else:
            clear_console()
            neo_bank()
            print("Invalid Choice, Please Try Again.","",sep="\n")








if __name__ == "__main__":
    main()
