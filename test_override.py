class Parent:
    """Create class Parent.
    """

    def show(self):
        print("I am the parent.")


class Child(Parent):
    """Create class Child. Sub class of class Parent.
    """

    def display(self):
        print("I am the child.")


obj = Child()
obj.show()
obj.display()
