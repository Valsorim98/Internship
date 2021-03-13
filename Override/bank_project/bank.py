from date import Date
from person import Person

def main():
    """Create main function to run the project.
    """    

    date = Date()       #call Date() class
    date.today_date()   #call today_date() method

    p_age = Person()    #call Person() class
    p_age.introduce()   #call introduce() method


if __name__ == "__main__":
    main()
