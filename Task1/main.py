from card_reader import ACT_230_RFID


def main():
    """Main function for the project.
    """
    #Create card reader one
    c1 = ACT_230_RFID("COM3")

    #call update method in a while cycle to check for token input non-stop
    while(1):
        c1.update()



if __name__ == "__main__":
    main()
