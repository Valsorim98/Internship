from card_reader import ACT230
from tokensbase import Tokens
from access_control import AccessControl


def main():
    """Main function for the project.
    """
    #Create card reader one
    card_reader = ACT230("COM3")

    tokens = Tokens()
    tbase = tokens.get_database()

    ac = AccessControl(card_reader, tbase)

    #call update method in a while cycle to check for token input non-stop
    while(1):
        ac.update()



if __name__ == "__main__":
    main()
