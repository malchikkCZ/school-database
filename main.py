import os
from core import Database


def main():
    school = Database()
    working = True
    while working:
        os.system("clear")
        print("Welcome to our school database.")        
        working = school.main_menu()
        if working == True:
            input("\nPress ENTER to return to main menu.")   
    print("Thank you for using our software!\n")
 

if __name__ == "__main__":
    main()
