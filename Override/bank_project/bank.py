from date import Date
from years_later import PersonLater

def __password():
    """Create private method.
    """    

    password = str(input("Enter the password you want to sign up with: "))
    print(f"Your account is signed up with password: {password}")


def main():
    """Create main function to run the project.
    """    

    Date().today_date()   #call Date() class and call today_date() method

    print("You have to be at least 18 years old to open a back account.")
   
    age = PersonLater().introduce()  #call PersonLater() class which is sub class of Person and call introduce() method


    if age >= 18:
        print(f"You can open a bank account!")
        __password()
    else:
        print("You are not old enough.")


if __name__ == "__main__":
    main()
