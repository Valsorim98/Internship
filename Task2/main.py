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
        print(f"{name}'s grades are: {grades_list}")
        print(f"{name}'s average grade is: {av_grade}")

    ug.save()
    print("Ready...")

if __name__ == "__main__":
    main()
