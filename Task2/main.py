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
        for subject in subjects:
            name = student["name"]
            grade = int(input(f"Enter {name}'s grade for {subject}: "))
            grades.append(grade)

    ug.save()
    print("Ready...")

if __name__ == "__main__":
    main()
