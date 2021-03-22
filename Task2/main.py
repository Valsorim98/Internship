from update_grades import UpdateGrades
import os
import json

def main():

    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, "database_students.json")

    json_content = None
    with open(file_path, 'r') as f:
        content = f.read()
        json_content = json.loads(content)

    student = json_content["Students"][0]["Student1"]
    print(student)
    UpdateGrades().update_grades(student)

    #for item in json_content["Students"][0]:
    #for item in student:
        #print(json_content["Students"][0][item][0]["grade"])
        #print(item)
        #UpdateGrades().update_grades(item)

    

if __name__ == "__main__":
    main()
