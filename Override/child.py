class Child():
    """Create class Child. Sub class of class Parent.
    """

    def display(self):
        super().display()   #call parent's class method using super()
        print("I am the child.")
        