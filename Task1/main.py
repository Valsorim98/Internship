from card_reader import ACT_230_RFID


def main():

    c1 = ACT_230_RFID("COM3")

    while(1):
        c1.update()



if __name__ == "__main__":
    main()
