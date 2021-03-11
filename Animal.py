
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
        for i in range(len(input_list)): 
            for i1 in range(len(input_list)): 
                if i != i1: 
                    if input_list[i] == input_list[i1]: 
                        print("There are duplicates")


def main(check_for_duplicates):

    #create list to store user inputs
    input_list = []
  #  unique_list = set(input_list) #see later

    #create cycle to get the needed amount of inputs
    i = 0
    while i < 4:
        a = str(input("Please enter four animal types: "))
        input_list.append(a)
        i += 1

    #call check_for_duplicates method
    check_for_duplicates()

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
    main(check_for_duplicates)
