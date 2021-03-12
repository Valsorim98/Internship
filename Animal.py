
class Animal:
    """Create class Animal
    """    
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



def main():
    """Create main function
    """    
    #create counter for duplicates
    counter = 0

    #create list to store user inputs
    input_list = []

    #create cycle to get the needed amount of inputs
    i = 0
    while i < 4:
        a = str(input("Please enter four animal types: "))
        input_list.append(a)
        i += 1

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

    #nested for loop to check duplicates
    for i in range(len(input_list)):
        for i1 in range(len(input_list)):
            if i != i1:
                if input_list[i] == input_list[i1]:
                    counter += 1
                    break
    print(f"There are {counter} duplicates.")

#start main function
if __name__ == "__main__":
    main()
