
class Person:
    """Create class Person.
    """
    def __init__(self, name, age):
        """Constructor for class Person.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def is_greater(self, age):
        """Shows if the input age is greater than the person's age.

        Args:
            age (int): Shows the input age.

        Returns:
            bool: Returns True if the input age is older than the person's age, else False.
        """
        return self.age < age

    def is_equal(self, age):
        """Shows if the input age is equal to the person's age.

        Args:
            age (int): Shows the input age.

        Returns:
            bool: Returns True if the input age equals the person's age, else False.
        """
        return self.age == age

    def is_lower(self, age):
        """Shows if the input age is younger than the person's age.

        Args:
            age (int): Shows the input age.

        Returns:
            bool: Returns True if the input age is younger than the person's age, else False.
        """
        return self.age > age


    def introduce_self(self):
        """Prints the person's name and age.
        """
        print(f"My name is {self.name} and I am {self.age} years old.")

def main():
    """Create main function.
    """

    #Cycle asks user for integer type until provided
    while True:
        try:
            #age input
            age = int(input("Please enter age: "))
            break
        except ValueError:
            print("You didn't enter a number. Please enter a number.")


    #create two people with names and age
    p1 = Person("Tom", 20)
    p2 = Person("Jerry", 35)

    #call introduce_self method which is printing to the console
    p1.introduce_self()
    p2.introduce_self()

    #create variables to store the bool response from is_greater method
    p1_great = p1.is_greater(age)
    p2_great = p2.is_greater(age)

    #create variables to store the bool response from is_equal method
    p1_equal = p1.is_equal(age)
    p2_equal = p2.is_equal(age)

    #create variables to store the bool response from is_lower method
    p1_lower = p1.is_lower(age)
    p2_lower = p2.is_lower(age)

    #create conditional statements to print the person's age compared to the input age for person 1 - Tom
    if p1_great:
        print(f"{p1.name}'s age is younger than {age}")
    if p1_equal:
        print(f"{p1.name}'s age equals {age}")
    if p1_lower:
        print(f"{p1.name}'s age is older than {age}")

    #create conditional statements to print the person's age compared to the input age for person 2 - Jerry
    if p2_great:
        print(f"{p2.name}'s age is younger than {age}")
    if p2_equal:
        print(f"{p2.name}'s age equals {age}")
    if p2_lower:
        print(f"{p2.name}'s age is older than {age}")

if __name__ == "__main__":
    main()
