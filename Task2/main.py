#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import json

from update_grades import UpdateGrades

def main():

    subjects = ["Philosophy", "Mathematics", "Finance", "PE", "Biology"]

    ug = UpdateGrades()
    students = ug.get_students()
    
    for student in students:
        grades = student["grade"]
        grades.clear()
        grades_list = []
        for subject in subjects:
            name = student["name"]
            grade = int(input(f"Enter {name}'s grade for {subject}: "))
            grades.append(grade)
            grades_list.append(grade)
        av_grade = sum(grades_list) / len(grades_list)
        print(f"{name}'s average grade is: {av_grade}")
        
        if 4.5 <= av_grade < 5.5:
            good_scholarship = True
        else:
            good_scholarship = False


        if av_grade >= 5.5:
            excellent_scholarship = True
        else:
            excellent_scholarship = False

        if excellent_scholarship == True:
            print(f"{name} gets a scholarship for excellent progress!")

        if good_scholarship == True:
            print(f"{name} gets a scholarship for very good progress!")

        if excellent_scholarship == False and good_scholarship == False:
            print(f"{name} should study more to get a scholarship!")


    ug.save()
    print("Ready...")

if __name__ == "__main__":
    main()
