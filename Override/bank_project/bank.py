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

    date = Date()       #call Date() class
    date.today_date()   #call today_date() method

    p_age = PersonLater()    #call PersonLater() class which is sub class of Person
    p_age.introduce()        #call introduce() method

    if age >= 18:
        print(f"You can open a bank account!")
        __password()

if __name__ == "__main__":
    main()
