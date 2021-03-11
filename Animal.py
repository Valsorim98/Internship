
class Animal:

    def __init__(self, name, type, age):
        """Constructor for animals

        Args:
            name (str): Animal name
            type (str): Animal type
            age (int): Animal age
        """        
        self.name = name
        self.type = type
        self.age = age

    def greet(self):
        """Method to print the animal's name, age and type.
        """        
        print(f"Hi, my name is {self.name} and I'm a {self.age} years old {self.type}.")

    def check_for_duplicates(self, input_list):
        """Check if the user entered duplicates.

        Args:
            input_list (list): Stores the user's inputs.
        """        
        if len(input_list) == len(set(input_list)):
            return False
        else:
            return True


def main():

    #create list to store user inputs
    input_list = []

    #create cycle to get the needed amount of inputs
    i = 0
    while i < 4:
        a = str(input("Please enter four animal types: "))
        input_list.append(a)
        i += 1

    #check if there is a duplicate in the input list
    is_duplicate = check_for_duplicates()
    
    if is_duplicate:
        print("Yes, there are duplicates in the list.")
    else:
        print("No, there are no duplicates in the list.")

    #create animals with name, type and age
    a1 = Animal("Riki", input_list[0], 3)
    a2 = Animal("Bandit", input_list[1], 7)
    a3 = Animal("Roko", input_list[2], 10)
    a4 = Animal("Mirage", input_list[3], 5)

    #call greet method
    a1.greet()
    a2.greet()
    a3.greet()
    a4.greet()


#start main function
if __name__ == "__main__":
    main()
