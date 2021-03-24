#!/usr/bin/env python
# -*- coding: utf8 -*-

from person import Person

def main():

    enter_door_unlocked = False
    exit_door_unlocked = False

    person1 = Person("Michael", "boss")
    person2 = Person("Lincoln", "worker")
    person3 = Person("Brad", "worker")

    is_person2_here = False
    is_person3_here = False
    is_everybody_inside = False

    name = str(input("Who is trying to enter the building?: "))


    if name == "Michael":
        enter_door_unlocked = True
        print("The boss came and unlocked the front door.")
        while(1):
            if is_everybody_inside == False:
                worker = str(input("Who is trying to get inside?: "))
                if worker == "Lincoln":
                    is_person2_here = True
                    print("Lincoln came to work!")
                elif worker == "Brad":
                    is_person3_here = True
                    print("Brad came to work!")
                elif worker != "Lincoln" or worker != "Brad":
                    print("You are not working here. You are not allowed to go inside!")
                if is_person2_here == True and is_person3_here == True:
                    is_everybody_inside = True
                    enter_door_unlocked = False
                    print("All workers came. The front door is now locked.")
                    break
    else:
        print("The boss haven't unlocked the door yet. Come later.")

        
    if enter_door_unlocked == True and is_everybody_inside == True:
        enter_door_unlocked = False
    else:
        enter_door_unlocked = True

    #pri proverka za izlizane ot izhodna vrata da pita ot konzolata kolko vreme e rabotil daden worker

if __name__ == "__main__":
    main()
