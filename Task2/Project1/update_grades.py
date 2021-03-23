#!/usr/bin/env python
# -*- coding: utf8 -*-

from student import Student
from subject import Subject
import os
import json

class UpdateGrades():
    """Database connector.
    """

#region Attributes

    __db_path = ""
    """Database file path.
    """    

    __json_content = None
    """Database content.
    """

#endregion

#region Constructor

    def __init__(self):
        """Constructor
        """

        dir_path = os.path.abspath(os.path.dirname(__file__))
        self.__db_path = os.path.join(dir_path, "database_students.json")

        with open(self.__db_path, 'r') as f:
            content = f.read()
            f.close()
            self.__json_content = json.loads(content)

#endregion

#region Public Methods

    def get_students(self):

        students = None

        if self.__json_content is None:
            return None

        if "students" in self.__json_content:
            students = self.__json_content["students"]

        return students

    def save(self):
        """Save database file.
        """

        with open(self.__db_path, 'w') as f:
            content = json.dumps(self.__json_content, indent=4)
            f.write(content)
            f.close()    

#endregion
