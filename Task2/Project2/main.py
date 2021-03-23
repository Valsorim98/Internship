#!/usr/bin/env python
# -*- coding: utf8 -*-

from person import Person

def main():

    enter_door_unlocked = False
    exit_door_unlocked = False

    person1 = Person("Michael", "boss")
    person2 = Person("Lincoln", "worker")
    person3 = Person("Brad", "worker")

    name = str(input("Who is trying to enter the building?: "))

    if name == "Michael":
        enter_door_unlocked = True
        print("The boss came and unlocked the front door.")
    else:
        print("The boss haven't unlocked the door yet.")
        



if __name__ == "__main__":
    main()
