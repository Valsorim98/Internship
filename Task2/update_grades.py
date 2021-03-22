from student import Student
from subject import Subject
import os
import json

class UpdateGrades():

    def __init__(self):

        dir_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(dir_path, "database_students.json")

        self.json_content = None
        with open(file_path, 'r') as f:
            content = f.read()
            self.json_content = json.loads(content)
        #print(json_content["Students"][0]["Student1"][0]["name"])


    #def cycle_update(self):
        #i = 4
        #while i < 4:
            #update_grades()
            #i += 1


    def update_grades(self, student):

        #create subjects
        subject1 = Subject("Philosophy")
        subject2 = Subject("Mathematics")
        subject3 = Subject("Finance")
        subject4 = Subject("PE")
        subject5 = Subject("Biology")
        #list of all subjects
        all_subjects = [subject1.name, subject2.name, subject3.name, subject4.name, subject5.name]

        student1 = Student(self.json_content["Students"][0]["Student1"][0]["name"], 20, None)
        
        #grades list from input
        grades_list = []

        #enter student's grade for subjects
        for subject_names in range(len(all_subjects)):
            asdf = student[0]["name"]
            grade = int(input(f"Enter {asdf}'s grade for {all_subjects[subject_names]}: "))
            grades_list.append(grade)
            #prints student's grades from json file
            #print(json_content["Students"][0]["Student1"][0]["grade"][i])
            
        #convert python list to json string
        grades_list_json = json.dumps(grades_list)
        #print(grades_list_json)

        #update student1 grade with grades_list
        with open('Task2/database_students.json', 'r+') as f:
            json_content = json.load(f)
            json_content["Students"][0]["Student1"][0]["grade"] = grades_list_json
            f.seek(0)
            f.truncate()
            json.dump(json_content, f, indent=4)
            

        #prints student's grades as a list from the database
        print(json_content["Students"][0]["Student1"][0]["grade"])
        #print(grades_list)
        
        #for item in json_content["Students"][0]["Student1"]:
            #print(item["grade"][1])

            #print(item)

        student1 = Student(json_content["Students"][0]["Student1"][0]["name"], 20, grade)
        
        print(f"{student1.name}'s grade for {subject1.name} is: {student1.grade}")
