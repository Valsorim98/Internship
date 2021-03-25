#!/usr/bin/env python
# -*- coding: utf8 -*-

from person import Person

def main():
    """Main function.
    """    

    enter_door_unlocked = False
    exit_door_unlocked = False

    # Create the boss and workers
    person1 = Person("Michael", "boss")
    person2 = Person("Lincoln", "worker")
    person3 = Person("Brad", "worker")

    is_boss_here = False
    is_person2_here = False
    is_person3_here = False
    is_everybody_inside = False
    is_everybody_outside = False

    name = str(input("Who is trying to enter the building?: "))

    # Check who is trying to get inside and if all the workers are inside to lock the enter door
    if name == "Michael":
        enter_door_unlocked = True
        is_boss_here = True
        print("The boss came and unlocked the front door.")
        while(1):
            if is_everybody_inside == False:
                name = str(input("Who is trying to get inside?: "))
                if name == "Michael":
                    if is_boss_here == True:
                        print("The boss already came in.")
                if name == "Lincoln":
                    if is_person2_here == True:
                        print("Lincoln already came in.")
                        continue
                    is_person2_here = True
                    print("Lincoln came to work!")
                if name == "Brad":
                    if is_person3_here == True:
                        print("Brad already came in.")
                        continue
                    is_person3_here = True
                    print("Brad came to work!")
                if name != "Michael" and name != "Lincoln" and name != "Brad":
                    print("You are not working here. You are not allowed to go inside!")
                if is_boss_here == True and is_person2_here == True and is_person3_here == True:
                    enter_door_unlocked = False
                    is_everybody_inside = True
                    print("All workers came in. The front door is now locked.")
                    break
    else:
        print("The boss haven't unlocked the door yet. Come back later.")
        is_everybody_inside = False


    attention = str(input("Is there an emergency?: "))
    if attention == "Yes":
        enter_door_unlocked = True
        exit_door_unlocked = True
        is_everybody_outside = True
        print("There's an emergency! Everyone is out!")


    if is_everybody_inside == True and is_everybody_outside == False:
        name = str(input("Who is trying to exit the building?: "))
        while(1):
            if is_everybody_outside == False:
                if name == "Michael":
                    if is_boss_here == True:
                        exit_door_unlocked = True
                        print("Bye boss!")
                        is_boss_here = False
                        exit_door_unlocked = False
                        if is_boss_here == False and is_person2_here == False and is_person3_here == False:
                            is_everybody_outside = True
                            print("Everybody is out. Exit door is locked.")
                            break
                        name = str(input("Who is trying to exit the building?: "))
                    elif is_boss_here == False:
                        print("Michael already left.")
                        name = str(input("Who is trying to exit the building?: "))

                if name == "Lincoln":
                    if is_person2_here == True:
                        hours_work = float(input("How many hours have you worked today?: "))
                        if hours_work >= 8:
                            exit_door_unlocked = True
                            print("Bye Lincoln!")
                            is_person2_here = False
                            exit_door_unlocked = False
                            if is_boss_here == False and is_person2_here == False and is_person3_here == False:
                                is_everybody_outside = True
                                print("Everybody is out. Exit door is locked.")
                                break
                            name = str(input("Who is trying to exit the building?: "))
                        elif hours_work < 8:
                            print("You haven't finished working. Go back to work!")
                            name = str(input("Who is trying to exit the building?: "))
                    elif is_person2_here == False:
                        print("Lincoln already left.")
                        name = str(input("Who is trying to exit the building?: "))

                if name == "Brad":
                    if is_person3_here == True:
                        hours_work = float(input("How many hours have you worked today?: "))
                        if hours_work >= 8:
                            exit_door_unlocked = True
                            print("Bye Brad!")
                            is_person3_here = False
                            exit_door_unlocked = False
                            if is_boss_here == False and is_person2_here == False and is_person3_here == False:
                                is_everybody_outside = True
                                print("Everybody is out. Exit door is locked.")
                                break
                            name = str(input("Who is trying to exit the building?: "))
                        elif hours_work < 8:
                            print("You haven't finished working. Go back to work!")
                            name = str(input("Who is trying to exit the building?: "))
                    elif is_person3_here == False:
                        print("Brad already left.")
                        name = str(input("Who is trying to exit the building?: "))

                elif name != "Michael" and name != "Lincoln" and name != "Brad":
                    print("How did you get in? Call security!")
                    break



if __name__ == "__main__":
    main()
