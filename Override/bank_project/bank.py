from date import Date
from person import Person
from years_later import PersonLater

def main():
    """Create main function to run the project.
    """    

    date = Date()       #call Date() class
    date.today_date()   #call today_date() method

    p_age = PersonLater()    #call PersonLater() class which is sub class of Person
    p_age.introduce()        #call introduce() method


if __name__ == "__main__":
    main()
