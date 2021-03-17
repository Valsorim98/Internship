from card_reader import ACT230


def main():
    """Main function for the project.
    """
    #Create card reader one
    c1 = ACT230("COM3")

    #call update method in a while cycle to check for token input non-stop
    while(1):
        c1.update()



if __name__ == "__main__":
    main()
