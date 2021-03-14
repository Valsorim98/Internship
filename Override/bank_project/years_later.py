from person import Person

class PersonLater(Person):

    def introduce(self):
        """Create method introduce.
        """        

        age = int(input("Please enter your age: "))
        print(f"Hi, my name is Ivan Ivanov and I am {age} years old.")
        return age
        